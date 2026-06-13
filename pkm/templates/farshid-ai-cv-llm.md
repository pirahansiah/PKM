---
layout: farshid_default
title: farshid-ai-cv-llm
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/reveal.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/theme/black.min.css">

<style>
  body { background: #000 !important; overflow: hidden !important; }
  .site-main { padding: 0 !important; margin: 0 !important; background: #000 !important; border: none !important; box-shadow: none !important; }
  .toolbar, .site-footer, footer { display: none !important; }

  .presentation-panel {
    position: relative;
    width: 100%;
    height: calc(100vh - 60px);
    margin-top: 60px;
    border-radius: 0;
    overflow: hidden;
    background: #000;
    border: none;
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

  .slide-image {
    flex-shrink: 1;
    flex-grow: 0;
    max-width: 90% !important;
    max-height: 55% !important;
    object-fit: contain !important;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.2);
    margin: 10px 0 !important;
  }

  .reveal h1 { font-size: 1.8em; margin-bottom: 0.5em; color: #fff; }
  .reveal h2 { font-size: 1.4em; margin: 0.2em 0; color: #fff; }
  .reveal p, .reveal li { font-size: 0.7em; color: #ccc; }
  .reveal ul { list-style: none; padding: 0; }
  .reveal pre { width: 90%; }
  .reveal code { font-size: 0.8em; }
  .reveal .controls { color: #fff; }

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

      <!-- Slide 0 -->
      <section>
        <h1>**Start**</h1>
        <p>Technical Product Management & Strategic Consultancy for Embedded AI Vision Systems. </p>
        <p> Bridging the gap between R&D curiosity and Production-grade AI.</p>
      </section>

      <!-- Slide 2 — THE IMAGE SLIDE (Now Fixed) -->
      <section>
        <h2>System Architecture</h2>
        <p>Full Overview of Workflow</p>
        
        <img src="{{ '/contents/inbox/c.png' | relative_url }}" class="slide-image" alt="Architecture Diagram">
        
        <p>This diagram shows the CI/CD pipeline integrated with Postgres.</p>
      </section>

      <!-- Slide 3 -->
      <section>
        <section>
          <h2>Backend Logic</h2>
          <p>The code is rendered below ↓</p>
        </section>
        <section>
          <h2>Python (c.py)</h2>
          <pre><code class="language-python">
import math
def calculate_refraction():
    return "Liquid Effect Applied"
          </code></pre>
        </section>
      </section>

      <!-- Slide 4 -->
      <section>
        <h2>DevOps Stack</h2>
        <ul>
          <li class="fragment">Docker Containers</li>
          <li class="fragment">GitHub Actions CI</li>
          <li class="fragment">AWS Cloudfront</li>
        </ul>
      </section>

      <!-- Slide End -->
      <section>
        <h1>**End**</h1>
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
    // Helps fit content automatically
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

  // LEFT/RIGHT CLICK NAVIGATION
  document.querySelector('.presentation-panel').addEventListener('click', function(event) {
    // Don't trigger if clicking on a button or the native reveal controls
    if (event.target.closest('button, a, .controls, .progress')) return;

    const rect = this.getBoundingClientRect();
    const x = event.clientX - rect.left;
    
    // Left 40% goes back, Right 60% goes forward (better for natural tapping)
    if (x < rect.width * 0.4) {
      deck.prev();
    } else {
      deck.next();
    }
  });
</script>
