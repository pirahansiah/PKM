---
layout: presentation
title: My Project
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/reveal.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/theme/black.min.css">

<style>
/* Create a container so Reveal.js knows how much space it has */
.reveal-wrapper {
  width: 100%;
  height: 90vh;
  position: relative;
}

.glass-slide {
  background: rgba(255,255,255,0.06) !important;
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 16px;
  padding: 30px !important;
  backdrop-filter: blur(10px);
}
</style>

<div class="reveal-wrapper">
  <div class="reveal">
    <div class="slides">
      <section class="glass-slide">
        <h1>My Project</h1>
        <p>If you see this, it is working.</p>
      </section>
      
      <section>
        <h2>Backend</h2>
        <p>Database: Postgres</p>
      </section>
    </div>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/reveal.js"></script>
<script>
  // Initializing within the wrapper
  Reveal.initialize({
    embedded: true, // REQUIRED when inside a Jekyll layout container
    center: true,
    hash: true,
    transition: 'convex',
    // Helps with visibility
    display: 'block' 
  });
</script>
