---
layout: farshid_default
title: Knowledge Graph
permalink: /graph/
extra_css: graph.css
---

<div class="graph-page">
  <div class="graph-header">
    <h1>Knowledge Graph</h1>
    <div class="graph-controls">
      <a href="{{ '/search/' | relative_url }}" class="liquid-glass-item">&#128269; Search</a>
      <a href="{{ '/graph-tags/' | relative_url }}" class="liquid-glass-item">Hashtags</a>
      <a href="{{ '/' | relative_url }}" class="liquid-glass-item">Home</a>
    </div>
  </div>

  <iframe 
    src="{{ '/assets/knowledge_graph.html' | relative_url }}" 
    style="width:100%; height:80vh; border:none; border-radius:16px; background:#0d1117;"
    loading="lazy"
    title="Interactive Knowledge Graph"></iframe>
</div>

<style>
  .graph-page { padding: 0; }
  .graph-header {
    display: flex; align-items: center; justify-content: space-between;
    flex-wrap: wrap; gap: 12px; padding: 16px 0;
  }
  .graph-header h1 { margin: 0; font-size: 1.5rem; }
  .graph-controls { display: flex; gap: 8px; flex-wrap: wrap; }
</style>
