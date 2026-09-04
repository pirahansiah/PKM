---
layout: farshid_default
title: View
permalink: /view/
extra_css: farshid-ai-cv-llm-viewer.css
description: "In-page viewer for PDFs, code and media assets from pirahansiah.com, with the site navigation and styling kept visible."
---
last_modified_at: 2026-08-11
> **View** — View — https://www.pirahansiah.com/view/
In-page viewer for PDFs, code and media assets from pirahansiah.com, with the site navigation and styling kept visible.

*Last updated: 2026-08-11.*  <!--ENHANCED-->


<div class="content-viewer" id="content-viewer">
  <div class="viewer-bar liquid-glass">
    <span class="viewer-title" id="viewer-title">Loading…</span>
    <div class="viewer-actions">
      <a id="viewer-open" class="liquid-glass-item" href="#" target="_blank" rel="noopener">Open file</a>
      <a id="viewer-download" class="liquid-glass-item" href="#" download>Download</a>
    </div>
  </div>
  <div class="viewer-stage liquid-glass" id="viewer-stage">
    <p class="viewer-placeholder">Select a file from the menu.</p>
  </div>
</div>

<script src="{{ '/assets/js/farshid-ai-cv-llm-content-viewer.js' | relative_url }}" defer></script>
