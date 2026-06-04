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

  /* 3. Style the Image to fit inside the slide */
  .slide-image {
    max-width: 80%;
    max-height: 300px;
    border-radius: 12px;
    border: 2px solid rgba(255,255,255,0.2);
    margin-top: 10px;
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

      <!-- Slide 1 — Title -->
      <section>
        <h1>Data & DevOps</h1>
        <p style="font-size: 0.5em;">Tap anywhere to go forward</p>
      </section>

      <!-- Slide 2 — THE IMAGE SLIDE -->
      <section>
        <h2>System Architecture</h2>
        <img src="{{ '/contents/inbox/c.png' | relative_url }}" class="slide-image" alt="Architecture Diagram">
        <p style="font-size: 0.4em;">Contents from /inbox/c.png</p>
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

  // MOBILE FRIENDLY: Tap anywhere on the presentation to go to the next slide
  document.querySelector('.presentation-panel').addEventListener('click', function() {
    deck.next();
  });
</script>