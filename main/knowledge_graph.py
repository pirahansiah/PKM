#!/usr/bin/env python3
"""Build an Obsidian-style knowledge graph from the markdown notes in this folder.

Scans every ``*.md`` file in the script directory, extracts front matter, tags,
hashtags, headings and links, computes fuzzy + TF-IDF semantic similarity, and
optionally enriches each note with topics/summaries from a local Ollama model
(``qwen2.5:0.5b``). The result is a single self-contained ``knowledge_graph.html``
with several visualization tabs (force graph, similarity matrix, chord diagram,
tag treemap, cluster bubbles and a sortable node table).

Usage:
    python knowledge_graph.py [--no-llm] [--model qwen2.5:0.5b]
                              [--host http://127.0.0.1:11434]
                              [--sim-threshold 0.18] [--open]
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

from graph_llm import (
  enrich_note_summary,
  find_ollama_host,
  llm_rank_knowledge_paths,
)

# --- Constants -------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_HTML = SCRIPT_DIR / "knowledge_graph.html"
DEFAULT_HOST = "http://127.0.0.1:11434"
DEFAULT_MODEL = "qwen2.5:0.5b"
PROJECT_ROOT = SCRIPT_DIR.parent

PROJECT_FILE_EXTENSIONS = {
  ".md", ".txt", ".rst", ".adoc", ".yaml", ".yml", ".json",
  ".py", ".cpp", ".cc", ".cxx", ".c", ".hpp", ".hh", ".h",
  ".ts", ".js", ".rs",
}

IGNORE_DIR_NAMES = {
    ".git", "__pycache__", ".venv", "venv", "node_modules", "build", "builds",
    ".mypy_cache", ".pytest_cache", "graphify-out", ".conda", "conda",
    "miniconda3", "anaconda3", "site-packages", "pkgs", "envs", "lib", "libs",
    "dlls", "include",
}

LOW_PRIORITY_PATH_HINTS = {
    "old", "backup", "copy", "2025", "20260617", "22012025", "virtual-pen2025",
    ".conda", "site-packages", "anaconda", "miniconda", "env",
  "requirements", ".vscode", "launch.json", "tasks.json", "package-lock", "pnpm-lock",
}

HIGH_PRIORITY_PATH_HINTS = {
    "farshid-vmouse", "vpen-2026", "vpen", "contents", "docs", "readme",
}

HIGH_PRIORITY_NAME_HINTS = {
    "readme", "guide", "summary", "quick_reference", "troubleshooting",
    "adaptation", "plan", "todo", "vpen", "vmouse", "architecture",
}


# Fallback hosts tried in order when the primary is unreachable.
FALLBACK_HOSTS = [
    "http://127.0.0.1:11434",
    "http://localhost:11434",
]

STOPWORDS = {
    "the", "and", "for", "are", "but", "not", "you", "all", "any", "can", "had",
    "her", "was", "one", "our", "out", "has", "use", "with", "this", "that",
    "from", "they", "will", "your", "what", "when", "make", "like", "time",
    "just", "him", "know", "take", "into", "year", "good", "some", "could",
    "them", "than", "then", "look", "only", "come", "over", "also", "back",
    "after", "work", "first", "well", "even", "want", "because", "these",
    "give", "most", "have", "more", "been", "such", "where", "which", "their",
    "would", "there", "should", "about", "other", "using", "used", "each",
    "via", "etc", "using", "based", "between", "within", "while", "must",
}

# --- Data model ------------------------------------------------------------


@dataclass
class Note:
    """A single markdown note and everything extracted from it."""

    path: Path
    name: str
    title: str = ""
    front_matter: dict[str, Any] = field(default_factory=dict)
    fm_tags: set[str] = field(default_factory=set)    # from front matter
    hashtags: set[str] = field(default_factory=set)   # inline #hashtags
    tags: set[str] = field(default_factory=set)        # union of both
    headings: list[str] = field(default_factory=list)
    links: set[str] = field(default_factory=set)
    words: int = 0
    tokens: Counter = field(default_factory=Counter)
    summary: str = ""
    topics: list[str] = field(default_factory=list)
    node_type: str = "file"


# --- Markdown parsing ------------------------------------------------------

_FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
_HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$", re.MULTILINE)
_HASHTAG_RE = re.compile(r"(?:^|\s)#([A-Za-z][A-Za-z0-9_-]+)")
_INLINE_TAG_LINE_RE = re.compile(r"^\s*tags?\s*:\s*(.+?)\s*$", re.IGNORECASE | re.MULTILINE)
_WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")
_MDLINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+\.md)[^)]*\)")
_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9_-]{2,}")


def parse_front_matter(text: str) -> tuple[dict[str, Any], str]:
    """Return (front_matter_dict, body) splitting an optional YAML header."""
    match = _FRONT_MATTER_RE.match(text)
    if not match:
        return {}, text
    raw = match.group(1)
    fm: dict[str, Any] = {}
    key = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if re.match(r"^\s*-\s+", line) and key:
            fm.setdefault(key, [])
            if isinstance(fm[key], list):
                fm[key].append(line.split("-", 1)[1].strip().strip("\"'"))
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip("\"'")
            if value:
                if "," in value:
                    fm[key] = [v.strip() for v in value.split(",") if v.strip()]
                else:
                    fm[key] = value
            else:
                fm[key] = []
    return fm, text[match.end():]


def normalise_link(target: str) -> str:
    """Normalise a link/wikilink target to a comparable note name (no ext)."""
    target = target.strip().split("/")[-1].split("\\")[-1]
    if target.lower().endswith(".md"):
        target = target[:-3]
    return target.strip()


def parse_note(path: Path) -> Note:
    """Read and extract structured data from a single markdown file."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    fm, body = parse_front_matter(text)

    note = Note(path=path, name=path.stem, front_matter=fm)

    # Title: front matter -> first heading -> file stem.
    title = fm.get("title")
    if isinstance(title, list):
        title = title[0] if title else None
    headings = _HEADING_RE.findall(body)
    note.headings = [h.strip() for h in headings]
    note.title = (title or (headings[0].strip() if headings else path.stem))

    # Front-matter tags and inline/body tags tracked separately.
    raw_fm = fm.get("tags") or fm.get("tag") or []
    if isinstance(raw_fm, str):
        raw_fm = [raw_fm]
    inline_tag_lines: set[str] = set()
    for raw in _INLINE_TAG_LINE_RE.findall(body):
      for part in re.split(r"[,;]", raw):
        val = part.strip().lstrip("#").lower()
        if val:
          inline_tag_lines.add(val)

    note.fm_tags = {t.strip().lstrip("#").lower() for t in raw_fm if t.strip()} | inline_tag_lines
    note.hashtags = {t.lower() for t in _HASHTAG_RE.findall(body) if t}
    note.tags = note.fm_tags | note.hashtags

    # Links (wikilinks + markdown .md links).
    links: set[str] = set()
    links.update(normalise_link(t) for t in _WIKILINK_RE.findall(body))
    links.update(normalise_link(t) for t in _MDLINK_RE.findall(body))
    note.links = {link for link in links if link}

    # Tokens for TF-IDF (strip code fences first).
    clean = re.sub(r"```.*?```", " ", body, flags=re.DOTALL)
    clean = re.sub(r"`[^`]*`", " ", clean)
    tokens = [w.lower() for w in _TOKEN_RE.findall(clean)]
    tokens = [w for w in tokens if w not in STOPWORDS]
    note.tokens = Counter(tokens)
    note.words = len(tokens)
    return note


