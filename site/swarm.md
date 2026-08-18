---
layout: farshid_default
title: Agent Swarm
permalink: /swarm/
extra_css: swarm.css
---

> **Agent Swarm** — Ask a question; a swarm of AI agents explores the whole site — papers, journals, books, patents, keynotes, courses, wiki, CV — and answers with a dynamic knowledge graph — https://www.pirahansiah.com/swarm/

<div class="swarm-page">
  <div class="swarm-header">
    <h1>Agent Swarm</h1>
    <span class="swarm-stats" id="swarm-stat">Loading…</span>
    <div class="swarm-controls">
      <a href="{{ '/graph/' | relative_url }}" class="liquid-glass-item">Graph</a>
      <a href="{{ '/graph-tags/' | relative_url }}" class="liquid-glass-item">Hashtags</a>
      <a href="{{ '/search/' | relative_url }}" class="liquid-glass-item">&#128269; Search</a>
      <a href="{{ '/webgpu-llm/' | relative_url }}" class="liquid-glass-item">LLM</a>
      <a href="{{ '/' | relative_url }}" class="liquid-glass-item">Home</a>
    </div>
  </div>

  <div class="swarm-query-row">
    <div class="swarm-search-box">
      <input type="text" id="swarm-query" placeholder="Ask the swarm anything… e.g. camera calibration, optical flow, multi-agent LLMs, patents, OpenCV 5"
             autocomplete="off" disabled>
      <span class="swarm-search-icon">&#128269;</span>
    </div>
    <button type="button" id="swarm-ask" class="swarm-ask-btn" disabled>Launch swarm</button>
  </div>

  <div class="swarm-suggest" id="swarm-suggest">
    Try:
    <button type="button" data-q="camera calibration">camera calibration</button>
    <button type="button" data-q="optical flow">optical flow</button>
    <button type="button" data-q="multi-camera">multi-camera</button>
    <button type="button" data-q="quantization">quantization</button>
    <button type="button" data-q="RAG">RAG</button>
    <button type="button" data-q="patent">patent</button>
    <button type="button" data-q="OpenCV">OpenCV</button>
    <button type="button" data-q="ROS">ROS</button>
  </div>

  <div id="swarm-loading" class="swarm-loading" style="display:none">
    <span class="swarm-loading-spinner"></span> Indexing the site…
  </div>

  <div id="swarm-notice" class="swarm-notice" style="display:none"></div>

  <div id="swarm-wrap" class="liquid-glass swarm-wrap">
    <canvas id="swarm-canvas" aria-label="Agent swarm animation"></canvas>
  </div>
  <p class="swarm-hint">Watch the swarm: each node is an agent with its own specialty — text retrieval, graph mapping, tag mining, categorization, relation weaving, synthesis.</p>

  <div class="swarm-log" id="swarm-console" aria-live="polite"></div>

  <div class="swarm-section">
    <h2>&#128161; Swarm synthesis</h2>
    <div id="swarm-synthesis" class="swarm-synthesis"></div>
    <div class="swarm-sub">
      <h3>&#128221; Key points</h3>
      <div id="swarm-keypoints" class="swarm-keypoints"></div>
    </div>
    <div class="swarm-chips-row">
      <span class="swarm-chips-label">Coverage:</span>
      <div id="swarm-covered" class="swarm-covered"></div>
    </div>
  </div>

  <div class="swarm-section">
    <h2>&#128202; Knowledge understanding</h2>
    <div class="swarm-viz-grid">
      <div class="swarm-viz-panel">
        <div class="swarm-viz-sub">Categories covered</div>
        <div id="swarm-cat-bars" class="swarm-cat-bars"></div>
      </div>
      <div class="swarm-viz-panel">
        <div class="swarm-viz-sub">Top tags</div>
        <div id="swarm-tagcloud" class="swarm-tagcloud"></div>
      </div>
    </div>
  </div>

  <div class="swarm-section">
    <h2>&#128279; Related pages</h2>
    <div id="swarm-refs" class="swarm-refs"></div>
  </div>

  <div class="swarm-section">
    <h2>&#128517; Relations between findings</h2>
    <div id="swarm-relations" class="swarm-relations"></div>
  </div>

  <div class="swarm-section swarm-graph-section" id="swarm-graph" style="display:none">
    <h2>&#128506; Dynamic knowledge graph for your question</h2>
    <div id="swarm-graph-wrap" class="swarm-graph-wrap liquid-glass">
      <canvas id="swarm-graph-canvas" aria-label="Query-specific knowledge graph"></canvas>
    </div>
    <p class="swarm-hint">Built live from the swarm's findings — blue = pages &amp; publications, purple = tags, grey = categories. Click a node to open.</p>
  </div>

  <div class="swarm-section">
    <h2>&#128038; Ready to post on X</h2>
    <div class="swarm-xpost">
      <div class="swarm-xpost-body" id="swarm-xpost-body"></div>
      <div class="swarm-xpost-actions">
        <button type="button" class="swarm-ask-btn" id="swarm-xpost-copy">Copy</button>
        <a class="swarm-xpost-open" id="swarm-xpost-open" target="_blank" rel="noopener">Open in X</a>
      </div>
    </div>
  </div>

  <p class="swarm-hint-line">100% in-browser: the swarm reads the site index and knowledge graph locally — no server, no account, no tracking. The same engine powers the <a href="{{ '/webgpu-llm/' | relative_url }}">WebGPU LLM</a> page when you want generative answers.</p>
</div>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="{{ '/assets/js/swarm.js?v=1' | relative_url }}"></script>