---
layout: default
title: Data & DevOps
---

<style>
  /* 1. Ensure the presentation panel fits the Liquid Glass style */
  .presentation-panel {
    position: relative;
    width: 100%;
    min-height: 70vh;
    margin: 20px 0;
    border-radius: 24px;
    overflow: hidden;
    background: rgba(0, 0, 0, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.1);
  }

  .presentation-panel .reveal {
    height: 100%;
  }

  .reveal .slides section {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 1rem;
    padding: 1.5rem;
    box-sizing: border-box;
    text-align: center;
  }

  /* 2. Center the slides and make them mobile-responsive */
  .reveal {
    font-size: 0.8em; /* Slightly smaller for mobile compatibility */
  }

  .reveal h1 { font-size: 2.2em; }
  .reveal h2 { font-size: 1.6em; }

  /* 3. Style the Image/Video to fit inside the slide and always show the full image */
  .slide-image {
    max-width: calc(100vw - 40px);
    max-height: calc(100vh - 240px);
    width: auto;
    height: auto;
    object-fit: contain;
    border-radius: 12px;
    border: 2px solid rgba(255,255,255,0.2);
    margin: 0 auto;
    display: block;
  }

  .slide-image, .slide-video {
    max-width: calc(100vw - 40px);
    max-height: calc(100vh - 240px);
  }

  .slide-video {
    width: auto;
    height: auto;
    object-fit: contain;
    border-radius: 12px;
    border: 2px solid rgba(255,255,255,0.2);
    margin: 0 auto;
    display: block;
  }

  /* 4. Ensure code blocks don't overflow on iPhone */
  pre code {
    font-size: 0.5em !important;
    line-height: 1.2 !important;
  }
</style>

<!-- Load Reveal.js Assets -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/reveal.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/theme/black.min.css">

<div class="presentation-panel">
  <div class="reveal">
    <div class="slides">

      <!-- Slide 0 — Title -->
      <section>
        <h1>**Start**</h1>
        <p style="font-size: 0.5em;">Tap anywhere to go forward</p>
      </section>
      
      <!-- Slide 1 — Title -->
      <section>
        <h1>Data & DevOps</h1>
        <p style="font-size: 0.5em;">Tap anywhere to go forward</p>
      </section>

      <!-- Slide 2 — THE IMAGE SLIDE -->
      <section>
        <h2>System Architecture</h2>
        <img src="{{ '/contents/inbox/c.png' | relative_url }}" class="slide-image" alt="Architecture Diagram">
        <p style="font-size: 0.4em;">Tap left to go back, right to go next. Full image shown even if smaller.</p>
      </section>

      <!-- Slide 3 — Vertical Sub-slides -->
      <section>
        <section>
          <h2>Backend</h2>
          <p>Press ↓ for code</p>
        </section>
        <section>
          <h2>Python Logic (c.py)</h2>
          <pre><code class="language-python">
import math
def calculate_liquid_glass():
    return "iOS 26 Style"
          </code></pre>
        </section>
      </section>

      <!-- Slide 4 — DevOps -->
      <section>
        <h2>DevOps</h2>
        <ul>
          <li class="fragment">Docker</li>
          <li class="fragment">CI/CD</li>
          <li class="fragment">Cloud Deployment</li>
        </ul>
      </section>
      <!-- Slide End — Title -->
      <section>
        <h1>**End**</h1>
        <p style="font-size: 0.5em;">Tap anywhere to go forward</p>
      </section>

    </div>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/reveal.js"></script>
<script>
  // Initialize Reveal inside the panel
  let deck = new Reveal(document.querySelector('.presentation-panel'), {
    embedded: true,    // IMPORTANT: Keeps your main menu/nav visible
    hash: true,
    center: true,      // Centers slides vertically in the panel
    touch: true,       // Enables swipe on iPhone
    controls: true,
    progress: true,
    mouseWheel: false
  });

  deck.initialize();

  // MOBILE FRIENDLY: Tap left for previous slide, right for next slide
  document.querySelector('.presentation-panel').addEventListener('click', function(event) {
    const panel = event.currentTarget;
    const controlClick = event.target.closest('button, a, .reveal .controls');
    if (controlClick) {
      return;
    }

    const rect = panel.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const isLeft = x < rect.width * 0.5;

    if (isLeft) {
      deck.prev();
    } else {
      deck.next();
    }
  });
</script>