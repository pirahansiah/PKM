---
layout: farshid_default
title: Knowledge Graph
permalink: /graph/
extra_css: graph.css
---

<div class="graph-page">
  <div class="graph-header">
    <h1>Knowledge Graph</h1>
    <span class="graph-stats" id="graph-stats">Loading…</span>
    <div class="graph-controls">
      <a href="{{ '/graph-tags/' | relative_url }}" class="liquid-glass-item">Hashtags</a>
      <a href="{{ '/search/' | relative_url }}" class="liquid-glass-item">&#128269; Search</a>
      <a href="{{ '/' | relative_url }}" class="liquid-glass-item">Home</a>
    </div>
  </div>

  <div class="graph-search-wrap">
    <div class="graph-search-box">
      <input type="text" id="graph-search-input" placeholder="Search nodes..." oninput="graphSearch(this.value)">
      <span class="graph-search-icon">&#128269;</span>
    </div>
    <span id="graph-search-results" class="graph-search-count"></span>
  </div>

  <p class="graph-hint">Scroll to zoom · Drag to pan · Click node to open page</p>
  <div id="graph-wrap" class="liquid-glass">
    <canvas id="graph-canvas" aria-label="Interactive knowledge graph"></canvas>
  </div>
  <div class="graph-bottom-bar">
    <div class="graph-legend">
      <span class="legend-hub">Hub</span>
      <span class="legend-cv">Pages</span>
      <span class="legend-ai">Tags</span>
    </div>
  </div>
</div>