def parse_code_file(path: Path, base_dir: Path) -> Note:
    """Parse a code/config file as a graph node candidate."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    rel_path = path.relative_to(base_dir)
    note = Note(path=path, name=f"code::{rel_path.as_posix()}", node_type="code")
    note.title = rel_path.as_posix()
    note.headings = []
    note.tags = set()
    note.fm_tags = set()
    note.hashtags = set()
    tokens = [w.lower() for w in _TOKEN_RE.findall(text)]
    tokens = [w for w in tokens if w not in STOPWORDS]
    note.tokens = Counter(tokens)
    note.words = len(tokens)
    note.summary = f"Code file with {len(lines)} lines."
    return note


def project_terms_from_notes(notes: list[Note], limit: int = 80) -> set[str]:
    """Build a compact keyword set that represents project intent."""
    c = Counter()
    for n in notes:
        c.update(n.tokens)
        c.update(t.lower() for t in n.topics)
    return {term for term, _ in c.most_common(limit)}


def code_file_score(path: Path, project_terms: set[str]) -> float:
    """Score project file importance for knowledge understanding."""
    rel = path.relative_to(PROJECT_ROOT).as_posix().lower()
    name = path.stem.lower()
    score = 0.0

    if any(h in rel for h in HIGH_PRIORITY_PATH_HINTS):
        score += 3.0
    if any(h in name for h in HIGH_PRIORITY_NAME_HINTS):
        score += 2.5
    ext = path.suffix.lower()
    if ext in {".md", ".txt", ".rst", ".adoc"}:
      score += 2.0
    if ext in {".py", ".cpp", ".cc", ".cxx", ".hpp", ".hh", ".h", ".rs"}:
      score += 1.2
    if any(k in name for k in {"architecture", "pipeline", "transform", "tracking", "camera", "model"}):
      score += 1.0
    if any(h in rel for h in LOW_PRIORITY_PATH_HINTS):
        score -= 4.0

    sample = path.read_text(encoding="utf-8", errors="ignore")[:5000].lower()
    overlap = sum(1 for t in project_terms if len(t) > 3 and t in sample)
    score += min(overlap * 0.2, 3.0)
    # Penalize noisy implementation files but keep concept-defining sources.
    code_signals = sample.count("def ") + sample.count("class ") + sample.count("import ")
    if ext in {".py", ".cpp", ".cc", ".cxx", ".hpp", ".hh", ".h", ".rs"}:
      score -= min(code_signals * 0.07, 1.2)
    else:
      score -= min(code_signals * 0.15, 2.5)
    knowledge_signals = (
        sample.count("purpose") + sample.count("goal") + sample.count("overview")
        + sample.count("setup") + sample.count("troubleshooting") + sample.count("workflow")
    )
    score += min(knowledge_signals * 0.3, 3.0)
    return score


def select_important_code_files(
    notes: list[Note],
    max_files: int = 35,
    llm_host: str | None = None,
    llm_model: str = DEFAULT_MODEL,
) -> list[Path]:
    """Select knowledge-important project files (not environment/implementation noise)."""
    project_terms = project_terms_from_notes(notes)
    candidates: list[tuple[float, Path]] = []
    for path in PROJECT_ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in PROJECT_FILE_EXTENSIONS:
            continue
        parts = {p.lower() for p in path.parts}
        if parts & IGNORE_DIR_NAMES:
            continue
        rel = path.relative_to(PROJECT_ROOT).as_posix().lower()
        # Avoid duplicating note nodes from contents/; focus on project-level knowledge.
        if rel.startswith("contents/"):
            continue
        if any(h in rel for h in LOW_PRIORITY_PATH_HINTS):
            continue
        score = code_file_score(path, project_terms)
        if score >= 3.2:
            candidates.append((score, path))

    candidates.sort(key=lambda x: x[0], reverse=True)
    heuristic = [p for _, p in candidates[: max(max_files * 3, 30)]]

    if llm_host and heuristic:
        picked = llm_rank_knowledge_paths(
            heuristic,
            PROJECT_ROOT,
            llm_host,
            llm_model,
            max_files=max_files,
        )
        if picked:
            return picked
    return heuristic[:max_files]


# --- Similarity ------------------------------------------------------------


def compute_tfidf(notes: list[Note]) -> dict[str, dict[str, float]]:
    """Compute L2-normalised TF-IDF vectors keyed by note name."""
    n_docs = len(notes)
    df: Counter = Counter()
    for note in notes:
        df.update(note.tokens.keys())

    vectors: dict[str, dict[str, float]] = {}
    for note in notes:
        vec: dict[str, float] = {}
        for term, freq in note.tokens.items():
            tf = freq / max(note.words, 1)
            idf = math.log((1 + n_docs) / (1 + df[term])) + 1.0
            vec[term] = tf * idf
        norm = math.sqrt(sum(v * v for v in vec.values())) or 1.0
        vectors[note.name] = {t: v / norm for t, v in vec.items()}
    return vectors


def cosine(a: dict[str, float], b: dict[str, float]) -> float:
    """Cosine similarity between two sparse vectors."""
    if len(a) > len(b):
        a, b = b, a
    return sum(v * b.get(t, 0.0) for t, v in a.items())


def fuzzy_ratio(a: str, b: str) -> float:
    """Fuzzy string similarity in [0, 1]."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def tfidf_topics(note: Note, vectors: "dict[str, dict[str, float]]", n: int = 6) -> list[str]:
    """Return top-n TF-IDF terms for a note as its topic keywords."""
    vec = vectors.get(note.name, {})
    return [t for t, _ in sorted(vec.items(), key=lambda x: -x[1])[:n]]


def top_tfidf_terms(name: str, vectors: "dict[str, dict[str, float]]", n: int = 12) -> list[str]:
  """Return top TF-IDF terms for a node name from a vector map."""
  vec = vectors.get(name, {})
  return [t for t, _ in sorted(vec.items(), key=lambda x: -x[1])[:n]]


def enrich_with_llm(note: Note, host: str, model: str) -> None:
  """Compatibility wrapper; real implementation lives in graph_llm.py."""
  enrich_note_summary(note, host, model)


# --- Graph assembly --------------------------------------------------------


