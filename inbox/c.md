---
layout: default
title: Farshid Pirahansiah

---
---
layout: default
---

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
      <h1>My Project</h1>
      <p>Press <kbd>→</kbd> to go forward, <kbd>↓</kbd> for sub-slides</p>
    </section>

    <!-- Slide 2 — with vertical sub-slides -->
    <section>
      <section>
        <h2>Frontend</h2>
        <p>Press ↓ for details</p>
      </section>
      <section>
        <h2>React</h2>
        <ul>
          <li class="fragment">Components</li>
          <li class="fragment">Hooks</li>
        </ul>
      </section>
      <section>
        <h2>CSS</h2>
        <ul>
          <li class="fragment">Tailwind</li>
          <li class="fragment">Animations</li>
        </ul>
      </section>
    </section>

    <!-- Slide 3 -->
    <section>
      <section>
        <h2>Backend</h2>
      </section>
      <section>
        <h2>Database</h2>
        <ul>
          <li class="fragment fade-up">Postgres</li>
          <li class="fragment fade-up">Redis</li>
        </ul>
      </section>
    </section>

    <!-- Slide 4 — code highlight -->
    <section>
      <h2>Code</h2>
      <pre><code class="language-js">
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
    transition: 'slide',       // none / fade / slide / convex / concave / zoom
    transitionSpeed: 'default',
    backgroundTransition: 'fade',
    controls: true,
    progress: true,
    center: true,
  });
</script>


computer vision in IoT
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
defaults write com.apple.desktopservices DSDontWriteUSBStores -bool TRUE
dot_clean -m /Volumes/4tb
sudo mdutil -i off /Volumes/4tb
touch /Volumes/4tb/.metadata_never_index

cd /Volumes/4tb/2026-6/pirahansiah.github.io
git submodule update --remote --merge
