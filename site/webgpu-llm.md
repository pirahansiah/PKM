---
layout: farshid_default
title: WebGPU LLM
permalink: /webgpu-llm/
extra_css: webgpu-llm.css
---

> **WebGPU LLM** — Ask your questions across all site pages with an in-browser LLM — https://www.pirahansiah.com/webgpu-llm/

<div class="llm-page">
  <div class="llm-header">
    <h1>WebGPU LLM</h1>
    <span class="llm-stats" id="llm-stats">Loading…</span>
    <div class="llm-controls">
      <a href="{{ '/graph/' | relative_url }}" class="liquid-glass-item">Graph</a>
      <a href="{{ '/graph-tags/' | relative_url }}" class="liquid-glass-item">Hashtags</a>
      <a href="{{ '/search/' | relative_url }}" class="liquid-glass-item">&#128269; Search</a>
      <a href="{{ '/' | relative_url }}" class="liquid-glass-item">Home</a>
    </div>
  </div>

  <div class="llm-body">
    <!-- Local-only notice: user asked for this prominently at the top -->
    <div class="llm-notice" id="llm-notice">
      <div class="llm-notice-title">&#128274; 100% local &amp; private — runs in your browser</div>
      <div class="llm-notice-text">
        This page runs a small LLM <strong>entirely in your browser</strong> — no data, question, or document
        ever leaves your device. Pick a model from <strong>~15&nbsp;MB (Nano) up to ~1.5&nbsp;GB (Large)</strong>;
        each option shows its estimated total RAM (weights&nbsp;+&nbsp;KV&nbsp;cache&nbsp;+&nbsp;context). The
        <strong>Method</strong> selector chooses how it runs: <strong>Auto</strong> picks the best backend for your
        system, <strong>WebGPU</strong> uses your GPU, and <strong>WASM</strong> is the universal fallback that runs
        on any device (its SIMD&nbsp;&rarr;&nbsp;plain ladder is the modern successor to asm.js). The first load
        downloads the model once, then it's cached by the browser. <strong>All answers are English only.</strong>
        Questions run on your own hardware — no account, no tracking.
      </div>
    </div>

    <div class="llm-search-wrap">
      <div class="llm-search-box">
        <input type="text" id="llm-query" placeholder="Ask anything about the site… (e.g. camera calibration)" autofocus disabled>
        <span class="llm-search-icon">&#128269;</span>
      </div>
      <button type="button" id="llm-ask-btn" class="llm-ask-btn" disabled>Ask</button>
      <button type="button" id="llm-init-btn" class="llm-ask-btn" style="background:var(--glass-bg);border:1px solid var(--glass-border);color:#22D3EE" title="Pre-download the selected model now (the Micro default is ~90 MB)">Load model</button>
    </div>

    <div class="llm-suggest">
      Try:
      <button type="button" data-q="camera calibration">camera calibration</button>
      <button type="button" data-q="optical flow">optical flow</button>
      <button type="button" data-q="quantization">quantization</button>
      <button type="button" data-q="RAG">RAG</button>
      <button type="button" data-q="CUDA">CUDA</button>
      <button type="button" data-q="patent">patent</button>
      <button type="button" data-q="OpenCV">OpenCV</button>
    </div>

    <div class="llm-device-row">
      <span class="llm-badge" id="llm-device-badge"><span id="llm-device-text">checking GPU…</span></span>
      <label class="llm-model-pick" for="llm-model-select">
        <span>Model:</span>
        <select id="llm-model-select" title="Choose the model size — smaller downloads less, larger answers better. Each shows its estimated total RAM (weights + KV cache + context).">
          <option value="Xenova/LaMini-Flan-T5-77M">Micro — Flan-T5 77M · ~150 MB</option>
          <option value="Xenova/llama2.c-stories15M">Nano — stories 15M · ~25 MB</option>
          <option value="Xenova/llama2.c-stories42M">Pico — stories 42M · ~95 MB</option>
          <option value="Xenova/llama2.c-stories110M">Slim — stories 110M · ~230 MB</option>
          <option value="Xenova/distilgpt2">Compact — DistilGPT-2 · ~375 MB</option>
          <option value="Xenova/LaMini-GPT-124M">Tiny — LaMini 124M · ~475 MB</option>
          <option value="Xenova/Qwen1.5-0.5B-Chat">Medium — Qwen1.5 0.5B · ~1.1 GB</option>
          <option value="onnx-community/Qwen2.5-0.5B-Instruct">Balanced — Qwen2.5 0.5B · ~780 MB</option>
          <option value="onnx-community/Qwen2.5-1.5B-Instruct">Large — Qwen2.5 1.5B · ~2.4 GB</option>
        </select>
      </label>
      <label class="llm-model-pick" for="llm-device-select">
        <span>Method:</span>
        <select id="llm-device-select" title="How the model runs — Auto picks the best backend for your device; WASM runs on every browser">
          <option value="auto">Auto (best for device)</option>
          <option value="webgpu">WebGPU (GPU, fastest)</option>
          <option value="wasm">WASM (universal)</option>
        </select>
      </label>
      <div class="llm-progress-wrap">
        <div class="llm-progress" id="llm-progress"><div class="llm-progress-bar" id="llm-progress-bar" style="width:0%">0%</div></div>
      </div>
      <span class="llm-status-text" id="llm-status-text"></span>
    </div>
    <div class="llm-ram-info" id="llm-ram-info"></div>

    <!-- Answer package FIRST: review + keyword map + key points + visualizations + tags + refs + X post -->
    <div class="llm-answer" id="llm-answer">
      <h2>&#128161; Topic review</h2>
      <div class="llm-review" id="llm-review"></div>

      <div class="llm-kwmap" id="llm-kwmap" style="display:none">
        <div class="llm-kwmap-title">&#128270; Keyword map</div>
        <div class="llm-kwmap-rows" id="llm-kwmap-rows"></div>
        <div class="llm-kwmap-idea" id="llm-kwmap-idea"></div>
      </div>

      <div class="llm-keypoints" id="llm-keypoints"></div>

      <div class="llm-viz" id="llm-viz">
        <div class="llm-viz-title">&#128202; Visualizations</div>
        <div class="llm-viz-grid">
          <div class="llm-viz-panel">
            <div class="llm-viz-sub">Categories in results</div>
            <div class="llm-bars" id="llm-cat-bars"></div>
          </div>
          <div class="llm-viz-panel">
            <div class="llm-viz-sub">Top tags &amp; hashtags</div>
            <div class="llm-tagcloud" id="llm-tagcloud"></div>
          </div>
        </div>
      </div>

      <div class="llm-refs" id="llm-refs">
        <div class="llm-refs-title">&#128279; References</div>
        <ol class="llm-refs-list" id="llm-refs-list"></ol>
      </div>

      <div class="llm-web" id="llm-web">
        <div class="llm-web-title">&#127760; Find more on the web</div>
        <div class="llm-web-links" id="llm-web-links"></div>
        <div class="llm-web-hint">Opens a new tab with a search for this topic — combine with the tags above.</div>
      </div>

      <div class="llm-xpost" id="llm-xpost">
        <div class="llm-xpost-title">&#128038; Ready to post on X</div>
        <div class="llm-xpost-body" id="llm-xpost-body"></div>
        <div class="llm-xpost-actions">
          <button type="button" class="llm-ask-btn llm-copy-btn" id="llm-xpost-copy">Copy</button>
          <a class="llm-xpost-open" id="llm-xpost-open" target="_blank" rel="noopener">Open in X</a>
        </div>
      </div>

      <div class="llm-sources" id="llm-sources"></div>
    </div>

    <!-- Relevant pages / files / PDFs (instant, no model needed) -->
    <div class="llm-results-head" id="llm-results-head" style="display:none">
      <span>Relevant pages &amp; files: <span class="count" id="llm-count">0</span></span>
    </div>
    <div class="llm-results" id="llm-results"></div>

    <div class="llm-conn" id="llm-conn">
      <h2>&#128279; Connection map</h2>
      <canvas id="llm-conn-canvas" aria-label="Related pages connection map"></canvas>
      <div class="llm-conn-hint">Top results and their neighbors from the knowledge graph — click a node to open</div>
    </div>

    <!-- ============ ChatGPT-like chat section (separate div) ============ -->
    <div class="llm-chat" id="llm-chat">
      <div class="llm-chat-head">
        <h2>&#128172; Chat with your site</h2>
        <span class="llm-chat-sub">Conversational follow-ups — the model remembers this conversation. Same local &amp; private engine.</span>
      </div>
      <div class="llm-chat-log" id="llm-chat-log">
        <div class="chat-msg chat-bot">
          <div class="chat-bubble">Hi! Ask me anything about the site — papers, courses, CV, code, anything. I answer from your pages, locally in your browser. (First question may need the model to load once.)</div>
        </div>
      </div>
      <div class="llm-chat-input-row">
        <input type="text" id="llm-chat-input" placeholder="Type a message…" autocomplete="off" disabled>
        <button type="button" id="llm-chat-send" class="llm-ask-btn" disabled>Send</button>
      </div>
      <div class="llm-chat-status" id="llm-chat-status"></div>
    </div>

    <p class="llm-hint-line" id="llm-hint-line">Runs fully in your browser: 9 models from ~15 MB (Nano) to ~1.5 GB (Large) with per-model RAM estimates (weights + KV cache + context), via transformers.js. Method: Auto / WebGPU / WASM — WASM runs on every device (the modern asm.js-style universal fallback). All answers are English only. BM25 retrieval over every page; first run downloads the model (cached).</p>
  </div>
</div>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="{{ '/assets/js/llm-search.js?v=15' | relative_url }}"></script>