def build_graph(
    notes: list[Note],
    code_notes: list[Note],
    note_vectors: dict[str, dict[str, float]],
    all_vectors: dict[str, dict[str, float]],
    sim_threshold: float,
) -> dict[str, Any]:
    """Assemble nodes, links and derived matrices for the visualizations."""
    name_set = {n.name for n in notes}
    name_lower = {n.name.lower(): n.name for n in notes}

    nodes: list[dict[str, Any]] = []
    links: list[dict[str, Any]] = []

    # File nodes.
    for note in notes:
        search_terms = " ".join(top_tfidf_terms(note.name, note_vectors, 20))
        rel_path = note.path.relative_to(PROJECT_ROOT).as_posix()
        web_url = "/contents/" + rel_path.rsplit(".", 1)[0] + "/"
        nodes.append({
            "id": note.name,
            "label": note.title or note.name,
            "type": "file",
            "url": web_url,
            "summary": note.summary,
            "tags": sorted(note.tags),
            "topics": note.topics,
            "headings": note.headings[:12],
            "words": note.words,
            "path": rel_path,
            "search_text": (
                f"{note.title} {note.summary} "
                f"{' '.join(sorted(note.tags))} {' '.join(note.topics)} "
                f"{' '.join(note.headings[:12])} {search_terms}"
            ).lower(),
        })

    # Explicit links (wikilink / markdown link), resolved by name or fuzzy.
    for note in notes:
        for target in note.links:
            resolved = None
            if target in name_set:
                resolved = target
            elif target.lower() in name_lower:
                resolved = name_lower[target.lower()]
            else:
                best, score = None, 0.0
                for other in name_set:
                    r = fuzzy_ratio(target, other)
                    if r > score:
                        best, score = other, r
                if score >= 0.82:
                    resolved = best
            if resolved and resolved != note.name:
                links.append({
                    "source": note.name, "target": resolved,
                    "type": "link", "weight": 1.0,
                })

    # FM tag nodes (type="tag") and inline hashtag nodes (type="hashtag").
    tag_to_files: dict[str, list[str]] = defaultdict(list)
    hashtag_to_files: dict[str, list[str]] = defaultdict(list)
    for note in notes:
        for tag in note.fm_tags:
            tag_to_files[tag].append(note.name)
        for tag in note.hashtags:
            if tag not in note.fm_tags:
                hashtag_to_files[tag].append(note.name)
            else:
                tag_to_files[tag].append(note.name)  # promote to fm_tag node
    for tag, files in tag_to_files.items():
        tag_clean = re.sub(r'[^\w-]', '', tag)
        tag_id = f"#tag:{tag_clean}"
        nodes.append({
            "id": tag_id, "label": f"#{tag}", "type": "tag",
            "summary": f"Front-matter tag in {len(files)} note(s)",
            "tags": [], "topics": [], "headings": [],
            "words": len(files), "path": "",
          "search_text": f"#{tag} front matter tag {tag} {' '.join(files)}".lower(),
        })
        for fname in files:
            links.append({"source": fname, "target": tag_id, "type": "tag", "weight": 0.6})
    for tag, files in hashtag_to_files.items():
        tag_clean = re.sub(r'[^\w-]', '', tag)
        tag_id = f"#hashtag:{tag_clean}"
        nodes.append({
            "id": tag_id, "label": f"#{tag}", "type": "hashtag",
            "summary": f"Inline hashtag in {len(files)} note(s)",
            "tags": [], "topics": [], "headings": [],
            "words": len(files), "path": "",
          "search_text": f"#{tag} hashtag inline {tag} {' '.join(files)}".lower(),
        })
        for fname in files:
            links.append({"source": fname, "target": tag_id, "type": "hashtag", "weight": 0.55})

    # Topic nodes (from LLM) + file<->topic edges.
    topic_to_files: dict[str, list[str]] = defaultdict(list)
    for note in notes:
        for topic in note.topics:
            topic_to_files[topic].append(note.name)
    for topic, files in topic_to_files.items():
        if len(files) < 1:
            continue
        topic_id = f"#topic:{topic}"
        nodes.append({
            "id": topic_id, "label": topic, "type": "topic",
            "summary": f"LLM topic across {len(files)} note(s)",
            "tags": [], "topics": [], "headings": [],
            "words": len(files), "path": "",
          "search_text": f"{topic} topic semantic {' '.join(files)}".lower(),
        })
        for fname in files:
            links.append({
                "source": fname, "target": topic_id,
                "type": "topic", "weight": 0.5,
            })

    # Code file nodes.
    for code in code_notes:
        rel_path = code.path.relative_to(PROJECT_ROOT).as_posix()
        nodes.append({
            "id": code.name,
            "label": code.title or code.name,
            "type": "code",
            "url": "/contents/" + rel_path.rsplit(".", 1)[0] + "/" if rel_path.endswith(".md") else "",
            "summary": code.summary,
            "tags": [], "topics": code.topics, "headings": [],
            "words": code.words, "path": rel_path,
            "search_text": f"{code.title} {code.summary}".lower(),
        })

    # Semantic similarity edges + full matrix (file x file).
    file_names = [n.name for n in notes]
    matrix = [[0.0] * len(file_names) for _ in file_names]
    for i, a in enumerate(file_names):
      for j in range(i + 1, len(file_names)):
        b = file_names[j]
        sim = cosine(note_vectors[a], note_vectors[b])
        matrix[i][j] = matrix[j][i] = round(sim, 4)
        if sim >= sim_threshold:
          links.append({
            "source": a, "target": b,
            "type": "similar", "weight": round(sim, 3),
          })

    # Code <-> markdown semantic edges: top matches per code file.
    for code in code_notes:
        sims: list[tuple[float, str]] = []
        for note in notes:
            sim = cosine(all_vectors.get(code.name, {}), all_vectors.get(note.name, {}))
            if sim >= 0.08:
                sims.append((sim, note.name))
        sims.sort(reverse=True)
        for sim, target in sims[:4]:
            links.append({
                "source": code.name,
                "target": target,
                "type": "code-semantic",
                "weight": round(sim, 3),
            })

    # Connected-component grouping (union-find over all edges).
    parent = {n["id"]: n["id"] for n in nodes}

    def find(x: str) -> str:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: str, b: str) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for link in links:
        if link["source"] in parent and link["target"] in parent:
            union(link["source"], link["target"])
    groups: dict[str, int] = {}
    for node in nodes:
        root = find(node["id"])
        node["group"] = groups.setdefault(root, len(groups))

    # Degree as node size driver.
    degree: Counter = Counter()
    for link in links:
        degree[link["source"]] += 1
        degree[link["target"]] += 1
    for node in nodes:
        node["degree"] = degree[node["id"]]

    return {
        "nodes": nodes,
        "links": links,
        "matrix": {"labels": file_names, "values": matrix},
        "tags": {t: len(f) for t, f in sorted(tag_to_files.items())},
        "hashtags": {t: len(f) for t, f in sorted(hashtag_to_files.items())},
        "topics": {t: len(f) for t, f in sorted(topic_to_files.items())},
        "code_count": len(code_notes),
    }


# --- graph.json export (for Jekyll site rendering) ---------------------------

# Map knowledge_graph node types to graph-view.js categories.
_TYPE_TO_CATEGORY = {
    "file": "page",
    "code": "page",
    "tag": "tag",
    "hashtag": "tag",
    "topic": "tag",
    "project": "hub",
}

# Hub definitions that get injected as top-level nodes.
_HUBS = [
    {"id": "hub-product", "label": "Product", "url": "/contents/public/product/"},
    {"id": "hub-research", "label": "Research", "url": "/contents/public/research/"},
    {"id": "hub-solutions", "label": "Solutions", "url": "/contents/public/solutions/"},
    {"id": "hub-content", "label": "Content Hub", "url": "/contents/public/"},
    {"id": "hub-wiki", "label": "Wiki", "url": "/contents/wiki/"},
    {"id": "hub-portfolio", "label": "Portfolio", "url": "/contents/pkm/use-cases/"},
]


def _note_url(note: Note) -> str:
    """Derive a Jekyll permalink-style URL from a note's path."""
    rel = note.path.relative_to(PROJECT_ROOT).with_suffix("")
    return "/" + rel.as_posix() + "/"