<style>
  .graph-search-wrap { max-width: 500px; margin: 8px auto; }
  .graph-search-box { position: relative; }
  .graph-search-box input {
    width: 100%; padding: 10px 36px 10px 14px; font-size: 14px;
    border: 1px solid var(--glass-border); border-radius: 10px;
    background: var(--glass-bg); color: var(--text); outline: none;
    box-sizing: border-box;
  }
  .graph-search-box input:focus { border-color: #0a84ff; }
  .graph-search-box input::placeholder { color: var(--text-muted); }
  .graph-search-icon { position: absolute; right: 12px; top: 50%; transform: translateY(-50%); color: var(--text-muted); font-size: 0.9rem; pointer-events: none; }
  .graph-search-count {
    display: block; font-size: 0.75rem; color: #0a84ff;
    margin-top: 4px; text-align: center; min-height: 1em;
  }
</style>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/fuse.js@7.0.0/dist/fuse.min.js"></script>
<script>
(function() {
  var wrap = document.getElementById("graph-wrap");
  var canvas = document.getElementById("graph-canvas");
  if (!wrap || !canvas) return;
  var ctx = canvas.getContext("2d");
  var W, H, dpr;
  var simulation;
  var gNodes = [], gLinks = [];
  var transform = { x: 0, y: 0, k: 1 };
  var hoveredNode = null, draggingNode = null;
  var tooltipEl = null;
  var gFuse = null;

  var COLORS = { hub: "#0a84ff", page: "#30d158", tag: "#af52de" };
  var isDark = matchMedia("(prefers-color-scheme:dark)").matches;
  var BG = isDark ? "#0d1117" : "#f8f9fa";
  var TEXT = isDark ? "#f5f5f7" : "#1d1d1f";
  var EDGE_COLOR = isDark ? "rgba(139,148,158,0.2)" : "rgba(100,116,139,0.15)";

  function resize() {
    dpr = window.devicePixelRatio || 1;
    W = wrap.clientWidth; H = wrap.clientHeight;
    canvas.width = W * dpr; canvas.height = H * dpr;
    canvas.style.width = W + "px"; canvas.style.height = H + "px";
  }

  function nodeR(d) { return Math.sqrt((d.connections || 0) + 1) * 2 + 3; }

  function render() {
    ctx.save(); ctx.scale(dpr, dpr);
    ctx.clearRect(0, 0, W, H); ctx.fillStyle = BG; ctx.fillRect(0, 0, W, H);
    ctx.save(); ctx.translate(transform.x, transform.y); ctx.scale(transform.k, transform.k);

    var active = hoveredNode;
    var connected = new Set();
    if (active) {
      gLinks.forEach(function(l) {
        var s = typeof l.source === "object" ? l.source : null;
        var t = typeof l.target === "object" ? l.target : null;
        if (s === active || t === active) { connected.add(s); connected.add(t); }
      });
    }

    gLinks.forEach(function(l) {
      var s = l.source, t = l.target;
      if (!s || !t || typeof s.x !== "number" || typeof t.x !== "number") return;
      var isHL = active && (s === active || t === active);
      var isDim = active && !isHL;
      ctx.beginPath(); ctx.moveTo(s.x, s.y); ctx.lineTo(t.x, t.y);
      ctx.strokeStyle = isHL ? "#0a84ff" : EDGE_COLOR;
      ctx.lineWidth = isHL ? 1.5 / transform.k : 0.5 / transform.k;
      ctx.globalAlpha = isDim ? 0.08 : isHL ? 0.8 : 0.3;
      ctx.stroke(); ctx.globalAlpha = 1;
    });

    gNodes.forEach(function(n) {
      if (typeof n.x !== "number" || typeof n.y !== "number") return;
      var r = nodeR(n);
      var isHov = hoveredNode === n;
      var isConn = active && connected.has(n);
      var isDim = active && !isHov && !isConn;
      var fill = COLORS[n.category] || "#8e8e93";

      if (isHov) {
        ctx.globalAlpha = 0.2; ctx.beginPath();
        ctx.arc(n.x, n.y, r + 8, 0, Math.PI * 2);
        ctx.fillStyle = fill; ctx.fill();
      }

      ctx.globalAlpha = isDim ? 0.08 : 1;
      ctx.beginPath(); ctx.arc(n.x, n.y, isHov ? r + 2 : r, 0, Math.PI * 2);
      ctx.fillStyle = fill; ctx.fill();
      ctx.strokeStyle = isHov ? "#0a84ff" : "rgba(255,255,255,0.15)";
      ctx.lineWidth = (isHov ? 2 : 0.4) / Math.max(transform.k, 0.5);
      ctx.stroke();

      var showLabel = isHov || isConn || (!active && transform.k > 0.6);
      if (showLabel) {
        var label = n.label || n.id;
        if (!isHov && !isConn && label.length > 20) label = label.substring(0, 18) + "…";
        ctx.globalAlpha = isDim ? 0.08 : isHov ? 1 : 0.5;
        ctx.fillStyle = isHov ? "#0a84ff" : TEXT;
        ctx.font = (isHov ? "600 " : "400 ") + Math.max(8, 10 / Math.max(transform.k, 0.5)) + "px -apple-system, system-ui, sans-serif";
        ctx.textAlign = "center";
        ctx.fillText(label, n.x, n.y + r + 10 / Math.max(transform.k, 0.5));
      }
      ctx.globalAlpha = 1;
    });
    ctx.restore(); ctx.restore();
  }

  function hitTest(px, py) {
    var mx = (px - transform.x) / transform.k;
    var my = (py - transform.y) / transform.k;
    for (var i = gNodes.length - 1; i >= 0; i--) {
      var n = gNodes[i];
      if (typeof n.x !== "number") continue;
      var dx = mx - n.x, dy = my - n.y;
      if (dx * dx + dy * dy <= (nodeR(n) + 6) * (nodeR(n) + 6)) return n;
    }
    return null;
  }

  function showTooltip(node, px, py) {
    if (!tooltipEl) { tooltipEl = document.createElement("div"); tooltipEl.className = "graph-tooltip"; wrap.appendChild(tooltipEl); }
    tooltipEl.innerHTML = '<div class="gt-title">' + (node.label || node.id) + '</div><div class="gt-cat" style="color:' + (COLORS[node.category]||'#8e8e93') + '">' + (node.category||'') + '</div>';
    tooltipEl.style.left = Math.min(px, W - 180) + "px";
    tooltipEl.style.top = (py - 50) + "px";
    tooltipEl.style.display = "block";
  }
  function hideTooltip() { if (tooltipEl) tooltipEl.style.display = "none"; }

  function setup(data) {
    var KIND_MAP = { moc: "hub", note: "page", tag: "tag" };
    gNodes = (data.nodes || []).map(function(n, i) {
      if (!n.category && n.kind) n.category = KIND_MAP[n.kind] || "page";
      if (!n.category) n.category = "page";
      n.index = i; n.connections = 0; return n;
    });

    var idSet = new Set(gNodes.map(function(n) { return n.id; }));
    gLinks = [];
    (data.links || []).forEach(function(l) {
      var s = typeof l.source === "string" ? l.source : null;
      var t = typeof l.target === "string" ? l.target : null;
      if (s && t && s !== t && idSet.has(s) && idSet.has(t)) {
        gLinks.push({ source: s, target: t, strength: l.strength || l.weight || 0.5 });
      }
    });

    gLinks.forEach(function(l) {
      var sId = typeof l.source === "object" ? l.source.id : l.source;
      var tId = typeof l.target === "object" ? l.target.id : l.target;
      gNodes.forEach(function(n) { if (n.id === sId || n.id === tId) n.connections++; });
    });

    simulation = d3.forceSimulation(gNodes)
      .force("link", d3.forceLink(gLinks).id(function(d) { return d.id; }).distance(80).strength(function(d) { return (d.strength || 0.5) * 0.4; }))
      .force("charge", d3.forceManyBody().strength(-150).distanceMax(350))
      .force("center", d3.forceCenter(W / 2, H / 2).strength(0.06))
      .force("collide", d3.forceCollide().radius(function(d) { return nodeR(d) + 3; }).strength(0.8))
      .force("x", d3.forceX(W / 2).strength(0.04))
      .force("y", d3.forceY(W / 2).strength(0.04))
      .alphaDecay(0.025)
      .on("tick", render);

    d3.select(canvas).call(d3.zoom().scaleExtent([0.1, 6]).on("zoom", function(e) { transform = e.transform; render(); }));

    d3.select(canvas).call(d3.drag()
      .on("start", function(e, d) { if (!e.active) simulation.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; draggingNode = d; })
      .on("drag", function(e, d) { var rect = wrap.getBoundingClientRect(); var p = transform.invert([e.sourceEvent.clientX - rect.left, e.sourceEvent.clientY - rect.top]); d.fx = p[0]; d.fy = p[1]; })
      .on("end", function(e, d) { if (!e.active) simulation.alphaTarget(0); d.fx = null; d.fy = null; draggingNode = null; })
    );

    d3.select(canvas)
      .on("mousemove", function(e) {
        if (draggingNode) return;
        var rect = wrap.getBoundingClientRect();
        var hit = hitTest(e.clientX - rect.left, e.clientY - rect.top);
        if (hit !== hoveredNode) {
          hoveredNode = hit;
          canvas.style.cursor = hit ? (hit.url ? "pointer" : "default") : "grab";
          if (hit) showTooltip(hit, e.clientX - rect.left, e.clientY - rect.top);
          else hideTooltip();
          render();
        }
      })
      .on("click", function(e) {
        if (draggingNode) return;
        var rect = wrap.getBoundingClientRect();
        var hit = hitTest(e.clientX - rect.left, e.clientY - rect.top);
        if (hit && hit.url) {
          window.location.href = hit.url;
        }
      });

    var stat = document.getElementById("graph-stats");
    if (stat) stat.textContent = gNodes.length + " nodes · " + gLinks.length + " connections";

    // Search
    var input = document.getElementById("graph-search-input");
    var countEl = document.getElementById("graph-search-results");
    if (input) {
      gFuse = new Fuse(gNodes.map(function(n) { return { id: n.id, title: n.label || n.id }; }), { keys: [{ name: "title", weight: 2 }], threshold: 0.4, minMatchCharLength: 2 });
      input.addEventListener("input", function() {
        var q = input.value.trim();
        if (!q || q.length < 2 || !gFuse) { render(); countEl.textContent = ""; return; }
        var results = gFuse.search(q);
        if (results.length === 0) { render(); countEl.textContent = "No matches"; return; }
        var matched = new Set();
        results.forEach(function(r) { gNodes.forEach(function(n, i) { if (n.id === r.item.id) matched.add(i); }); });
        countEl.textContent = results.length + " found";
        render();
      });
    }

    render();
  }

  resize();
  window.addEventListener("resize", function() {
    resize();
    if (simulation) {
      simulation.force("center", d3.forceCenter(W / 2, H / 2));
      simulation.force("x", d3.forceX(W / 2).strength(0.04));
      simulation.force("y", d3.forceY(H / 2).strength(0.04));
      render();
    }
  });

  fetch("{{ '/assets/graph.json' | relative_url }}")
    .then(function(r) { if (!r.ok) throw new Error("no graph"); return r.json(); })
    .then(function(data) { setup(data); })
    .catch(function(e) { console.error("Graph load error:", e); var s = document.getElementById("graph-stats"); if (s) s.textContent = "Graph data missing"; });
})();
</script>
