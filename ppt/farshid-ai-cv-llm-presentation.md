---
layout: farshid_default
title: "Reducing Token Usage in AI-Assisted Development"
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/reveal.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/theme/black.min.css">

<style>
  body { background: #000 !important; overflow: hidden !important; }
  .site-main { padding: 0 !important; margin: 0 !important; background: #000 !important; border: none !important; box-shadow: none !important; max-width: none !important; width: 100% !important; }
  .toolbar, .site-footer, footer { display: none !important; }

  .presentation-panel {
    width: 100%;
    height: calc(100vh - 80px);
    overflow: hidden;
    background: #000;
  }

  .reveal .slides section {
    height: 100%;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    align-items: center !important;
    padding: 20px !important;
    box-sizing: border-box !important;
  }

  .reveal .slides { height: 100%; }
  .reveal { height: 100%; width: 100%; }

  .reveal h1 { font-size: 2em; margin-bottom: 0.3em; color: #fff; }
  .reveal h2 { font-size: 1.4em; margin: 0.1em 0; color: #0a84ff; }
  .reveal h3 { font-size: 1em; margin: 0.1em 0; color: #bf5af2; }
  .reveal p, .reveal li { font-size: 0.65em; color: #ccc; line-height: 1.4; }
  .reveal ul { list-style: none; padding: 0; text-align: left; }
  .reveal pre { width: 90%; }
  .reveal code { font-size: 0.8em; background: rgba(255,255,255,0.1); padding: 2px 6px; border-radius: 4px; }
  .reveal .controls { color: #fff; }

  .slide-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; width: 90%; }
  .slide-card { background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.15); border-radius: 12px; padding: 16px; text-align: left; }
  .slide-card h3 { margin-top: 0; }
  .slide-metric { font-size: 2.5em; font-weight: 800; margin: 0.1em 0; }
  .slide-metric.green { color: #30d158; }
  .slide-metric.red { color: #ff375f; }
  .slide-metric.blue { color: #0a84ff; }
  .slide-metric.purple { color: #bf5af2; }
  .slide-metric.orange { color: #ff9f0a; }

  .nav-hint {
    position: absolute;
    bottom: 10px;
    font-size: 0.4em;
    opacity: 0.3;
    color: white;
    pointer-events: none;
    z-index: 10;
  }
</style>

<div class="presentation-panel">
  <div class="nav-hint">← Tap Left for Back | Tap Right for Next →</div>
  
  <div class="reveal">
    <div class="slides">

      <!-- Slide 1: Title -->
      <section>
        <h1>Reducing Token Usage</h1>
        <h2>in AI-Assisted Development</h2>
        <p>Practical strategies for .claude, .cursor, and Copilot workspaces</p>
        <p style="margin-top: 2em; color: #888;">Dr. Farshid Pirahansiah | pirahansiah.com</p>
      </section>

      <!-- Slide 2: The Problem -->
      <section>
        <h2>The Problem: Token Bloat</h2>
        <div class="slide-grid">
          <div class="slide-card" style="text-align: center;">
            <div class="slide-metric red">162 KB</div>
            <p>Full .claude folder</p>
          </div>
          <div class="slide-card" style="text-align: center;">
            <div class="slide-metric red">100%</div>
            <p>Token cost (no optimization)</p>
          </div>
          <div class="slide-card" style="text-align: center;">
            <div class="slide-metric orange">Slow</div>
            <p>Response time</p>
          </div>
          <div class="slide-card" style="text-align: center;">
            <div class="slide-metric orange">$$$</div>
            <p>API cost</p>
          </div>
        </div>
        <p style="margin-top: 1em;">1 token ≈ 4 chars • Every file = tokens per request • Irrelevant = wasted money</p>
      </section>

      <!-- Slide 3: Token Cost Breakdown -->
      <section>
        <h2>Token Cost by Component</h2>
        <table style="font-size: 0.6em; width: 90%; border-collapse: collapse;">
          <tr style="background: #0a84ff;">
            <th style="padding: 8px;">Component</th>
            <th>Size</th>
            <th>CV Project</th>
            <th>Web Project</th>
            <th>Minimal</th>
          </tr>
          <tr style="background: rgba(255,255,255,0.05);">
            <td style="padding: 6px;">Core (CLAUDE, AGENTS)</td><td>~10 KB</td><td>✅</td><td>✅</td><td>✅</td>
          </tr>
          <tr><td style="padding: 6px;">Rules (6 files)</td><td>~12 KB</td><td>5/6</td><td>1/6</td><td>❌</td></tr>
          <tr style="background: rgba(255,255,255,0.05);">
            <td style="padding: 6px;">Skills (32 files)</td><td>~90 KB</td><td>7/32</td><td>5/32</td><td>❌</td>
          </tr>
          <tr><td style="padding: 6px;">Agents (7 files)</td><td>~14 KB</td><td>4/7</td><td>2/7</td><td>❌</td></tr>
          <tr style="background: rgba(255,255,255,0.05); font-weight: bold;">
            <td style="padding: 6px;">TOTAL</td><td>~162 KB</td><td>38-45%</td><td>20-30%</td><td>6-10%</td>
          </tr>
        </table>
      </section>

      <!-- Slide 4: Strategy 1 - Templates -->
      <section>
        <h2>Strategy 1: .cursorignore Templates</h2>
        <div class="slide-grid">
          <div class="slide-card">
            <h3 style="color: #30d158;">Minimal (5-10%)</h3>
            <p>Core config only<br>No skills/agents/rules<br>Best for: Simple tasks</p>
          </div>
          <div class="slide-card">
            <h3 style="color: #0a84ff;">Web/Backend (20-30%)</h3>
            <p>Python/backend skills<br>modernize, tdd, codebase-design<br>Best for: Web apps, APIs</p>
          </div>
          <div class="slide-card">
            <h3 style="color: #bf5af2;">CV/ML (35-45%)</h3>
            <p>cv-pipeline, quantize, edge-deploy<br>data-labelling, benchmark-model<br>Best for: YOLO, SAM2, vision</p>
          </div>
          <div class="slide-card">
            <h3 style="color: #ff9f0a;">Edge/C++ (40-50%)</h3>
            <p>edge-deploy, quantize, benchmark<br>cpp-style, hardware-optimization<br>Best for: Inference, deployment</p>
          </div>
        </div>
        <p style="margin-top: 1em;"><code>copy .cursorignore.cv-project → project/.cursorignore</code></p>
      </section>

      <!-- Slide 5: Strategy 2 - Selective Loading -->
      <section>
        <h2>Strategy 2: Selective File Loading</h2>
        <div class="slide-grid">
          <div class="slide-card">
            <h3 style="color: #30d158;">✅ INCLUDE</h3>
            <ul>
              <li><code>! .claude/skills/cv-pipeline/</code></li>
              <li><code>! .claude/skills/quantize/</code></li>
              <li><code>! .claude/agents/cv-ml-expert.md</code></li>
              <li><code>! .claude/rules/python-style.md</code></li>
              <li><code>! .claude/CLAUDE.md</code></li>
            </ul>
          </div>
          <div class="slide-card">
            <h3 style="color: #ff375f;">❌ EXCLUDE</h3>
            <ul>
              <li><code>.claude/skills/modernize/</code></li>
              <li><code>.claude/skills/portfolio/</code></li>
              <li><code>.claude/agents/devops-engineer.md</code></li>
              <li><code>.claude/workflows/</code></li>
              <li><code>.claude/agent-memory/</code></li>
            </ul>
          </div>
        </div>
        <p style="margin-top: 1em; color: #30d158; font-weight: bold;">Result: 38-45% instead of 100% → Faster + Cheaper + Focused</p>
      </section>

      <!-- Slide 6: Strategy 3 - File Cleanup -->
      <section>
        <h2>Strategy 3: Remove Unnecessary Files</h2>
        <div class="slide-grid">
          <div class="slide-card">
            <h3 style="color: #ff375f;">Reference Docs</h3>
            <ul>
              <li>DIRECTORY-TREE.md</li>
              <li>FILE-INVENTORY.md</li>
              <li>SETUP-IGNORE-FILES.md</li>
              <li>PRESENTATION-BASIC-USERS.md</li>
            </ul>
          </div>
          <div class="slide-card">
            <h3 style="color: #ff9f0a;">Project Registries</h3>
            <ul>
              <li>PROJECT_PORTFOLIO_ASSETS.md (4084 lines!)</li>
              <li>PROJECT_REGISTRY.md (322 lines)</li>
              <li>MEMORY.md (session history)</li>
              <li>PERSONAL.md (git-ignored)</li>
            </ul>
          </div>
          <div class="slide-card">
            <h3 style="color: #bf5af2;">Tool-Specific</h3>
            <ul>
              <li>.cursorignore (7 variants)</li>
              <li>presentation.pptx</li>
              <li>requirements.txt (wrong project)</li>
              <li>commands/, workflows/</li>
            </ul>
          </div>
          <div class="slide-card">
            <h3 style="color: #0a84ff;">Stale Subdirs</h3>
            <ul>
              <li>myWebsite/ (duplicate)</li>
              <li>agent-memory/ (other projects)</li>
              <li>._* macOS resource forks</li>
              <li>.DS_Store files</li>
            </ul>
          </div>
        </div>
        <p style="margin-top: 1em; color: #30d158; font-weight: bold;">Real result: -4,967 lines removed | +584 lines added</p>
      </section>

      <!-- Slide 7: Before/After -->
      <section>
        <h2>Before & After: Real Example</h2>
        <div class="slide-grid">
          <div class="slide-card" style="border-color: #ff375f;">
            <h3 style="color: #ff375f;">BEFORE</h3>
            <ul>
              <li>60 files • 4 directories</li>
              <li>162+ KB total content</li>
              <li>PROJECT_PORTFOLIO_ASSETS.md: 4084 lines</li>
              <li>DIRECTORY-TREE.md: 324 lines</li>
              <li>FILE-INVENTORY.md: 280 lines</li>
              <li>7 .cursorignore variants</li>
              <li>agent-memory/ from other projects</li>
            </ul>
          </div>
          <div class="slide-card" style="border-color: #30d158;">
            <h3 style="color: #30d158;">AFTER</h3>
            <ul>
              <li>12 files • 3 directories</li>
              <li>~30 KB total content</li>
              <li>CLAUDE.md: 73 lines (focused)</li>
              <li>README.md: 17 lines (clean)</li>
              <li>rules/: 6 files (standards)</li>
              <li>skills/: 32 folders (on-demand)</li>
              <li><strong>81% file reduction • 82% size reduction</strong></li>
            </ul>
          </div>
        </div>
      </section>

      <!-- Slide 8: Results -->
      <section>
        <h2>Results: Token Reduction Impact</h2>
        <div class="slide-grid">
          <div class="slide-card" style="text-align: center;">
            <div class="slide-metric green">-81%</div>
            <p>Files Removed<br>60 → 12</p>
          </div>
          <div class="slide-card" style="text-align: center;">
            <div class="slide-metric blue">-82%</div>
            <p>Size Reduction<br>162KB → ~30KB</p>
          </div>
          <div class="slide-card" style="text-align: center;">
            <div class="slide-metric purple">-88%</div>
            <p>Line Reduction<br>785 → 90 lines</p>
          </div>
          <div class="slide-card" style="text-align: center;">
            <div class="slide-metric orange">60-95%</div>
            <p>Token Savings<br>with .cursorignore</p>
          </div>
        </div>
      </section>

      <!-- Slide 9: Best Practices -->
      <section>
        <h2>Best Practices</h2>
        <div class="slide-grid">
          <div class="slide-card">
            <h3>🎯 Project-Specific</h3>
            <p>Each project gets its own .cursorignore tailored to its tech stack</p>
          </div>
          <div class="slide-card">
            <h3>🧹 Regular Audits</h3>
            <p>Quarterly cleanup of stale memories, old logs, unused agents</p>
          </div>
          <div class="slide-card">
            <h3>📄 Minimal CLAUDE.md</h3>
            <p>Keep project brain under 100 lines. Remove anything not used weekly</p>
          </div>
          <div class="slide-card">
            <h3>🔗 Shared Templates</h3>
            <p>Store .cursorignore templates in ~/.claude/ for reuse across projects</p>
          </div>
        </div>
      </section>

      <!-- Slide 10: Codebase Memory MCP -->
      <section>
        <h2>Strategy 5: codebase-memory-mcp</h2>
        <p style="color: #bf5af2; font-weight: bold;">Stop telling Claude "read this file" • Stop grep the whole repo</p>
        <div class="slide-grid">
          <div class="slide-card">
            <h3 style="color: #30d158;">What It Does</h3>
            <ul>
              <li>Indexes entire codebase into a knowledge graph</li>
              <li>158 languages, sub-ms queries</li>
              <li>Single static binary, zero dependencies</li>
              <li>One query replaces dozens of grep/read cycles</li>
            </ul>
          </div>
          <div class="slide-card">
            <h3 style="color: #0a84ff;">Speed</h3>
            <ul>
              <li>Linux kernel (28M LOC) → 3 minutes</li>
              <li>Average repo → milliseconds</li>
              <li>Cypher query → &lt;1ms</li>
              <li>Trace call path (depth=5) → &lt;10ms</li>
            </ul>
          </div>
        </div>
        <p style="margin-top: 1em; font-size: 0.7em;"><code>curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh | bash</code></p>
      </section>

      <!-- Slide 11: Benchmark Results -->
      <section>
        <h2>Benchmarked Across 31 Real Repos</h2>
        <div class="slide-grid">
          <div class="slide-card" style="text-align: center;">
            <div class="slide-metric green">10x</div>
            <p>Fewer tokens on<br>structural queries</p>
          </div>
          <div class="slide-card" style="text-align: center;">
            <div class="slide-metric blue">83%</div>
            <p>Answer quality on<br>complex tasks</p>
          </div>
          <div class="slide-card" style="text-align: center;">
            <div class="slide-metric purple">2.1x</div>
            <p>Fewer tool calls<br>per query</p>
          </div>
          <div class="slide-card" style="text-align: center;">
            <div class="slide-metric orange">99%</div>
            <p>Token reduction<br>vs file-by-file</p>
          </div>
        </div>
        <p style="margin-top: 1em; font-size: 0.7em;">5 structural queries: ~3,400 tokens vs ~412,000 via grep/read</p>
      </section>

      <!-- Slide 12: Impact Analysis -->
      <section>
        <h2>Impact Analysis</h2>
        <div class="slide-grid">
          <div class="slide-card">
            <h3 style="color: #ff375f;">BEFORE (grep/read)</h3>
            <ul>
              <li>Read file → parse → find reference</li>
              <li>Grep repo → scan results → read files</li>
              <li>Repeat 10-20 times per question</li>
              <li>~412,000 tokens per query session</li>
              <li>Context window pollution</li>
            </ul>
          </div>
          <div class="slide-card">
            <h3 style="color: #30d158;">AFTER (codebase-memory)</h3>
            <ul>
              <li>Index once → persistent knowledge graph</li>
              <li>One graph query → all dependencies</li>
              <li>14 MCP tools: search, trace, architecture</li>
              <li>~3,400 tokens per query session</li>
              <li>Clean, focused context</li>
            </ul>
          </div>
        </div>
        <p style="margin-top: 1em; font-size: 0.7em;">github.com/DeusData/codebase-memory-mcp • 18.7k stars • MIT License</p>
      </section>

      <!-- Slide 13: Summary -->
      <section>
        <h1>Summary</h1>
        <ul style="margin-top: 1em;">
          <li>→ 5 strategies: Templates, Selective Loading, Cleanup, Combine, Graph Indexing</li>
          <li>→ File cleanup: 60 files → 12 files, 162KB → ~30KB</li>
          <li>→ .cursorignore: 60-95% token savings per project</li>
          <li>→ codebase-memory: 10x fewer tokens, 99% reduction vs grep</li>
          <li>→ Faster responses + Lower costs + Better focus</li>
        </ul>
        <p style="margin-top: 2em; color: #0a84ff;">pirahansiah.com</p>
      </section>

      <!-- End -->
      <section>
        <h1>Thank You</h1>
        <button id="restart-btn" style="background: rgba(255,255,255,0.1); color: white; border: 1px solid white; padding: 10px; border-radius: 10px; cursor: pointer;">Restart</button>
      </section>

    </div>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/reveal.js"></script>
<script>
  let deck = new Reveal(document.querySelector('.presentation-panel'), {
    embedded: true,
    hash: true,
    center: true,      
    touch: true,       
    controls: true,
    progress: true,
    width: 960,
    height: 700,
    margin: 0.1,
    minScale: 0.2,
    maxScale: 2.0
  });

  deck.initialize();

  document.getElementById('restart-btn').addEventListener('click', function(e) {
    e.stopPropagation();
    window.location.href = window.location.pathname;
  });

  document.querySelector('.presentation-panel').addEventListener('click', function(event) {
    if (event.target.closest('button, a, .controls, .progress')) return;
    const rect = this.getBoundingClientRect();
    const x = event.clientX - rect.left;
    if (x < rect.width * 0.4) {
      deck.prev();
    } else {
      deck.next();
    }
  });
</script>