def export_graph_json(data: dict[str, Any]) -> dict[str, Any]:
    """Convert knowledge_graph internal format to graph-view.js format."""
    node_id_set = {n["id"] for n in data["nodes"]}
    kg_nodes = {n["id"]: n for n in data["nodes"]}

    # Start with hub nodes.
    nodes: list[dict[str, Any]] = []
    for hub in _HUBS:
        nodes.append({**hub, "category": "hub", "size": 5})

    # Add file/tag/topic nodes.
    for n in data["nodes"]:
        cat = _TYPE_TO_CATEGORY.get(n["type"], "page")
        url = n.get("url", "")
        if not url and n["type"] == "file":
            # Try to derive URL from path.
            path_str = n.get("path", "")
            if path_str and path_str.endswith(".md"):
                url = "/" + path_str[:-3] + "/"
        size = max(1, min(5, (n.get("degree", 0) or 0) // 3 + 1))
        nodes.append({
            "id": n["id"],
            "label": n.get("label", n["id"]),
            "url": url,
            "category": cat,
            "size": size,
        })

    # Convert links — resolve string IDs to indices.
    idx_map = {n["id"]: i for i, n in enumerate(nodes)}
    links: list[dict[str, Any]] = []
    for l in data["links"]:
        src = l["source"] if isinstance(l["source"], str) else l["source"].get("id", l["source"])
        tgt = l["target"] if isinstance(l["target"], str) else l["target"].get("id", l["target"])
        if src in idx_map and tgt in idx_map and src != tgt:
            links.append({
                "source": src,
                "target": tgt,
                "strength": round(l.get("weight", l.get("strength", 0.5)), 3),
            })

    # Add hub-to-page links for top-level content.
    page_urls = {n.get("url", ""): n["id"] for n in nodes if n.get("url")}
    for hub in _HUBS:
        hub_id = hub["id"]
        for node in nodes:
            if node["category"] == "page" and node.get("url", "").startswith(hub["url"][:hub["url"].rfind("/", 0, -1) + 1]):
                if node["id"] in idx_map and hub_id in idx_map:
                    links.append({"source": hub_id, "target": node["id"], "strength": 0.3})

    return {"nodes": nodes, "links": links}


# --- HTML rendering --------------------------------------------------------


def render_html(data: dict[str, Any], meta: dict[str, Any]) -> str:
    """Inject the graph data into the self-contained HTML template."""
    payload = json.dumps(data, ensure_ascii=False)
    meta_json = json.dumps(meta, ensure_ascii=False)
    return HTML_TEMPLATE.replace("/*__DATA__*/", payload).replace(
        "/*__META__*/", meta_json
    )


# --- Main ------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build an Obsidian-style knowledge graph HTML from markdown notes.",
    )
    parser.add_argument("--no-llm", action="store_true",
                        help="Disable Ollama enrichment (local techniques only).")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"Ollama model name (default: {DEFAULT_MODEL}).")
    parser.add_argument("--host", default=DEFAULT_HOST,
                        help=f"Ollama base URL (default: {DEFAULT_HOST}).")
    parser.add_argument("--sim-threshold", type=float, default=0.18,
                        help="Min TF-IDF cosine to draw a similarity edge.")
    parser.add_argument("--max-code-files", type=int, default=35,
              help="Max important code files to add as project nodes.")
    parser.add_argument("--open", action="store_true",
                        help="Open the generated HTML in the default browser.")
    args = parser.parse_args()

    md_files = sorted(PROJECT_ROOT.rglob("*.md"))
    md_files = [p for p in md_files if not p.name.startswith("._")]
    if not md_files:
        print(f"[SCAN] No markdown files found in {PROJECT_ROOT}")
        return 1
    print(f"[SCAN] Found {len(md_files)} markdown notes in {PROJECT_ROOT.name}/")

    notes = [parse_note(p) for p in md_files]
    for note in notes:
        print(f"[PARSE] {note.name}: {note.words} words, "
              f"{len(note.fm_tags)} fm_tags, {len(note.hashtags)} hashtags, "
              f"{len(note.links)} links")

    print("[SIM] Computing TF-IDF vectors and cosine similarity...")
    vectors = compute_tfidf(notes)

    active_host: str | None = None
    use_llm = not args.no_llm
    if use_llm:
        active_host = find_ollama_host(args.host, args.model, FALLBACK_HOSTS)
        if active_host:
            print(f"[LLM] Using {active_host} with {args.model}")
            for note in notes:
                enrich_with_llm(note, active_host, args.model)
                print(f"[LLM] {note.name} -> {note.summary[:60]!r}")
        else:
            print("[LLM] No Ollama endpoint found; using local techniques only.")
            use_llm = False
    else:
        print("[LLM] Disabled by --no-llm; using local techniques only.")

    # Always derive topics from TF-IDF top terms (more reliable than small LLM).
    for note in notes:
        if not note.topics:
            note.topics = tfidf_topics(note, vectors)

    print("[PROJECT] Selecting knowledge-important project files...")
    selected_code_paths = select_important_code_files(
        notes,
        max_files=args.max_code_files,
        llm_host=active_host,
        llm_model=args.model,
    )
    code_notes = [parse_code_file(p, PROJECT_ROOT) for p in selected_code_paths]
    for code in code_notes[:12]:
        print(f"[PROJECT] + {code.path.relative_to(PROJECT_ROOT).as_posix()}")
    if len(code_notes) > 12:
        print(f"[PROJECT] ... and {len(code_notes) - 12} more")

    all_vectors = compute_tfidf(notes + code_notes) if code_notes else vectors
    # Re-use the already-computed vectors below.
    print("[GRAPH] Assembling nodes, links and matrices...")
    data = build_graph(notes, code_notes, vectors, all_vectors, args.sim_threshold)
    meta = {
        "source_dir": str(SCRIPT_DIR),
        "note_count": len(notes),
      "code_count": len(code_notes),
        "node_count": len(data["nodes"]),
        "link_count": len(data["links"]),
        "llm_used": use_llm,
        "model": args.model if use_llm else "",
        "sim_threshold": args.sim_threshold,
    }

    print(f"[WRITE] {OUTPUT_HTML.name} "
          f"({meta['node_count']} nodes, {meta['link_count']} links)")
    OUTPUT_HTML.write_text(render_html(data, meta), encoding="utf-8")

    # Also export graph.json for Jekyll site rendering.
    graph_json_path = SCRIPT_DIR.parent.parent / "assets" / "graph.json"
    graph_json = export_graph_json(data)
    graph_json_path.write_text(
        json.dumps(graph_json, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"[WRITE] {graph_json_path.name} "
          f"({len(graph_json['nodes'])} nodes, {len(graph_json['links'])} links)")

    if args.open:
        import webbrowser
        webbrowser.open(OUTPUT_HTML.as_uri())
    print(f"[DONE] {OUTPUT_HTML}")
    return 0


# --- HTML template (D3 v7, multi-tab) --------------------------------------

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />

<script src="https://d3js.org/d3.v7.min.js"></script>
<style>
  :root{
    --bg:#0d1117; --panel:#161b22; --border:#30363d; --fg:#e6edf3;
    --muted:#8b949e; --accent:#58a6ff; --file:#58a6ff; --tag:#3fb950;
    --hashtag:#f78166; --topic:#d29922; --sim:#a371f7; --code:#56d364; --project:#ff7b72;
  }
  *{box-sizing:border-box}
  html,body{margin:0;height:100%;background:var(--bg);color:var(--fg);
    font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}
  header{padding:10px 16px;border-bottom:1px solid var(--border);
    display:flex;align-items:center;gap:16px;flex-wrap:wrap;position:relative;z-index:120}
  header h1{font-size:16px;margin:0;font-weight:600}
  header .meta{color:var(--muted);font-size:12px}
  .tabs{display:flex;gap:4px;padding:8px 16px 0;border-bottom:1px solid var(--border);
    flex-wrap:wrap;background:var(--panel);position:relative;z-index:120}
  .tab{padding:8px 14px;cursor:pointer;border:1px solid transparent;
    border-bottom:none;border-radius:6px 6px 0 0;color:var(--muted);font-size:13px}
  .tab:hover{color:var(--fg)}
  .tab.active{background:var(--bg);color:var(--fg);border-color:var(--border)}
  .view{display:none;position:absolute;top:108px;bottom:0;left:0;right:0;overflow:auto;z-index:1}
  .view.active{display:block}
  svg{width:100%;height:100%;display:block}
  .controls{position:absolute;top:116px;right:18px;z-index:10;background:var(--panel);
    border:1px solid var(--border);border-radius:8px;padding:10px;font-size:12px;width:210px}
  .controls label{display:flex;align-items:center;gap:6px;margin:4px 0;cursor:pointer}
  .controls input[type=text]{width:100%;background:var(--bg);color:var(--fg);
    border:1px solid var(--border);border-radius:5px;padding:5px;margin-bottom:6px}
  .legend{display:flex;gap:14px;padding:8px 16px;font-size:12px;color:var(--muted);flex-wrap:wrap;position:relative;z-index:120}
  .legend span{display:inline-flex;align-items:center;gap:5px}
  .dot{width:10px;height:10px;border-radius:50%}
  .tooltip{position:absolute;pointer-events:none;background:#1c2128;border:1px solid var(--border);
    border-radius:6px;padding:8px 10px;font-size:12px;max-width:320px;color:var(--fg);
    box-shadow:0 4px 16px rgba(0,0,0,.5);z-index:50;opacity:0;transition:opacity .1s}
  #detail-panel{position:fixed;right:0;top:108px;bottom:0;width:296px;
    background:var(--panel);border-left:1px solid var(--border);
    padding:16px;overflow-y:auto;display:none;z-index:30;font-size:12px}
  #detail-panel h2{font-size:14px;margin:0 0 10px;padding-right:24px}
  #dp-close{position:absolute;right:14px;cursor:pointer;color:var(--muted);font-size:20px;line-height:1}
  .dp-row{margin:5px 0}.dp-row b{color:var(--muted)}
  .node-label{font-size:10px;fill:var(--muted);pointer-events:none}
  .node-selected{stroke:#ffffff;stroke-width:2.6px}
  .label-selected{font-weight:700;fill:#ffffff}
  table{border-collapse:collapse;width:calc(100% - 32px);margin:16px;font-size:13px}
  th,td{border:1px solid var(--border);padding:6px 10px;text-align:left}
  th{background:var(--panel);cursor:pointer;position:sticky;top:0}
  tr:hover{background:#1c2128}
  .pill{display:inline-block;background:#21262d;border:1px solid var(--border);
    border-radius:10px;padding:1px 7px;margin:1px;font-size:11px}
  .axis text{fill:var(--muted);font-size:10px}
  .cell-label{fill:var(--muted);font-size:10px}
</style>
</head>
<body>
<header>
 
  <span class="meta" id="meta"></span>
</header>
<div class="tabs" id="tabs"></div>
<div class="legend">
  <span><span class="dot" style="background:var(--file)"></span>Note</span>
  <span><span class="dot" style="background:var(--tag)"></span>FM Tag</span>
  <span><span class="dot" style="background:var(--hashtag)"></span>#Hashtag</span>
  <span><span class="dot" style="background:var(--code)"></span>Code</span>
  <span><span class="dot" style="background:var(--project)"></span>Project</span>
  <span><span class="dot" style="background:var(--topic)"></span>LLM topic</span>
  <span><span class="dot" style="background:var(--sim)"></span>Similarity edge</span>
</div>

<div class="view active" id="view-graph"><svg id="svg-graph"></svg></div>
<div class="view" id="view-matrix"><svg id="svg-matrix"></svg></div>
<div class="view" id="view-chord"><svg id="svg-chord"></svg></div>
<div class="view" id="view-tags"><svg id="svg-tags"></svg></div>
<div class="view" id="view-clusters"><svg id="svg-clusters"></svg></div>
<div class="view" id="view-table"><div id="table-wrap"></div></div>

<div id="detail-panel">
  <span id="dp-close">×</span>
  <h2 id="dp-title"></h2>
  <div id="dp-body"></div>
</div>

<div class="controls" id="graph-controls">
  <input type="text" id="search" placeholder="Semantic + fuzzy search (shows only relevant nodes)..." />
  <label><input type="checkbox" class="ftype" value="link" checked> links</label>
  <label><input type="checkbox" class="ftype" value="similar" checked> similarity</label>
  <label><input type="checkbox" class="ftype" value="tag" checked> FM tags</label>
  <label><input type="checkbox" class="ftype" value="hashtag" checked> hashtags</label>
  <label><input type="checkbox" class="ftype" value="topic" checked> topics</label>
  <label><input type="checkbox" class="ftype" value="project" checked> project links</label>
  <label><input type="checkbox" class="ftype" value="code-semantic" checked> code semantics</label>
  <label><input type="range" id="charge" min="50" max="600" value="240"> spread</label>
</div>

<div class="tooltip" id="tooltip"></div>

<script>
const DATA = /*__DATA__*/;
const META = /*__META__*/;
const color = {
  file:"#58a6ff", tag:"#3fb950", hashtag:"#f78166", topic:"#d29922",
  code:"#56d364", project:"#ff7b72"
};
const linkColor = {
  link:"#58a6ff", similar:"#a371f7", tag:"#3fb950", hashtag:"#f78166", topic:"#d29922",
  project:"#ff7b72", "code-semantic":"#56d364"
};
const tip = d3.select("#tooltip");

document.getElementById("meta").textContent =
  `${META.note_count} notes · ${META.node_count} nodes · ${META.link_count} links · ` +
  `${META.code_count||0} code files · ` +
  (META.llm_used ? `LLM: ${META.model}` : "local techniques only");

// --- Tabs ---
const TABS = [
  ["graph","Graph"],["matrix","Similarity Matrix"],["chord","Chord"],
  ["tags","Tags & Topics"],["clusters","Clusters"],["table","Node Table"]
];
const tabsEl = document.getElementById("tabs");
const rendered = {};
TABS.forEach(([id,label],i)=>{
  const d = document.createElement("div");
  d.className = "tab" + (i===0?" active":"");
  d.textContent = label;
  d.onclick = ()=>activate(id,d);
  tabsEl.appendChild(d);
});
function activate(id, el){
  document.querySelectorAll(".tab").forEach(t=>t.classList.remove("active"));
  el.classList.add("active");
  document.querySelectorAll(".view").forEach(v=>v.classList.remove("active"));
  document.getElementById("view-"+id).classList.add("active");
  document.getElementById("graph-controls").style.display = id==="graph"?"block":"none";
  if(!rendered[id]){ renderers[id](); rendered[id]=true; }
}
function size(svgSel){
  const el = svgSel.node().parentNode;
  return [el.clientWidth, el.clientHeight];
}

// --- 1. Force graph ---
function renderGraph(){
  const svg = d3.select("#svg-graph");
  const [W,H] = size(svg);
  const g = svg.append("g");
  svg.call(d3.zoom().scaleExtent([0.2,4]).on("zoom",e=>g.attr("transform",e.transform)));
  svg.on("click",closeDetail);

  const nodes = DATA.nodes.map(d=>Object.assign({},d));
  const links = DATA.links.map(d=>Object.assign({},d));
  let selectedId = null;
  
  const savedPos = loadSavedPositions();

  // Restore pinned positions from previous interactions.
  nodes.forEach(d=>{
    const p = savedPos[d.id];
    if(p && Number.isFinite(p.x) && Number.isFinite(p.y)){
      d.x = p.x; d.y = p.y; d.fx = p.x; d.fy = p.y;
    }
  });

  const sim = d3.forceSimulation(nodes)
    .force("link", d3.forceLink(links).id(d=>d.id).distance(d=>d.type==="similar"?120:70))
    .force("charge", d3.forceManyBody().strength(-240))
    .force("center", d3.forceCenter(W/2,H/2))
    .force("collide", d3.forceCollide().radius(d=>radius(d)+4));

  const link = g.append("g").selectAll("line").data(links).join("line")
    .attr("stroke",d=>linkColor[d.type]).attr("stroke-opacity",0.4)
    .attr("stroke-width",d=>d.type==="similar"?d.weight*3:1.2)
    .attr("data-type",d=>d.type);

  const node = g.append("g").selectAll("circle").data(nodes).join("circle")
    .attr("r",radius).attr("fill",d=>color[d.type]).attr("stroke","#0d1117").attr("stroke-width",1.5)
    .style("cursor","pointer")
    .call(drag(sim))
    .on("mouseover",(e,d)=>showTip(e,d)).on("mousemove",moveTip).on("mouseout",hideTip)
    .on("click",(e,d)=>{
      e.stopPropagation();
      if(e.ctrlKey || e.metaKey){
        openRelevantFile(d);
        return;
      }
      selectedId = d.id;
      applySelectionStyles();
      showDetail(d);
    })
    .on("dblclick",(e,d)=>{
      // Shift+double-click unlocks a previously pinned node.
      if(!e.shiftKey) return;
      d.fx = null;
      d.fy = null;
      delete savedPos[d.id];
      savePositions(savedPos);
      sim.alpha(0.35).restart();
    });

  const labels = g.append("g").selectAll("text").data(nodes).join("text")
    .attr("class","node-label").attr("dx",d=>radius(d)+2).attr("dy",3)
    .text(d=>shortLabel(d));

  sim.on("tick",()=>{
    link.attr("x1",d=>d.source.x).attr("y1",d=>d.source.y)
        .attr("x2",d=>d.target.x).attr("y2",d=>d.target.y);
    node.attr("cx",d=>d.x).attr("cy",d=>d.y);
    labels.attr("x",d=>d.x).attr("y",d=>d.y);
  });

  function radius(d){ return d.type==="file" ? 6+Math.sqrt(d.degree||1)*2.4 : 4+Math.sqrt(d.degree||1)*1.6; }

  function shortLabel(d){
    const raw = (d.label || d.id || "").trim();
    const maxLen = d.type === "file" ? 26 : 16;
    if(!raw) return "";
    return raw.length > maxLen ? raw.slice(0, maxLen - 1) + "…" : raw;
  }

  document.querySelectorAll(".ftype").forEach(cb=>cb.onchange=()=>{
    const on = new Set([...document.querySelectorAll(".ftype:checked")].map(c=>c.value));
    link.style("display",d=>on.has(d.type)?null:"none");
    applySelectionStyles();
  });
  document.getElementById("charge").oninput = e=>{
    sim.force("charge").strength(-e.target.value); sim.alpha(0.4).restart();
  };
  document.getElementById("search").oninput = e=>{
    const q = e.target.value.toLowerCase().trim();
    if(!q){
      node.style("display",null).attr("opacity",1);
      labels.style("display",null).attr("opacity",1);
      link.style("display",d=>{
        const on = new Set([...document.querySelectorAll(".ftype:checked")].map(c=>c.value));
        return on.has(d.type)?null:"none";
      });
      selectedId = null;
      applySelectionStyles();
      return;
    }
    const terms = q.split(/\s+/).filter(Boolean);
    const score = d=>{
      const text = `${d.label||""} ${d.summary||""} ${d.search_text||""}`.toLowerCase();
      let s = 0;
      for(const t of terms){
        if(text.includes(t)) s += 1.4;
      }
      // Lightweight fuzzy on label by character order overlap.
      const lbl = (d.label||"").toLowerCase();
      let i=0,j=0,m=0;
      while(i<lbl.length && j<q.length){ if(lbl[i]===q[j]){m++;j++;} i++; }
      const fuzzy = q.length ? (m / q.length) : 0;
      s += fuzzy;
      return s;
    };

    const ranked = nodes.map(d=>({id:d.id, s:score(d)})).sort((a,b)=>b.s-a.s);
    const best = ranked.length ? ranked[0] : null;
    const matched = new Set();
    if(best && best.s >= 1.2){
      selectedId = best.id;
      const oneHop = buildNeighborSet(best.id);
      oneHop.forEach(id=>matched.add(id));
    } else {
      selectedId = null;
    }

    node.style("display",d=>matched.has(d.id)?null:"none").attr("opacity",d=>matched.has(d.id)?1:0.05);
    labels.style("display",d=>matched.has(d.id)?null:"none").attr("opacity",d=>matched.has(d.id)?1:0.05);
    link.style("display",d=>{
      const on = new Set([...document.querySelectorAll(".ftype:checked")].map(c=>c.value));
      const s = typeof d.source === "object" ? d.source.id : d.source;
      const t = typeof d.target === "object" ? d.target.id : d.target;
      if(!on.has(d.type)) return "none";
      return (matched.has(s) && matched.has(t)) ? null : "none";
    });
    applySelectionStyles();
  };

  function buildNeighborSet(id){
    const near = new Set([id]);
    links.forEach(l=>{
      const s = typeof l.source === "object" ? l.source.id : l.source;
      const t = typeof l.target === "object" ? l.target.id : l.target;
      if(s === id) near.add(t);
      if(t === id) near.add(s);
    });
    return near;
  }

  function applySelectionStyles(){
    if(!selectedId){
      node.classed("node-selected",false).attr("opacity",1);
      labels.classed("label-selected",false).attr("opacity",1);
      link.attr("stroke-opacity",0.4);
      return;
    }
    const near = buildNeighborSet(selectedId);
    node.classed("node-selected",d=>d.id===selectedId)
      .attr("opacity",d=>near.has(d.id)?1:0.15);
    labels.classed("label-selected",d=>d.id===selectedId)
      .attr("opacity",d=>near.has(d.id)?1:0.22);
    link.attr("stroke-opacity",d=>{
      const s = typeof d.source === "object" ? d.source.id : d.source;
      const t = typeof d.target === "object" ? d.target.id : d.target;
      if(s===selectedId || t===selectedId) return 0.95;
      if(near.has(s) && near.has(t)) return 0.45;
      return 0.08;
    });
  }

  function clearSelection(){
    selectedId = null;
    applySelectionStyles();
    closeDetail();
  }

  function loadSavedPositions(){
    try{
      return JSON.parse(window.localStorage.getItem(POS_KEY) || "{}") || {};
    }catch(_){
      return {};
    }
  }

  function savePositions(data){
    try{ window.localStorage.setItem(POS_KEY, JSON.stringify(data)); }catch(_){}
  }

  svg.on("click",clearSelection);
}

function drag(sim){
  return d3.drag()
    .on("start",(e,d)=>{ if(!e.active) sim.alphaTarget(0.3).restart(); d.fx=d.x; d.fy=d.y; })
    .on("drag",(e,d)=>{ d.fx=e.x; d.fy=e.y; })
    .on("end",(e,d)=>{
      if(!e.active) sim.alphaTarget(0);
      // Keep node pinned where dropped.
      d.fx = e.x;
      d.fy = e.y;
      try{
        
        const cur = JSON.parse(window.localStorage.getItem(key) || "{}");
        cur[d.id] = {x:d.fx, y:d.fy};
        window.localStorage.setItem(key, JSON.stringify(cur));
      }catch(_){ }
    });
}
function showTip(e,d){
  let html = `<b>${d.label}</b> <span style="color:#8b949e">(${d.type})</span>`;
  if(d.summary) html += `<br>${d.summary}`;
  if(d.tags&&d.tags.length) html += `<br>tags: ${d.tags.map(t=>"#"+t).join(" ")}`;
  if(d.topics&&d.topics.length) html += `<br>topics: ${d.topics.join(", ")}`;
  if(d.words) html += `<br><span style="color:#8b949e">${d.words} words · degree ${d.degree||0}</span>`;
  tip.html(html).style("opacity",1); moveTip(e);
}
function moveTip(e){ tip.style("left",(e.clientX+14)+"px").style("top",(e.clientY+14)+"px"); }
function hideTip(){ tip.style("opacity",0); }

// --- 2. Similarity matrix ---
function renderMatrix(){
  const svg = d3.select("#svg-matrix");
  const labels = DATA.matrix.labels, vals = DATA.matrix.values;
  const n = labels.length, pad=160, cell=Math.min(46,(Math.min(900,window.innerWidth)-pad)/Math.max(n,1));
  const W = pad+cell*n+40, H = pad+cell*n+40;
  svg.attr("viewBox",`0 0 ${W} ${H}`);
  const g = svg.append("g").attr("transform",`translate(${pad},${pad})`);
  const sc = d3.scaleSequential(d3.interpolateViridis).domain([0,1]);
  for(let i=0;i<n;i++) for(let j=0;j<n;j++){
    g.append("rect").attr("x",j*cell).attr("y",i*cell).attr("width",cell-1).attr("height",cell-1)
      .attr("fill", i===j?"#21262d":sc(vals[i][j]))
      .on("mouseover",e=>{tip.html(`<b>${labels[i]}</b> ↔ <b>${labels[j]}</b><br>cosine: ${vals[i][j].toFixed(3)}`).style("opacity",1);moveTip(e);})
      .on("click",e=>{
        const id = labels[i];
        if(e.ctrlKey || e.metaKey){
          openRelevantById(id);
          return;
        }
        const node = DATA.nodes.find(n=>n.id===id);
        if(node) showDetail(node);
      })
      .on("mousemove",moveTip).on("mouseout",hideTip);
  }
  g.selectAll(".rl").data(labels).join("text").attr("class","cell-label")
    .attr("x",-8).attr("y",(d,i)=>i*cell+cell/2+3).attr("text-anchor","end").text(d=>d);
  g.selectAll(".cl").data(labels).join("text").attr("class","cell-label")
    .attr("transform",(d,i)=>`translate(${i*cell+cell/2},-8) rotate(-45)`).text(d=>d);
}

// --- 3. Chord diagram (note-to-note, link+similarity weights) ---
function renderChord(){
  const svg = d3.select("#svg-chord");
  const [W,H] = size(svg); const R = Math.min(W,H)/2-90;
  const files = DATA.nodes.filter(d=>d.type==="file").map(d=>d.id);
  const idx = new Map(files.map((f,i)=>[f,i]));
  const m = files.map(()=>files.map(()=>0));
  DATA.links.forEach(l=>{
    const s = typeof l.source==="object"?l.source.id:l.source;
    const t = typeof l.target==="object"?l.target.id:l.target;
    if((l.type==="link"||l.type==="similar") && idx.has(s) && idx.has(t)){
      m[idx.get(s)][idx.get(t)] += l.weight; m[idx.get(t)][idx.get(s)] += l.weight;
    }
  });
  const g = svg.append("g").attr("transform",`translate(${W/2},${H/2})`);
  const chord = d3.chord().padAngle(0.05)(m);
  const col = d3.scaleOrdinal(d3.schemeTableau10);
  g.append("g").selectAll("path").data(chord.groups).join("path")
    .attr("d",d3.arc().innerRadius(R).outerRadius(R+14))
    .attr("fill",d=>col(d.index)).attr("stroke","#0d1117")
    .on("mouseover",(e,d)=>{tip.html(`<b>${files[d.index]}</b>`).style("opacity",1);moveTip(e);})
    .on("click",(e,d)=>{
      const id = files[d.index];
      if(e.ctrlKey || e.metaKey){
        openRelevantById(id);
        return;
      }
      const node = DATA.nodes.find(n=>n.id===id);
      if(node) showDetail(node);
    })
    .on("mousemove",moveTip).on("mouseout",hideTip);
  g.append("g").attr("fill-opacity",0.62).selectAll("path").data(chord).join("path")
    .attr("d",d3.ribbon().radius(R)).attr("fill",d=>col(d.source.index)).attr("stroke","#0d1117");
  g.selectAll(".lbl").data(chord.groups).join("text").attr("class","cell-label")
    .each(d=>{d.angle=(d.startAngle+d.endAngle)/2;})
    .attr("transform",d=>`rotate(${d.angle*180/Math.PI-90}) translate(${R+20}) ${d.angle>Math.PI?"rotate(180)":""}`)
    .attr("text-anchor",d=>d.angle>Math.PI?"end":null).text(d=>files[d.index]);
}

// --- 4. Tags & Topics treemap ---
function renderTags(){
  const svg = d3.select("#svg-tags");
  const [W,H] = size(svg);
  const children = [];
  Object.entries(DATA.tags).forEach(([k,v])=>children.push({name:"#"+k,value:v,kind:"tag"}));
  Object.entries(DATA.hashtags||{}).forEach(([k,v])=>children.push({name:"#"+k,value:v,kind:"hashtag"}));
  Object.entries(DATA.topics).forEach(([k,v])=>children.push({name:k,value:v,kind:"topic"}));
  if(!children.length){ svg.append("text").attr("x",20).attr("y",40).attr("fill","#8b949e").text("No tags or topics found."); return; }
  const root = d3.hierarchy({children}).sum(d=>d.value).sort((a,b)=>b.value-a.value);
  d3.treemap().size([W,H]).padding(3)(root);
  const g = svg.append("g");
  const leaf = g.selectAll("g").data(root.leaves()).join("g").attr("transform",d=>`translate(${d.x0},${d.y0})`);
  leaf.append("rect").attr("width",d=>d.x1-d.x0).attr("height",d=>d.y1-d.y0)
    .attr("fill",d=>d.data.kind==="tag"?"#3fb950":d.data.kind==="hashtag"?"#f78166":"#d29922").attr("fill-opacity",0.78).attr("rx",4)
    .on("mouseover",(e,d)=>{tip.html(`<b>${d.data.name}</b><br>${d.data.kind} · ${d.data.value} note(s)`).style("opacity",1);moveTip(e);})
    .on("click",(e,d)=>{
      const id = d.data.kind === "tag"
        ? `#tag:${String(d.data.name).replace(/^#/,"")}`
        : d.data.kind === "hashtag"
          ? `#hashtag:${String(d.data.name).replace(/^#/,"")}`
          : `#topic:${String(d.data.name).replace(/^#/,"")}`;
      if(e.ctrlKey || e.metaKey){
        openRelevantById(id);
        return;
      }
      const node = DATA.nodes.find(n=>n.id===id);
      if(node) showDetail(node);
    })
    .on("mousemove",moveTip).on("mouseout",hideTip);
  leaf.append("text").attr("x",5).attr("y",16).attr("fill","#0d1117").style("font-size","12px")
    .style("font-weight","600").text(d=>d.data.name).each(function(d){ if((d.x1-d.x0)<40) d3.select(this).remove(); });
}

// --- 5. Cluster bubbles (group by connected component) ---
function renderClusters(){
  const svg = d3.select("#svg-clusters");
  const [W,H] = size(svg);
  const groups = d3.group(DATA.nodes,d=>d.group);
  const packData = {children:[...groups].map(([gid,members])=>({
    name:"cluster "+gid, children: members.map(m=>({name:m.label,value:(m.degree||1)+1,type:m.type,d:m}))
  }))};
  const root = d3.hierarchy(packData).sum(d=>d.value);
  d3.pack().size([W,H]).padding(6)(root);
  const g = svg.append("g");
  const col = d3.scaleOrdinal(d3.schemeSet3);
  g.selectAll("circle.cl").data(root.descendants().filter(d=>d.depth===1)).join("circle")
    .attr("cx",d=>d.x).attr("cy",d=>d.y).attr("r",d=>d.r)
    .attr("fill",d=>col(d.data.name)).attr("fill-opacity",0.10).attr("stroke",d=>col(d.data.name));
  const leaf = g.selectAll("g.leaf").data(root.leaves()).join("g").attr("transform",d=>`translate(${d.x},${d.y})`);
  leaf.append("circle").attr("r",d=>d.r).attr("fill",d=>color[d.data.type])
    .on("mouseover",(e,d)=>showTip(e,d.data.d))
    .on("click",(e,d)=>{
      const node = d.data.d;
      if(e.ctrlKey || e.metaKey){
        openRelevantFile(node);
        return;
      }
      showDetail(node);
    })
    .on("mousemove",moveTip).on("mouseout",hideTip);
  leaf.append("text").attr("text-anchor","middle").attr("dy",3).style("font-size","9px").attr("fill","#0d1117")
    .text(d=>d.r>16?d.data.name:"");
}

// --- 6. Sortable node table ---
function renderTable(){
  const wrap = d3.select("#table-wrap");
  const cols = [["label","Node"],["type","Type"],["degree","Degree"],["words","Weight"],["tags","Tags"],["topics","Topics"],["summary","Summary"]];
  let rows = DATA.nodes.slice();
  const table = wrap.append("table");
  const thead = table.append("thead").append("tr");
  let sortKey="degree", asc=false;
  cols.forEach(([k,lab])=>thead.append("th").text(lab).on("click",()=>{ if(sortKey===k) asc=!asc; else {sortKey=k;asc=false;} draw(); }));
  const tbody = table.append("tbody");
  function draw(){
    rows.sort((a,b)=>{ let x=a[sortKey],y=b[sortKey];
      if(Array.isArray(x)) x=x.length; if(Array.isArray(y)) y=y.length;
      if(typeof x==="string") return asc?(""+x).localeCompare(y):(""+y).localeCompare(x);
      return asc?x-y:y-x; });
    tbody.selectAll("tr").remove();
    rows.forEach(r=>{
      const tr=tbody.append("tr");
      tr.on("click",e=>{
        if(e.ctrlKey || e.metaKey){
          openRelevantFile(r);
          return;
        }
        showDetail(r);
      });
      tr.append("td").html(`<b>${r.label}</b>`);
      tr.append("td").text(r.type);
      tr.append("td").text(r.degree||0);
      tr.append("td").text(r.words||0);
      tr.append("td").html((r.tags||[]).map(t=>`<span class="pill">#${t}</span>`).join(""));
      tr.append("td").html((r.topics||[]).map(t=>`<span class="pill">${t}</span>`).join(""));
      tr.append("td").text(r.summary||"");
    });
  }
  draw();
}

const renderers = {graph:renderGraph,matrix:renderMatrix,chord:renderChord,tags:renderTags,clusters:renderClusters,table:renderTable};

// --- Detail panel --------------------------------------------------------
function showDetail(d){
  const p = document.getElementById("detail-panel");
  document.getElementById("dp-title").textContent = d.label||d.id;
  let html = `<div class="dp-row"><b>Type:</b> ${d.type}</div>`;
  if(d.summary) html += `<div class="dp-row"><b>Summary:</b> ${d.summary}</div>`;
  if(d.path) html += `<div class="dp-row"><b>File:</b> ${d.path}</div>`;
  if(d.words) html += `<div class="dp-row"><b>Words:</b> ${d.words} &nbsp;·&nbsp; Degree: ${d.degree||0}</div>`;
  if(d.tags&&d.tags.length) html += `<div class="dp-row"><b>Tags:</b> ${d.tags.map(t=>'<span class="pill">#'+t+'</span>').join(' ')}</div>`;
  if(d.topics&&d.topics.length) html += `<div class="dp-row"><b>Topics:</b> ${d.topics.map(t=>'<span class="pill">'+t+'</span>').join(' ')}</div>`;
  if(d.headings&&d.headings.length) html += `<div class="dp-row"><b>Headings:</b><ul style="margin:4px 0;padding-left:16px">${d.headings.slice(0,10).map(h=>'<li style="color:var(--muted)">'+h+'</li>').join('')}</ul></div>`;
  document.getElementById("dp-body").innerHTML = html;
  p.style.display="block";
}
function closeDetail(){
  document.getElementById("detail-panel").style.display="none";
}
document.getElementById("dp-close").onclick = closeDetail;

function findRelatedFileNode(d){
  if(d.type === "file") return d;
  const id = d.id;
  for(const l of DATA.links){
    const s = typeof l.source === "object" ? l.source.id : l.source;
    const t = typeof l.target === "object" ? l.target.id : l.target;
    let other = null;
    if(s === id) other = t;
    if(t === id) other = s;
    if(!other) continue;
    const n = DATA.nodes.find(x => x.id === other && x.type === "file");
    if(n) return n;
  }
  return null;
}

function openRelevantById(id){
  const node = DATA.nodes.find(n=>n.id===id);
  if(node){
    openRelevantFile(node);
    return;
  }
  openRelevantFile({id, type:"topic"});
}

function openRelevantFile(d){
  const fileNode = findRelatedFileNode(d);
  if(!fileNode || !fileNode.path){
    showDetail(d);
    return;
  }
  let rel = String(fileNode.path || "").replace(/\\/g, "/").replace(/^\//, "");
  // Jekyll/GitHub Pages route convention: page path without .md extension.
  if(rel.toLowerCase().endsWith(".md")) rel = rel.slice(0, -3);
  if(!rel.startsWith(".") && !rel.startsWith("/")) rel = "./" + rel;
  window.open(encodeURI(rel), "_blank");
}
renderGraph(); rendered.graph=true;
window.addEventListener("resize",()=>{ for(const k in rendered){ d3.select("#svg-"+k).selectAll("*").remove(); if(k!=="table") renderers[k](); } });
</script>
</body>
</html>
"""


if __name__ == "__main__":
    sys.exit(main())
