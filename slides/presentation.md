---
layout: farshid_default
title: "Hermes Agent for Research Assistance — Comprehensive Presentation"
tags:
  - presentation
  - research
  - hermes-agent
  - ai
  - llm
hashtags: "#presentation #research #hermes-agent #ai #llm"
description: "Comprehensive presentation deck: Using Hermes Agent for university research, literature review, code reproduction, experimentation, and paper writing."
---
last_modified_at: 2026-09-06
> **Hermes Agent for Research Assistance** — Autonomous AI Research Partner for Academia & Engineering — https://www.pirahansiah.com/notes/slides/presentation/
> Presentation: Comprehensive setup, configurations, workflow automation, ArXiv integration, and multi-agent execution for researchers.

*Last updated: 2026-09-06.*

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/reveal.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/theme/black.min.css">

<style>
  body { background: #000 !important; overflow: hidden !important; }
  .site-main { padding: 0 !important; margin: 0 !important; background: #000 !important; border: none !important; box-shadow: none !important; max-width: none !important; width: 100% !important; }
  .toolbar, .site-footer, footer { display: none !important; }
  .presentation-panel { width: 100%; height: calc(100vh - 80px); overflow: hidden; background: #050b14; }
  .reveal .slides section { height: 100%; display: flex !important; flex-direction: column !important; justify-content: center !important; align-items: center !important; padding: 20px !important; box-sizing: border-box !important; }
  .reveal .slides { height: 100%; }
  .reveal { height: 100%; width: 100%; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
  .reveal h1 { font-size: 2.0em; margin-bottom: 0.2em; color: #fff; text-align: center; font-weight: 800; background: linear-gradient(135deg, #22D3EE, #06B6D4, #3B82F6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
  .reveal h2 { font-size: 1.35em; margin: 0.2em 0 0.5em; color: #22D3EE; text-align: center; font-weight: 700; }
  .reveal h3 { font-size: 1.1em; color: #A855F7; margin: 0.2em 0; }
  .reveal p, .reveal li { font-size: 0.85em; color: #cbd5e1; line-height: 1.5; }
  .reveal ul { list-style: none; padding: 0; text-align: left; margin: 0.5em 0; }
  .reveal .controls { color: #22D3EE; }
  .reveal .progress { color: #22D3EE; height: 4px; }
  
  /* Grid & Card layout */
  .m { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; width: 98%; max-width: 1100px; margin: 0.5em auto; }
  .m-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; width: 98%; max-width: 1100px; margin: 0.5em auto; }
  .m-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; width: 98%; max-width: 1100px; margin: 0.5em auto; }
  
  .c { background: rgba(15, 23, 42, 0.75); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 12px; padding: 16px; text-align: center; backdrop-filter: blur(12px); box-shadow: 0 8px 32px rgba(0,0,0,0.37); }
  .c-left { text-align: left; }
  .c p { text-align: left; margin: 6px 0; font-size: 0.82em; }
  
  /* Big Metric Numbers */
  .n { font-size: 2.2em; font-weight: 800; margin: 0; line-height: 1.1; }
  .n.g { color: #30d158; } 
  .n.r { color: #0284C7; } 
  .n.b { color: #22D3EE; } 
  .n.p { color: #A855F7; } 
  .n.o { color: #ff9f0a; }
  
  /* Code blocks */
  .code-box { background: #090d16; border: 1px solid rgba(34,211,238,0.3); border-radius: 8px; padding: 12px 16px; font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace; font-size: 0.75em; color: #38bdf8; text-align: left; width: 95%; max-width: 1000px; overflow-x: auto; box-shadow: inset 0 2px 8px rgba(0,0,0,0.6); }
  .code-box pre { margin: 0; padding: 0; }
  .code-box .cmd { color: #34d399; font-weight: bold; }
  .code-box .cmt { color: #64748b; italic; }
  .code-box .str { color: #fbbf24; }
  .code-box .kw { color: #f472b6; font-weight: bold; }
  
  .tag { display: inline-block; background: rgba(34, 211, 238, 0.15); border: 1px solid rgba(34, 211, 238, 0.4); color: #38bdf8; padding: 2px 8px; border-radius: 6px; font-size: 0.75em; font-weight: 600; margin-right: 4px; }
  
  .nav-hint { position: absolute; bottom: 8px; font-size: 0.55em; opacity: 0.4; color: #94a3b8; pointer-events: none; z-index: 10; }
  
  @media (max-width: 768px) { 
    .m, .m-2, .m-3 { grid-template-columns: 1fr; } 
    .n { font-size: 1.6em; } 
    .reveal h1 { font-size: 1.4em; } 
    .reveal h2 { font-size: 1.1em; } 
    .code-box { font-size: 0.65em; }
  }
</style>

<div class="presentation-panel">
  <div class="nav-hint">← Tap Left / Press Left Arrow | Tap Right / Press Right Arrow →</div>
  <div class="reveal">
    <div class="slides">

      <!-- Slide 1: Title Slide -->
      <section>
        <span class="tag">UNIVERSITY LECTURE & RESEARCH SEMINAR</span>
        <h1>Hermes Agent for Research Assistance</h1>
        <h2>Autonomous Workflows, Literature Sweeps, Code Execution & Paper Drafting</h2>
        <p style="color:#94a3b8; margin-top:1.2em; font-size: 0.95em;">
          <strong>Dr. Farshid Pirahansiah</strong><br>
          <span style="color:#38bdf8;">AI & Computer Vision Engineer • pirahansiah.com</span>
        </p>
      </section>

      <!-- Slide 2: Executive Summary / Motivation -->
      <section>
        <h2>Why Hermes Agent for Researchers?</h2>
        <div class="m-2">
          <div class="c c-left">
            <h3 style="color:#f87171;">⚠️ Academic Research Pain Points</h3>
            <p>• <strong>10,000+ papers/year</strong> per field (ArXiv overload).</p>
            <p>• <strong>Manual literature synthesis</strong> & BibTeX management.</p>
            <p>• <strong>Broken code repos</strong>, missing dependencies, failed builds.</p>
            <p>• Passive LLM chats lose context and cannot touch local files/tools.</p>
          </div>
          <div class="c c-left">
            <h3 style="color:#34d399;">🚀 Hermes Agent Solution</h3>
            <p>• <strong>Autonomous tool calling</strong>: Terminal, ArXiv, Python, Web extraction.</p>
            <p>• <strong>Persistent Memory</strong> & reusable <strong>Skill System</strong>.</p>
            <p>• <strong>Parallel subagents</strong> (`delegate_task`) for concurrent sweeps.</p>
            <p>• Runs on <strong>Local LLMs</strong> (oMLX/llama.cpp) & <strong>Cloud Providers</strong>.</p>
          </div>
        </div>
        <p style="margin-top:0.8em; color:#cbd5e1;">A unified terminal & GUI agent that acts as a full-time research assistant.</p>
      </section>

      <!-- Slide 3: Architecture Overview -->
      <section>
        <h2>Hermes Core Architecture</h2>
        <div class="m">
          <div class="c">
            <div class="n b">Skills</div>
            <p style="text-align:center;"><strong>Procedural Memory</strong><br>ArXiv, LaTeX, W&B, PyTorch, Git workflows.</p>
          </div>
          <div class="c">
            <div class="n g">Memory</div>
            <p style="text-align:center;"><strong>Durable Profile</strong><br>User bio, SSH nodes, GPU clusters, research domain.</p>
          </div>
          <div class="c">
            <div class="n p">Subagents</div>
            <p style="text-align:center;"><strong>Parallel Workers</strong><br>`delegate_task` for parallel experiments & sweeps.</p>
          </div>
          <div class="c">
            <div class="n o">Gateway</div>
            <p style="text-align:center;"><strong>Multi-Surface</strong><br>CLI, Desktop GUI, Web Dashboard, Telegram, Discord.</p>
          </div>
        </div>
        <p style="margin-top:0.8em; font-size: 0.8em; color:#94a3b8;">Supports 35+ providers: Local oMLX, vLLM, OpenAI, Anthropic, Gemini, DeepSeek, OpenRouter.</p>
      </section>

      <!-- Slide 4: Quick Installation & Setup -->
      <section>
        <h2>Installation & Research Environment Setup</h2>
        <div class="code-box">
          <pre><span class="cmt"># 1. Official Hermes Shell Installer (uv + python venv + launcher)</span>
<span class="cmd">curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash</span>

<span class="cmt"># 2. Interactive setup wizard (Pick provider: Local LLM, Gemini, OpenAI, etc.)</span>
<span class="cmd">hermes setup</span>

<span class="cmt"># 3. Check environment health & dependencies</span>
<span class="cmd">hermes doctor</span>

<span class="cmt"># 4. Launch Hermes interactive CLI or Desktop GUI</span>
<span class="cmd">hermes</span>           <span class="cmt"># Terminal REPL</span>
<span class="cmd">hermes desktop</span>   <span class="cmt"># Native Electron GUI</span></pre>
        </div>
      </section>

      <!-- Slide 5: Research Configuration (config.yaml & .env) -->
      <section>
        <h2>Tailored Research Configuration</h2>
        <p style="color:#38bdf8;">Configuring <code>~/.hermes/config.yaml</code> for Research Labs</p>
        <div class="code-box">
          <pre><span class="kw">model</span>:
  <span class="kw">default</span>: <span class="str">Qwen3.5-4B-OptiQ-4bit</span>        <span class="cmt"># Fast local model for baseline task</span>
  <span class="kw">provider</span>: <span class="str">custom</span>
  <span class="kw">base_url</span>: <span class="str">"http://127.0.0.1:8000/v1"</span>   <span class="cmt"># oMLX / llama-server local endpoint</span>
  <span class="kw">aliases</span>:
    <span class="kw">reasoning</span>: <span class="str">gemini/gemini-2.0-flash-lite</span>
    <span class="kw">deep-coder</span>: <span class="str">deepseek/deepseek-coder</span>

<span class="kw">agent</span>:
  <span class="kw">max_turns</span>: <span class="str">30</span>
  <span class="kw">context_compression</span>: <span class="str">true</span>            <span class="cmt"># Preserves state on huge paper reads</span>

<span class="kw">terminal</span>:
  <span class="kw">backend</span>: <span class="str">local</span>
  <span class="kw">workdir</span>: <span class="str">"/Users/farshid/research-projects"</span></pre>
        </div>
      </section>

      <!-- Slide 6: Key Hermes Skills for Researchers -->
      <section>
        <h2>Essential Hermes Skills for Academic Work</h2>
        <div class="m-3">
          <div class="c c-left">
            <h3 style="color:#22D3EE;">📚 Paper & Lit Review</h3>
            <p>• <code>arxiv</code> — Direct paper search & downloading.</p>
            <p>• <code>grounded-citations</code> — Verified source grounding.</p>
            <p>• <code>llm-wiki</code> — Karpathy-style Markdown Knowledge Base.</p>
          </div>
          <div class="c c-left">
            <h3 style="color:#30D158;">📊 Code & Execution</h3>
            <p>• <code>jupyter-live-kernel</code> — Live Python kernel.</p>
            <p>• <code>evaluating-llms-harness</code> — Benchmark suites.</p>
            <p>• <code>systematic-debugging</code> — 4-phase root cause analysis.</p>
          </div>
          <div class="c c-left">
            <h3 style="color:#A855F7;">📝 Publishing & Docs</h3>
            <p>• <code>docx</code> / <code>pdf</code> — Parse & edit research papers.</p>
            <p>• <code>architecture-diagram</code> — Dark-theme SVG diagrams.</p>
            <p>• <code>markdown-to-pdf</code> — Export clean PDF preprints.</p>
          </div>
        </div>
      </section>

      <!-- Slide 7: Workflow 1 - Automated ArXiv Sweeps -->
      <section>
        <h2>Workflow 1: Automated ArXiv Literature Sweeps</h2>
        <p style="color:#34d399;">Command: <em>"Find recent papers on 3D SLAM and build a literature matrix"</em></p>
        <div class="code-box">
          <pre><span class="cmt"># Hermes executes ArXiv search -> parses PDFs -> builds references matrix</span>
<span class="kw">from</span> hermes_tools <span class="kw">import</span> web_search, read_file, write_file

<span class="cmt"># 1. Search ArXiv by domain & topic</span>
results = arxiv_search(query=<span class="str">"cat:cs.CV AND title:SLAM"</span>, max_results=<span class="str">10</span>)

<span class="cmt"># 2. Extract key contributions, equations, and benchmarks</span>
matrix = []
<span class="kw">for</span> paper <span class="kw">in</span> results:
    pdf_text = web_extract(urls=[paper[<span class="str">'pdf_url'</span>]])
    summary = extract_key_innovations(pdf_text)
    matrix.append({<span class="str">"title"</span>: paper[<span class="str">'title'</span>], <span class="str">"bibtex"</span>: paper[<span class="str">'bib'</span>], <span class="str">"notes"</span>: summary})

<span class="cmt"># 3. Output clean Markdown matrix + references.bib</span>
write_file(<span class="str">"literature_review.md"</span>, format_matrix(matrix))
write_file(<span class="str">"references.bib"</span>, format_bibtex(matrix))</pre>
        </div>
      </section>

      <!-- Slide 8: Workflow 2 - Code Reproduction & Benchmarking -->
      <section>
        <h2>Workflow 2: Reproducing Code & Experiments</h2>
        <div class="m-2">
          <div class="c c-left">
            <h3>🔬 Automated Setup & Run</h3>
            <p>1. <strong>Clone GitHub Repo</strong>: Autonomous git checkout.</p>
            <p>2. <strong>Inspect & Resolve Deps</strong>: Reads <code>requirements.txt</code> / <code>environment.yml</code>.</p>
            <p>3. <strong>Fix Runtime Errors</strong>: Applies <code>systematic-debugging</code> to fix PyTorch CUDA mismatches or API changes.</p>
            <p>4. <strong>Log Metrics</strong>: Generates W&B or TensorBoard plots.</p>
          </div>
          <div class="c c-left">
            <h3>💻 Live Tool Output</h3>
            <div style="background:#020617; border-radius:6px; padding:8px; font-family:monospace; font-size:0.75em; color:#38bdf8;">
              $ hermes chat -q "Clone repository X, fix bugs, and run benchmark script"<br><br>
              <span style="color:#30d158;">[tool call]</span> terminal("git clone ...")<br>
              <span style="color:#30d158;">[tool call]</span> search_files(pattern="CUDA")<br>
              <span style="color:#30d158;">[tool call]</span> patch(file="model.py", old=..., new=...)<br>
              <span style="color:#30d158;">[tool call]</span> terminal("python eval.py --batch 32")<br>
              <span style="color:#fbbf24;">✓ Benchmark Complete: Accuracy = 94.2%</span>
            </div>
          </div>
        </div>
      </section>

      <!-- Slide 9: Workflow 3 - Drafting LaTeX & Research Papers -->
      <section>
        <h2>Workflow 3: Drafting LaTeX & Research Papers</h2>
        <div class="m-3">
          <div class="c">
            <div class="n b">1. Outline</div>
            <p>Generates structured IEEE/ACM template with Abstract, Introduction, Methodology, Experiments, Related Work.</p>
          </div>
          <div class="c">
            <div class="n g">2. Citation Check</div>
            <p>Uses <code>grounded-citations</code> to ensure every claim in the text links to a real ArXiv/DOI paper in <code>references.bib</code>.</p>
          </div>
          <div class="c">
            <div class="n p">3. Diagrams</div>
            <p>Produces publication-ready SVG architecture diagrams, flowcharts, or Manim mathematical animations.</p>
          </div>
        </div>
        <p style="margin-top:0.8em; font-size:0.8em; color:#94a3b8;">Zero hallucinated citations: claims are mechanically verified against PDF extractions.</p>
      </section>

      <!-- Slide 10: Workflow 4 - Parallel Research Swarms -->
      <section>
        <h2>Workflow 4: Parallel Research Swarms (`delegate_task`)</h2>
        <p style="color:#a855f7;">Spawning Concurrent Subagents for Heavy Academic Workloads</p>
        <div class="code-box">
          <pre><span class="cmt"># Main Hermes Agent dispatches 3 subagents in parallel</span>
delegate_task(tasks=[
  {
    <span class="str">"goal"</span>: <span class="str">"Search ArXiv for 2025-2026 Vision-Language-Action models and extract benchmarks"</span>,
    <span class="str">"context"</span>: <span class="str">"Focus on robotics manipulation"</span>
  },
  {
    <span class="str">"goal"</span>: <span class="str">"Benchmark Qwen3.5 vs K2-Horizon on local M3 GPU using llama.cpp"</span>,
    <span class="str">"context"</span>: <span class="str">"Log tokens/sec, memory usage, and context latency"</span>
  },
  {
    <span class="str">"goal"</span>: <span class="str">"Format collected findings into an IEEE LaTeX draft"</span>,
    <span class="str">"context"</span>: <span class="str">"Save to ~/paper_draft/main.tex"</span>
  }
])</pre>
        </div>
      </section>

      <!-- Slide 11: Persistent Memory & Custom Lab Skills -->
      <section>
        <h2>Persistent Memory & Custom Lab Skills</h2>
        <div class="m-2">
          <div class="c c-left">
            <h3 style="color:#38bdf8;">🧠 Persistent Memory (<code>memory</code>)</h3>
            <p>Stores facts that survive across every terminal session:</p>
            <p>• Primary research focus (e.g. <em>Computer Vision, 3D Reconstruction</em>).</p>
            <p>• Lab GPU Cluster details (e.g. <em>SLURM partition <code>a100-80gb</code>, node IPs</em>).</p>
            <p>• Preferred paper format & writing style guidelines.</p>
          </div>
          <div class="c c-left">
            <h3 style="color:#fbbf24;">⚡ Custom Skills (<code>skill_manage</code>)</h3>
            <p>Teaches Hermes specialized lab procedures:</p>
            <p>• <strong>Slurm Job Submission</strong>: <code>sbatch</code> script creation & queue monitoring.</p>
            <p>• <strong>HuggingFace Dataset Uploads</strong>: Automated push of custom datasets.</p>
            <p>• <strong>Lab Calibration Pipeline</strong>: Multi-camera camera intrinsic sweeps.</p>
          </div>
        </div>
      </section>

      <!-- Slide 12: Cost & Token Efficiency Comparison -->
      <section>
        <h2>Cost & Token Efficiency Comparison</h2>
        <div class="m">
          <div class="c">
            <div class="n g">0 $</div>
            <p><strong>Local oMLX / Ollama</strong><br>100% private, zero cost, runs on Mac/Linux.</p>
          </div>
          <div class="c">
            <div class="n b">90%</div>
            <p><strong>Prompt Caching</strong><br>Free cache hits on long paper context blocks.</p>
          </div>
          <div class="c">
            <div class="n p">99%</div>
            <p><strong>Codebase Memory</strong><br>Graph queries replace reading full repos.</p>
          </div>
          <div class="c">
            <div class="n o">10x</div>
            <p><strong>Speedup</strong><br>Parallel subagent sweeps vs manual searching.</p>
          </div>
        </div>
        <p style="margin-top:0.8em; font-size: 0.85em;">Local models handle draft tasks & code execution; Cloud models handle complex reasoning.</p>
      </section>

      <!-- Slide 13: Case Study - Computer Vision Research -->
      <section>
        <h2>Case Study: Computer Vision & 3D Reconstruction</h2>
        <div class="m-2">
          <div class="c c-left">
            <h3 style="color:#22D3EE;">Project Goal</h3>
            <p>Build an end-to-end multi-camera 3D point cloud generation pipeline and publish open source benchmarks on pirahansiah.com.</p>
            <p><strong>Hermes Execution</strong>:</p>
            <p>• Pulled 15 camera calibration papers from ArXiv.</p>
            <p>• Debugged OpenCV / GStreamer C++ DMA pipeline.</p>
            <p>• Generated benchmark tables and SVG pipeline diagrams.</p>
          </div>
          <div class="c c-left">
            <h3 style="color:#30D158;">Deliverables Produced</h3>
            <p>✓ <code>3d-vision.md</code> documentation page on website.</p>
            <p>✓ Verified OpenCV C++ code with zero memory leaks.</p>
            <p>✓ BibTeX reference database with 15 verified citations.</p>
            <p>✓ Interactive web visualizer demo.</p>
          </div>
        </div>
      </section>

      <!-- Slide 14: Summary & Next Steps -->
      <section>
        <h1>Summary & Key Takeaways</h1>
        <div style="text-align:left; max-width:800px; margin:0.8em auto; font-size:0.9em; line-height:1.7;">
          <p>✔ <strong>Autonomous Research Agent</strong>: Move from passive chatting to active tool execution.</p>
          <p>✔ <strong>End-to-End Workflow</strong>: Literature review → Code reproduction → Experimentation → Paper drafting.</p>
          <p>✔ <strong>Lab Privacy & Local Serving</strong>: Run on local oMLX / llama.cpp or Cloud APIs seamlessly.</p>
          <p>✔ <strong>Parallel Power</strong>: Use subagents (`delegate_task`) for concurrent paper sweeps.</p>
        </div>
        <p style="margin-top:1.2em; color:#22D3EE; font-size:1.1em; font-weight: bold;">
          Explore the Knowledge Base & Code: pirahansiah.com
        </p>
      </section>

      <!-- Slide 15: Thank You Slide -->
      <section>
        <h1>Thank You & Discussion</h1>
        <h2 style="color:#cbd5e1;">Hermes Agent for Research Assistance</h2>
        <p style="margin-top:1.5em;">
          <a href="https://www.pirahansiah.com/notes/docs/research/" style="color:#38bdf8; text-decoration:underline;">Research Publications & Notes</a> • 
          <a href="https://github.com/pirahansiah" style="color:#38bdf8; text-decoration:underline;">GitHub Repositories</a>
        </p>
        <div style="margin-top:2em;">
          <button id="restart-btn" style="background:rgba(34,211,238,0.2); color:#22D3EE; border:1px solid #22D3EE; padding:12px 24px; border-radius:10px; cursor:pointer; font-size:0.9em; font-weight:bold;">
            🔄 Restart Presentation
          </button>
        </div>
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
    width: 1050, 
    height: 720, 
    margin: 0.08, 
    minScale: 0.2, 
    maxScale: 2.0 
  });
  deck.initialize();
  
  document.getElementById('restart-btn').addEventListener('click', function(e) { 
    e.stopPropagation(); 
    deck.slide(0); 
  });
  
  document.querySelector('.presentation-panel').addEventListener('click', function(event) {
    if (event.target.closest('button, a, .controls, .progress, pre, code')) return;
    const rect = this.getBoundingClientRect();
    const x = event.clientX - rect.left;
    if (x < rect.width * 0.35) { deck.prev(); } else if (x > rect.width * 0.65) { deck.next(); }
  });
</script>
