---
layout: farshid_default
title: "Local LLM Optimization on Apple Silicon"
description: "Run the fastest small reasoning model inside Hermes Agent at 64K context on Apple M3 (16GB) using MLX (CPU+GPU+NPU), with oMLX, llama.cpp, and Ollama paths plus downloadable scripts."
tags: [ai, llm, apple-silicon, mlx, optimization, hermes]
hashtags: "#ai #llm #applesilicon #mlx #optimization #hermes"
markmap: |
  # Local LLM Optimization on Apple Silicon
  ## Backends
  - oMLX (MLX: CPU+GPU+NPU)
  - llama.cpp (Metal: CPU+GPU)
  - Ollama (disabled here)
  ## Key Wins
  - 64K context
  - Continuous batching
  - Tiered / paged KV cache
  - Thinking suppression
  ## Persistence
  - launchd daemon
  - Survives reboot/logout
  ## Files
  - OPTIMIZATION.md
  - prompts.md
  - optimize_local_llm.sh
---

last_modified_at: 2026-09-05
> **Local LLM Optimization on Apple Silicon** — Run the fastest small reasoning model inside Hermes Agent at 64K context on Apple M3 (16GB) using MLX. — https://www.pirahansiah.com/notes/docs/llm/local-llm-optimization/

# Local LLM Optimization on Apple Silicon (M3, 16GB)

Target machine (verified live): **Apple M3, 16GB, macOS 27**. Goal: run the **fastest small reasoning model** inside **Hermes Agent** with **64K context**, using the latest Apple-native acceleration (CPU + GPU + NPU via **MLX**).

*Last updated: 2026-09-05.*  <!--ENHANCED-->

## Current live state (this machine, Sep 5 2026)

- **Hermes → oMLX (port 8000)**. Default model `Qwen3.5-4B-OptiQ-4bit` (since Sep 5 2026); `Qwen3.5-0.8B-OptiQ-4bit` also served (fallback / small-quick). Both MLX safetensors, 64K context via the `q35` custom provider.
- **Ollama is up but unused by Hermes**: `ollama serve` runs on :11434 but Hermes's `base_url` points at oMLX on :8000.
- **Hermes gateway runs as a headless daemon** (launchd `ai.hermes.gateway`). Telegram bot works with no terminal open.
- **oMLX auto-starts via launchd**: `com.farshid.omlx-serve.plist` (RunAtLoad + KeepAlive) holds :8000 across reboots/logout.

## Bottom line (measured on this M3)

| Path | Status | Model | Speed | Verdict |
|---|---|---|---|---|
| **oMLX (MLX) — port 8000** | **ACTIVE** | `Qwen3.5-4B-OptiQ-4bit` default (0.8B also served) | 4B ≈ 40 tok/s, 0.8B ≈ 79–98 tok/s | Max-native CPU+GPU+ANE, continuous batching, paged tiered KV cache |
| Ollama MLX — port 11434 | **disabled** | `qwen3.5:0.8b-mlx` | 75 tok/s | Works but contrives reasoning handling; no per-request thinking toggle |
| llama.cpp (Metal) — port 8080 | fallback only | `Qwen3.5-0.8B-Q4_K_M.gguf` | 67–78 tok/s | No NPU; reasoning + jinja quirks |

> **Key insight: Qwen3/3.5 are reasoning models.** Out of the box they burn the whole prompt budget on `thinking` and return an **empty final message** if you don't give them room or suppress thinking. oMLX makes thinking suppression trivial via `chat_template_kwargs`.

## What "all processors" means on Apple Silicon

- **MLX** (`mlx-lm`): schedules on **CPU + GPU + ANE (Neural Engine)**.
- **llama.cpp** with Metal: **CPU + GPU only**, no NPU.
- **oMLX** is built on `mlx-lm` → full MLX device coverage (CPU + GPU + NPU).

If you specifically need NPU: use the MLX/oMLX path. llama.cpp cannot touch the Neural Engine.

## Install oMLX (macOS app; precompiled kernels included)

```bash
# Recommended: official DMG (ships precompiled MLX custom kernels, no Xcode build)
curl -L -o /tmp/oMLX.dmg \
  "https://github.com/jundot/omlx/releases/download/v0.6.4/oMLX-0.6.4-macos26-27.dmg"
hdiutil attach /tmp/oMLX.dmg -nobrowse
cp -R /Volumes/oMLX/oMLX.app /Applications/
hdiutil detach /Volumes/oMLX
```

CLI entry points:
```bash
/Applications/oMLX.app/Contents/MacOS/omlx-cli        # CLI
/Applications/oMLX.app/Contents/Resources              # bundled Python + MLX
```

## Serve a model with oMLX (64K context, continuous batching, paged KV cache)

```bash
omlx-cli start
# Or run the CLI server directly:
/Applications/oMLX.app/Contents/MacOS/omlx-cli serve \
  --model-dir ~/.omlx/models \
  --port 8000 --host 127.0.0.1 \
  --log-level info
```

oMLX enables the optimization stack **by default**: continuous batching, tiered/paged KV cache (hot RAM + cold SSD), LRU multi-model memory + memory guard, prefix sharing + Copy-on-Write blocks.

## Suppress thinking (why many Qwen3.5 results come back empty)

