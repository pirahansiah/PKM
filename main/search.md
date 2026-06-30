---
layout: farshid_default
title: Search
permalink: /search/
---

<style>
  .search-wrap { max-width: 700px; margin: 0 auto; padding: 0 16px; }
  .search-hero { text-align: center; padding: 40px 0 24px; }
  .search-hero h1 { font-size: 1.8rem; color: var(--text); margin-bottom: 4px; }
  .search-hero p { color: var(--text-muted); font-size: 0.9rem; }
  .search-box { position: relative; margin-bottom: 8px; }
  .search-box input {
    width: 100%; padding: 14px 48px 14px 18px; font-size: 16px;
    border: 1px solid var(--glass-border); border-radius: 12px;
    background: var(--glass-bg); color: var(--text); outline: none;
    box-sizing: border-box; transition: border-color 0.2s;
  }
  .search-box input:focus { border-color: #0a84ff; }
  .search-box input::placeholder { color: var(--text-muted); }
  .search-box .search-icon { position: absolute; right: 16px; top: 50%; transform: translateY(-50%); color: var(--text-muted); font-size: 1.1rem; pointer-events: none; }
  .search-meta { display: flex; gap: 12px; align-items: center; flex-wrap: wrap; margin-bottom: 20px; }
  .search-meta label { font-size: 0.8rem; color: var(--text-muted); cursor: pointer; display: flex; align-items: center; gap: 4px; }
  .search-meta input[type="checkbox"] { accent-color: #0a84ff; }
  .search-tags { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 20px; }
  .search-tag {
    padding: 4px 10px; font-size: 0.75rem; border-radius: 6px; cursor: pointer;
    background: var(--glass-bg); border: 1px solid var(--glass-border); color: var(--text-muted);
    transition: all 0.2s;
  }
  .search-tag:hover, .search-tag.active { background: rgba(10,132,255,0.15); border-color: #0a84ff; color: #0a84ff; }
  .search-results { list-style: none; padding: 0; margin: 0; }
  .search-result {
    padding: 14px 16px; border-radius: 10px; margin-bottom: 8px;
    background: var(--glass-bg); border: 1px solid var(--glass-border);
    transition: transform 0.15s, border-color 0.2s;
  }
  .search-result:hover { transform: translateX(4px); border-color: #0a84ff; }
  .search-result a { text-decoration: none; color: var(--text); }
  .search-result-title { font-weight: 600; font-size: 0.95rem; margin-bottom: 4px; }
  .search-result-url { font-size: 0.75rem; color: #0a84ff; margin-bottom: 4px; word-break: break-all; }
  .search-result-body { font-size: 0.82rem; color: var(--text-muted); line-height: 1.4; }
  .search-result-body mark { background: rgba(10,132,255,0.25); color: var(--text); border-radius: 2px; padding: 0 2px; }
  .search-result-score { font-size: 0.7rem; color: var(--text-muted); margin-top: 4px; }
  .search-count { font-size: 0.8rem; color: var(--text-muted); margin-bottom: 12px; }
  .search-empty { text-align: center; padding: 40px 0; color: var(--text-muted); }
  .search-google { text-align: center; margin-top: 20px; padding: 16px; background: var(--glass-bg); border-radius: 10px; border: 1px solid var(--glass-border); }
  .search-google a { color: #0a84ff; text-decoration: none; font-size: 0.9rem; }
  .search-google a:hover { text-decoration: underline; }
  .search-google p { font-size: 0.75rem; color: var(--text-muted); margin-top: 4px; }
  @media (max-width: 480px) { .search-hero h1 { font-size: 1.4rem; } }
</style>

<div class="search-wrap">
  <div class="search-hero">
    <h1>Search</h1>
    <p>Fuzzy + content-based search across all content pages</p>
  </div>

  <div class="search-box">
    <input type="text" id="q" placeholder="Search pages, papers, code, topics..." autofocus oninput="doSearch()">
    <span class="search-icon">&#128269;</span>
  </div>

  <div class="search-meta">
    <label><input type="checkbox" id="opt-title" checked onchange="doSearch()"> Title</label>
    <label><input type="checkbox" id="opt-body" checked onchange="doSearch()"> Content</label>
    <label><input type="checkbox" id="opt-fuzzy" checked onchange="doSearch()"> Fuzzy</label>
  </div>

  <div class="search-tags">
    <span class="search-tag" onclick="quickSearch('computer vision')">Computer Vision</span>
    <span class="search-tag" onclick="quickSearch('YOLO')">YOLO</span>
    <span class="search-tag" onclick="quickSearch('OpenCV')">OpenCV</span>
    <span class="search-tag" onclick="quickSearch('LLM')">LLM</span>
    <span class="search-tag" onclick="quickSearch('CUDA')">CUDA</span>
    <span class="search-tag" onclick="quickSearch('patent')">Patent</span>
    <span class="search-tag" onclick="quickSearch('quantization')">Quantization</span>
    <span class="search-tag" onclick="quickSearch('edge AI')">Edge AI</span>
  </div>

  <div id="search-count" class="search-count"></div>
  <ul id="search-results" class="search-results"></ul>

  <div id="search-google" class="search-google" style="display:none;">
    <a id="google-link" href="#" target="_blank">Search on Google (site:pirahansiah.com)</a>
    <p>Powered by Google — for results not found locally</p>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/fuse.js@7.0.0/dist/fuse.min.js"></script>
<script>
var CONTENT_INDEX = [];
var fuse = null;
var fuseStrict = null;

function initSearch(data) {
  CONTENT_INDEX = data;
  fuse = new Fuse(data, {
    keys: [
      { name: 'title', weight: 0.4 },
      { name: 'tags', weight: 0.3 },
      { name: 'body', weight: 0.1 },
      { name: 'category', weight: 0.2 }
    ],
    threshold: 0.35,
    distance: 200,
    includeMatches: true,
    minMatchCharLength: 2
  });
  fuseStrict = new Fuse(data, {
    keys: [{ name: 'title', weight: 0.6 }, { name: 'tags', weight: 0.3 }],
    threshold: 0.25,
    distance: 100,
    includeMatches: true,
    minMatchCharLength: 2
  });
}

function doSearch() {
  var q = document.getElementById('q').value.trim();
  var resultsEl = document.getElementById('search-results');
  var countEl = document.getElementById('search-count');
  var googleEl = document.getElementById('search-google');
  var optFuzzy = document.getElementById('opt-fuzzy').checked;

  if (!q || !fuse) {
    resultsEl.innerHTML = '';
    countEl.textContent = '';
    googleEl.style.display = 'none';
    return;
  }

  var engine = optFuzzy ? fuse : fuseStrict;
  var results = engine.search(q);

  countEl.textContent = results.length + ' result' + (results.length !== 1 ? 's' : '') + ' for "' + q + '"';

  if (results.length === 0) {
    resultsEl.innerHTML = '<div class="search-empty">No results found locally.</div>';
    googleEl.style.display = 'block';
    document.getElementById('google-link').href = 'https://www.google.com/search?q=site:pirahansiah.com+' + encodeURIComponent(q);
    return;
  }

  googleEl.style.display = 'block';
  document.getElementById('google-link').href = 'https://www.google.com/search?q=site:pirahansiah.com+' + encodeURIComponent(q);

  var html = '';
  results.forEach(function(r) {
    var item = r.item || r;
    var score = r.score ? Math.round((1 - r.score) * 100) : 100;
    var snippet = item.body || '';
    if (snippet.length > 160) snippet = snippet.substring(0, 160) + '...';

    if (r.matches) {
      r.matches.forEach(function(m) {
        if (m.key === 'body' && m.indices && m.indices.length > 0) {
          var start = Math.max(0, m.indices[0][0] - 40);
          var end = Math.min(item.body.length, m.indices[0][1] + 60);
          snippet = (start > 0 ? '...' : '') + item.body.substring(start, end) + (end < item.body.length ? '...' : '');
        }
      });
    }

    html += '<li class="search-result">' +
      '<a href="' + item.url + '">' +
      '<div class="search-result-title">' + item.title + '</div>' +
      '<div class="search-result-url">' + item.url + '</div>' +
      '<div class="search-result-body">' + snippet + '</div>' +
      '<div class="search-result-score">' + score + '% match</div>' +
      '</a></li>';
  });

  resultsEl.innerHTML = html;
}

function quickSearch(term) {
  document.getElementById('q').value = term;
  doSearch();
  document.getElementById('q').focus();
}

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('q').addEventListener('keydown', function(e) {
    if (e.key === 'Enter') { e.preventDefault(); doSearch(); }
  });
  fetch('/assets/search-index.json')
    .then(function(r) { return r.json(); })
    .then(function(data) { initSearch(data); })
    .catch(function() { console.log('Search index not ready'); });
});
</script>
