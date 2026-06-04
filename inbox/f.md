---
layout: presentation
title: Data & DevOps
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/reveal.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/theme/black.min.css">

<style>
  .presentation-deck {
    width: 95%;
    max-width: 1000px;
    height: 75vh;
    position: relative;
    border-radius: 24px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.1);
    margin: 2rem auto;
  }

  .presentation-deck .reveal {
    background: rgba(0, 0, 0, 0.5) !important;
    backdrop-filter: blur(10px);
  }

  .presentation-deck .reveal .slides {
    text-align: center;
  }

  .glass-slide {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 16px;
    padding: 30px !important;
    backdrop-filter: blur(10px);
  }
</style>

<div class="presentation-deck">
  <div class="reveal">
    <div class="slides">
      <section class="glass-slide">
        <h1>Data & DevOps</h1>
        <p>Press <kbd>→</kbd> to start</p>
      </section>

      <section>
        <section>
          <h2>Backend</h2>
          <p>Press ↓ for details</p>
        </section>
        
        <section>
          <h2>Database & Assets</h2>
          <ul>
            <li class="fragment fade-up">Postgres</li>
            <li class="fragment fade-up">Redis</li>
          </ul>
        </section>

        <section>
          <h2>Python Logic (c.py)</h2>
          <pre><code class="language-python" data-trim>
# contents/inbox/c.py
import math

def calculate_liquid_glass():
    return "iOS 26 Style"
          </code></pre>
        </section>
      </section>
    </div>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/reveal.js"></script>
<script>
  Reveal.initialize({
    embedded: true,
    center: true,
    hash: true,
    transition: 'convex',
    display: 'block'
  });
</script>