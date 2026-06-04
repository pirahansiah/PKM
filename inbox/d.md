---
layout: presentation
title: My Project
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
      <section>
        <h1>My Project</h1>
        <p>Press <kbd>→</kbd> to start</p>
      </section>

      <section>
        <section>
          <h2>Frontend</h2>
          <p>Press ↓ for details</p>
        </section>
        <section>
          <h2>React</h2>
          <ul>
            <li class="fragment">Components</li>
          </ul>
        </section>
      </section>
    </div>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/reveal.js"></script>
<script>
  Reveal.initialize({
    embedded: true,
    hash: true,
    center: true,
    transition: 'slide',
    display: 'block'
  });
</script>