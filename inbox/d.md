---
layout: default
title: My Project
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/reveal.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/theme/black.min.css">

<style>
body {
  margin: 0;
  background: radial-gradient(circle at top, #1a1a2e, #0f0f1a);
  font-family: system-ui;
}

.reveal {
  font-size: 1.6em;
  color: #fff;
}

.reveal h1, .reveal h2 {
  letter-spacing: 1px;
  text-transform: none;
}

.reveal section {
  padding: 20px;
}

.glass {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 16px;
  padding: 30px;
  backdrop-filter: blur(10px);
  box-shadow: 0 10px 40px rgba(0,0,0,0.4);
}

.reveal .slides section {
  transition: transform 0.6s ease, opacity 0.6s ease;
}

.fragment {
  opacity: 0;
  transform: translateY(10px);
}

.fragment.visible {
  opacity: 1;
  transform: translateY(0);
  transition: all 0.5s ease;
}

code {
  font-size: 0.9em;
  background: #111;
  padding: 10px;
  border-radius: 10px;
  display: block;
}
</style>

<div class="reveal">
  <div class="slides">

    <section class="glass">
      <h1>My Project</h1>
      <p>Use → and ↓ to navigate</p>
    </section>

    <section>
      <section class="glass">
        <h2>Frontend</h2>
      </section>

      <section class="glass">
        <h2>React</h2>
        <ul>
          <li class="fragment">Components</li>
          <li class="fragment">Hooks</li>
        </ul>
      </section>

      <section class="glass">
        <h2>CSS</h2>
        <ul>
          <li class="fragment">Tailwind</li>
          <li class="fragment">Animations</li>
        </ul>
      </section>
    </section>

    <section>
      <section class="glass">
        <h2>Backend</h2>
      </section>

      <section class="glass">
        <h2>Database</h2>
        <ul>
          <li class="fragment">Postgres</li>
          <li class="fragment">Redis</li>
        </ul>
      </section>
    </section>

    <section class="glass">
      <h2>Code</h2>
      <pre><code>
fetch('/api/data')
  .then(res => res.json())
  .then(data => console.log(data));
      </code></pre>
    </section>

  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.0/reveal.js"></script>

<script>
Reveal.initialize({
  hash: true,
  transition: 'convex',
  backgroundTransition: 'fade',
  controls: true,
  progress: true,
  center: true,
  fragments: true
});
</script>