Per-request, in the OpenAI-compatible body:
```json
{ "model": "Qwen3.5-0.8B-OptiQ-4bit",
  "messages": [...],
  "max_tokens": 256,
  "chat_template_kwargs": { "enable_thinking": false } }
```

## Hermes integration

Edit `~/.hermes/config.yaml`:
```yaml
model:
  default: Qwen3.5-4B-OptiQ-4bit
  provider: custom
  base_url: http://127.0.0.1:8000/v1   # was http://127.0.0.1:11434/v1 (Ollama)
```
Then restart the gateway: `hermes gateway restart`. Verify: `hermes status` → Model `Qwen3.5-4B-OptiQ-4bit`, Provider "Custom endpoint".

## Alternate path — llama.cpp (Metal) full optimization

```bash
llama-server -m /path/Qwen3.5-0.8B-Q4_K_M.gguf \
  -c 65536 -ngl 99 -fa on -ctk q8_0 -ctv q8_0 \
  -b 1024 -ub 1024 --cache-reuse 256 -t 8 \
  --alias qwen3.5-0.8b-q4 \
  --port 8080 --host 127.0.0.1
```
- `-ngl 99` = all layers on GPU (Metal device `MTL0: Apple M3`, 12GB)
- `-fa on` = flash attention
- `-ctk q8_0 -ctv q8_0` = quantized KV cache → biggest long-context memory win

## Persistence — launchd daemon (survives reboot / logout, no terminal needed)

`~/Library/LaunchAgents/com.farshid.omlx-serve.plist` — `RunAtLoad` + `KeepAlive`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.farshid.omlx-serve</string>
    <key>ProgramArguments</key>
    <array>
        <string>/opt/homebrew/bin/omlx</string>
        <string>serve</string>
        <string>--model-dir</string>
        <string>/Users/farshid/.omlx/models</string>
        <string>--host</string>
        <string>127.0.0.1</string>
        <string>--port</string>
        <string>8000</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>
```
Install/load:
```bash
launchctl load -w ~/Library/LaunchAgents/com.farshid.omlx-serve.plist
launchctl list | grep omlx
curl -s http://127.0.0.1:8000/v1/models
```

## RAM math (16GB unified)

- 0.8B MLX OptiQ-4bit ≈ **0.7 GB** weights + KV (oMLX server ~1.2 GB RSS)
- 4B MLX OptiQ-4bit ≈ **3 GB** (KV grows; keep 64K but watch total)
- llama.cpp 1.7B Q8 ≈ 1.8–2.2 GB at 64K with quantized KV

Never let context default to a model's full 262K on 16GB (pre-set KV eats RAM you don't have).

## Download the files

All three source files are available for download — the full guide, the prompt/keyword bank, and the auto-detect startup script.

<div class="downloads-section">
  <div class="download-card">
    <div class="file-item">
      <div class="file-info">
        <div class="file-name">OPTIMIZATION.md</div>
        <div class="file-desc">Complete optimization guide: install, serve, suppress thinking, Hermes config, llama.cpp path, launchd persistence, RAM math (11.7 KB)</div>
      </div>
      <div class="file-action"><a href="/assets/downloads/OPTIMIZATION.md" target="_blank" class="btn btn-primary">Download</a></div>
    </div>
    <div class="file-item">
      <div class="file-info">
        <div class="file-name">prompts.md</div>
        <div class="file-desc">Reusable benchmark + optimization prompt templates and keyword bank (3.6 KB)</div>
      </div>
      <div class="file-action"><a href="/assets/downloads/prompts.md" target="_blank" class="btn btn-primary">Download</a></div>
    </div>
    <div class="file-item">
      <div class="file-info">
        <div class="file-name">optimize_local_llm.sh</div>
        <div class="file-desc">Auto-detect best backend (oMLX → llama.cpp → Ollama) and serve at 64K context; optional --persist launchd agent (7.4 KB)</div>
      </div>
      <div class="file-action"><a href="/assets/downloads/optimize_local_llm.sh" target="_blank" class="btn btn-primary">Download</a></div>
    </div>
  </div>
  <div class="download-all">
    <a href="/assets/downloads/local-llm-optimization-20260905.zip" target="_blank" class="btn btn-secondary">Download All 3 Files (ZIP)</a>
  </div>
</div>

<style>
  .downloads-section { padding: 1.5rem 0; }
  .download-card { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin-bottom: 1.25rem; }
  .file-item { display: flex; align-items: center; justify-content: space-between; gap: 1rem; padding: 1.1rem 1.25rem; background: var(--card); border: 1px solid var(--border); border-radius: 10px; }
  .file-info { flex: 1; }
  .file-name { font-weight: 600; font-size: 1.02rem; margin-bottom: 0.2rem; }
  .file-desc { font-size: 0.88rem; color: var(--muted-foreground); line-height: 1.45; }
  .btn { padding: 0.55rem 1.1rem; border-radius: 7px; font-weight: 500; text-decoration: none; display: inline-block; white-space: nowrap; }
  .btn-primary { background: var(--accent); color: var(--foreground); }
  .btn-primary:hover { background: var(--accent-strong); }
  .btn-secondary { background: transparent; border: 1px solid var(--border); color: var(--foreground); }
  .btn-secondary:hover { background: var(--muted); }
</style>
