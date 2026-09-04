---
layout: farshid_default
title: Knowledge Graph
permalink: /graph/
extra_css: graph.css
description: "Interactive knowledge graph of pirahansiah.com — click a topic to highlight every related page, then open any page in place. Back/forward walk your trail."
---
last_modified_at: 2026-09-04
> **Knowledge Graph** — Knowledge Graph — https://pirahansiah.com/graph/
Interactive knowledge graph of pirahansiah.com — click a topic to highlight every related page, then open any page in place.

*Last updated: 2026-09-04.*  <!--ENHANCED-->


<div class="graph-page">
  <div class="graph-header">
    <h1>Knowledge Graph</h1>
    <span class="graph-stats" id="graph-stats">Loading…</span>
    <div class="graph-controls">
      <a href="{{ '/graph-tags/' | relative_url }}" class="liquid-glass-item">Hashtags</a>
      <a href="{{ '/search/' | relative_url }}" class="liquid-glass-item">&#128269; Search</a>
      <a href="{{ '/webgpu-llm/' | relative_url }}" class="liquid-glass-item">LLM</a>
      <a href="{{ '/swarm/' | relative_url }}" class="liquid-glass-item">Swarm</a>
      <a href="{{ '/' | relative_url }}" class="liquid-glass-item">Home</a>
    </div>
  </div>

  <div class="graph-search-wrap">
    <div class="graph-search-box">
      <input type="text" id="graph-search-input" placeholder="Search pages & topics..." oninput="graphSearch(this.value)">
      <span class="graph-search-icon">&#128269;</span>
    </div>
    <span id="graph-search-results" class="graph-search-count"></span>
  </div>

  <div class="graph-topics" id="graph-topics"><span class="graph-topic-more">Loading topics…</span></div>
  <div id="graph-tag-hint" class="graph-tag-hint" style="display:none"></div>

  <div id="graph-wrap" class="liquid-glass" data-graph="/assets/graph.json">
    <canvas id="graph-canvas" aria-label="Interactive knowledge graph"></canvas>
    <aside class="graph-panel" id="graph-panel">
      <div class="graph-panel-title" id="graph-panel-title">Related pages</div>
      <div class="graph-panel-list" id="graph-panel-list"></div>
    </aside>
    <div class="graph-reader" id="graph-reader"></div>
  </div>

  <div class="graph-history">
    <button type="button" class="graph-hist-btn" id="graph-back" disabled>&#8592; Back</button>
    <button type="button" class="graph-hist-btn" id="graph-forward" disabled>Forward &#8594;</button>
    <nav class="graph-crumb" id="graph-crumb"></nav>
  </div>

  <div class="graph-bottom-bar">
    <div class="graph-legend">
      <span class="legend-hub">Hubs</span>
      <span class="legend-cv">Pages</span>
      <span class="legend-ai">Topics</span>
      <span class="legend-business">Assets</span>
    </div>
  </div>
</div>

<p class="graph-hint">Click a <strong>topic chip</strong> to highlight every related page · click a <strong>page</strong> in the graph or the side panel to open it here · use <strong>Back / Forward</strong> to walk your trail · Esc clears the topic · scroll to zoom, drag to pan.</p>

<style>
  .graph-search-wrap { max-width: 620px; margin: 8px auto 0; }
  .graph-search-box { position: relative; }
  .graph-search-box input {
    width: 100%; padding: 10px 36px 10px 14px; font-size: 14px;
    border: 1px solid var(--glass-border); border-radius: 10px;
    background: var(--glass-bg); color: var(--text); outline: none; box-sizing: border-box;
  }
  .graph-search-box input:focus { border-color: #22D3EE; }
  .graph-search-box input::placeholder { color: var(--text-muted); }
  .graph-search-icon { position: absolute; right: 12px; top: 50%; transform: translateY(-50%); color: var(--text-muted); font-size: 0.9rem; pointer-events: none; }
  .graph-search-count { display: block; font-size: 0.75rem; color: #22D3EE; margin-top: 4px; text-align: center; min-height: 1em; }
</style>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/fuse.js@7.0.0/dist/fuse.min.js"></script>
<script src="{{ '/assets/js/graph-view.js' | relative_url }}" defer></script>
