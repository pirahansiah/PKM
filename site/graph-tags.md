---
layout: farshid_default
title: Hashtag Graph
permalink: /graph-tags/
extra_css: graph.css
description: "Hashtag knowledge graph of pirahansiah.com — click a topic to see which other topics and pages cluster around it."
---
last_modified_at: 2026-09-04
> **Hashtag Graph** — Hashtag Graph — https://pirahansiah.com/graph-tags/
Hashtag knowledge graph of pirahansiah.com — click a topic to see which other topics and pages cluster around it.

*Last updated: 2026-09-04.*  <!--ENHANCED-->


<div class="graph-page">
  <div class="graph-header">
    <h1>Hashtag Graph</h1>
    <span class="graph-stats" id="graph-stats">Loading…</span>
    <div class="graph-controls">
      <button type="button" id="graph-freeze" class="liquid-glass-item">Freeze</button>
      <button type="button" id="graph-reset" class="liquid-glass-item">Reset</button>
      <a href="{{ '/graph/' | relative_url }}" class="liquid-glass-item">Full Graph</a>
      <a href="{{ '/' | relative_url }}" class="liquid-glass-item">Home</a>
    </div>
  </div>

  <div class="graph-topics" id="graph-topics"><span class="graph-topic-more">Loading topics…</span></div>
  <div id="graph-tag-hint" class="graph-tag-hint" style="display:none"></div>

  <div id="graph-wrap" class="liquid-glass" data-graph="/assets/graph-hashtags.json">
    <canvas id="graph-canvas" aria-label="Interactive hashtag graph"></canvas>
    <aside class="graph-panel" id="graph-panel">
      <div class="graph-panel-title" id="graph-panel-title">Related</div>
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
      <span class="legend-ai">Topics</span>
      <span class="legend-cv">Pages</span>
    </div>
  </div>
</div>

<p class="graph-hint">Click a <strong>topic</strong> to highlight its cluster · double-click any related topic/page to dive deeper · use <strong>Back / Forward</strong> to walk your trail · Esc clears the focus.</p>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/fuse.js@7.0.0/dist/fuse.min.js"></script>
<script src="{{ '/assets/js/graph-view.js' | relative_url }}" defer></script>
