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
    <div class="llm-search-wrap">
      <div class="llm-search-box">
        <input type="text" id="llm-query" placeholder="Ask anything about the site… (e.g. camera calibration)" autofocus disabled>
        <span class="llm-search-icon">&#128269;</span>
      </div>
      <button type="button" id="llm-ask-btn" class="llm-ask-btn" disabled>Ask</button>
      <button type="button" id="llm-init-btn" class="llm-ask-btn" style="background:var(--glass-bg);border:1px solid var(--glass-border);color:#0a84ff" title="Pre-download the LLM model">Load model</button>
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
      <div class="llm-progress-wrap">
        <div class="llm-progress" id="llm-progress"><div class="llm-progress-bar" id="llm-progress-bar" style="width:0%">0%</div></div>
      </div>
      <span class="llm-status-text" id="llm-status-text"></span>
    </div>

    <div class="llm-answer" id="llm-answer">
      <h2>&#128161; Answer</h2>
      <div class="llm-answer-body" id="llm-answer-body"></div>
      <div class="llm-sources" id="llm-sources"></div>
    </div>

    <div class="llm-conn" id="llm-conn">
      <h2>&#128279; Connection map</h2>
      <canvas id="llm-conn-canvas" aria-label="Related pages connection map"></canvas>
      <div class="llm-conn-hint">Top results and their neighbors from the knowledge graph — click a node to open</div>
    </div>

    <div class="llm-results-head" id="llm-results-head" style="display:none">
      <span>Relevant sections: <span class="count" id="llm-count">0</span></span>
    </div>
    <div class="llm-results" id="llm-results"></div>

    <p class="llm-hint-line" id="llm-hint-line">Runs fully in your browser: Qwen1.5-0.5B via transformers.js (WebGPU, WASM fallback) + TF-IDF retrieval over every page. First run downloads the model (a few hundred MB, cached by the browser).</p>
  </div>
</div>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="{{ '/assets/js/webgpu-llm.js' | relative_url }}"></script>
