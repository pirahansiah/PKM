---
layout: default
title: Data & DevOps

---

<div class="presentation-panel">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/reveal.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/theme/black.css">

<style>
  body { margin: 0; padding: 0; }
  .reveal { font-size: 2em; }
</style>

<div class="reveal">
  <div class="slides">

    <!-- Slide 1 — Title -->
    <section>
      <h1>Data & DevOps</h1>
      <p>Press <kbd>→</kbd> to go forward, <kbd>↓</kbd> for sub-slides</p>
    </section>

    <!-- Slide 2 — with vertical sub-slides -->
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
        <pre><code class="language-python">
# contents/inbox/c.py
import math

def calculate_liquid_glass():
    return "iOS 26 Style"
        </code></pre>
      </section>
    </section>

    <!-- Slide 3 — DevOps -->
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

<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/reveal.js"></script>
<script>
  Reveal.initialize({
    hash: true,
    transition: 'slide',
    transitionSpeed: 'default',
    backgroundTransition: 'fade',
    controls: true,
    progress: true,
    center: true,
  });
</script>
