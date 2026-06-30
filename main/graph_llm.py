#!/usr/bin/env python3
"""LLM helpers for knowledge_graph.py.

This module isolates Ollama access and all LLM-driven ranking/summarization logic
so it can be improved independently from the graph pipeline.

Prompts are loaded from prompts.md (in the same directory).
LLM responses are cached in llm_cache.json to avoid redundant calls.
"""
from __future__ import annotations

import hashlib
import json
import re
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
PROMPTS_FILE = SCRIPT_DIR / "prompts.md"
CACHE_FILE = SCRIPT_DIR / "llm_cache.json"


# --- Prompt loading --------------------------------------------------------

def _load_prompts() -> dict[str, str]:
    """Parse prompts.md into a dict keyed by section heading."""
    if not PROMPTS_FILE.exists():
        return {}
    text = PROMPTS_FILE.read_text(encoding="utf-8")
    sections: dict[str, str] = {}
    current_name: str | None = None
    current_lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("## "):
            if current_name is not None:
                sections[current_name] = "\n".join(current_lines).strip()
            current_name = line[3:].strip()
            current_lines = []
        elif current_name is not None:
            current_lines.append(line)
    if current_name is not None:
        sections[current_name] = "\n".join(current_lines).strip()
    return sections


def _get_prompt(name: str) -> str:
    """Get a prompt template by section name, or return empty string."""
    return _load_prompts().get(name, "")


# --- Cache -----------------------------------------------------------------

_cache: dict[str, str] | None = None


def _load_cache() -> dict[str, str]:
    global _cache
    if _cache is not None:
        return _cache
    if CACHE_FILE.exists():
        try:
            _cache = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            _cache = {}
    else:
        _cache = {}
    return _cache


def _save_cache() -> None:
    if _cache is not None:
        CACHE_FILE.write_text(json.dumps(_cache, indent=2, ensure_ascii=False), encoding="utf-8")


def _cache_key(prefix: str, *parts: str) -> str:
    raw = prefix + "::" + "::".join(parts)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:32]


def _file_hash(path: Path) -> str:
    """Fast hash of file mtime + size to detect changes without reading content."""
    try:
        stat = path.stat()
        return f"{stat.st_mtime_ns}:{stat.st_size}"
    except OSError:
        return "missing"


# --- Ollama API ------------------------------------------------------------

def ollama_available(host: str, model: str) -> bool:
    """Return True if the Ollama server on host has model available."""
    try:
        with urllib.request.urlopen(f"{host}/api/tags", timeout=3) as resp:
            if resp.status != 200:
                return False
            data = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, OSError, json.JSONDecodeError):
        return False
    names = {m.get("name", "") for m in data.get("models", [])}
    if not names:
        print(f"[LLM] {host} is reachable but has no models pulled.")
        return False
    base = model.split(":")[0]
    if model in names or any(n.split(":")[0] == base for n in names):
        return True
    print(f"[LLM] Model '{model}' not found on {host}. Available: {sorted(names)}")
    return False


def find_ollama_host(primary: str, model: str, fallback_hosts: list[str]) -> str | None:
    """Try primary host then fallback hosts; return the first that has model."""
    candidates = [primary] + [h for h in fallback_hosts if h != primary]
    for host in candidates:
        print(f"[LLM] Trying {host} ...")
        if ollama_available(host, model):
            return host
    return None


def ollama_generate(host: str, model: str, prompt: str) -> str:
    """Call Ollama /api/generate and return response text (or empty string)."""
    payload = json.dumps(
        {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.0, "num_predict": 160, "num_ctx": 8192},
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        f"{host}/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return str(data.get("response", "")).strip()
    except (urllib.error.URLError, OSError, json.JSONDecodeError) as exc:
        print(f"[LLM] generate failed: {exc}")
        return ""


# --- Summarize Note (cached) -----------------------------------------------

def enrich_note_summary(note: Any, host: str, model: str) -> None:
    """Populate note.summary with one short LLM summary sentence. Cached."""
    heading_hint = "; ".join(note.headings[:6]) or note.title
    top_terms = " ".join(t for t, _ in note.tokens.most_common(40))

    cache = _load_cache()
    key = _cache_key("summary", str(note.path), _file_hash(note.path), model)
    if key in cache:
        note.summary = cache[key]
        return

    template = _get_prompt("Summarize Note")
    if not template:
        template = (
            "Write ONE short sentence (max 20 words) summarising a technical note.\n"
            "Title: {title}\nKey terms: {top_terms}\nHeadings: {headings}\n"
            "Reply with the sentence only, no labels."
        )
    prompt = template.format(title=note.title, top_terms=top_terms, headings=heading_hint)
    out = ollama_generate(host, model, prompt)
    if not out:
        return
    for line in out.splitlines():
        line = line.strip().lstrip("-:• ")
        for prefix in ("summary:", "sentence:", "answer:"):
            if line.lower().startswith(prefix):
                line = line[len(prefix):].strip()
        if line:
            note.summary = line[:200]
            cache[key] = note.summary
            _save_cache()
            return


# --- Rank Knowledge Files (cached) -----------------------------------------

def llm_rank_knowledge_paths(
    candidates: list[Path],
    project_root: Path,
    host: str,
    model: str,
    max_files: int,
) -> list[Path]:
    """Pick files most important for domain knowledge using local Ollama. Cached."""
    indexed: list[tuple[int, str, str]] = []
    for i, p in enumerate(candidates):
        rel = p.relative_to(project_root).as_posix()
        head = p.read_text(encoding="utf-8", errors="ignore")[:260].replace("\n", " ")
        indexed.append((i, rel, head))

    # Build cache key from file list + hashes
    file_hashes = "::".join(f"{rel}:{_file_hash(p)}" for i, p, rel in [
        (i, candidates[i], candidates[i].relative_to(project_root).as_posix())
        for i in range(len(candidates))
    ])
    cache = _load_cache()
    key = _cache_key("rank", file_hashes, model, str(max_files))
    if key in cache:
        cached_indices = cache[key]
        keep = [int(x) for x in cached_indices.split(",") if x.strip().lstrip("-").isdigit()]
        keep = [i for i in keep if 0 <= i < len(candidates)]
        print(f"[LLM] Using cached ranking ({len(keep)} files)")
        return [candidates[i] for i in keep]

    template = _get_prompt("Rank Knowledge Files")
    if not template:
        template = "Select the most important files. Return JSON: {{\"keep\":[indices]}}"

    prompt = template.format(max_files=max_files)
    for i, rel, head in indexed[:140]:
        prompt += f"\n{i}. {rel} :: {head}"

    out = ollama_generate(host, model, prompt)
    keep: list[int] = []
    if out:
        try:
            payload = json.loads(out)
            keep = [
                int(x)
                for x in payload.get("keep", [])
                if isinstance(x, (int, float, str))
            ]
        except Exception:
            found = re.findall(r"\d+", out)
            keep = [int(x) for x in found]

    keep = [i for i in keep if 0 <= i < len(candidates)]
    uniq: list[int] = []
    seen: set[int] = set()
    for i in keep:
        if i not in seen:
            uniq.append(i)
            seen.add(i)
        if len(uniq) >= max_files:
            break

    # Cache the result
    cache[key] = ",".join(str(i) for i in uniq)
    _save_cache()

    return [candidates[i] for i in uniq]
