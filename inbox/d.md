---
layout: presentation
title: My Project
---

<style>
  /* Ensure the presentation has a specific area to live in */
  .presentation-container {
    height: 80vh; /* Adjust this to make it smaller/larger */
    width: 90%;
    margin: 20px auto;
    position: relative;
    border-radius: 30px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.2);
  }

  .reveal {
    background: rgba(0, 0, 0, 0.5) !important;
    backdrop-filter: blur(10px);
  }

  /* Fixes the "Top" issue - centers the slides vertically */
  .reveal .slides {
    text-align: center;
  }
</style>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/reveal.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/theme/black.css">

<div class="presentation-container">
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
  // Crucial: we tell Reveal which element to use as the viewport
  let deck = new Reveal(document.querySelector('.presentation-container'), {
    embedded: true, // This keeps it inside your box, not full screen
    hash: true,
    center: true,   // Vertically centers the content
    transition: 'slide'
  });
  deck.initialize();
</script>