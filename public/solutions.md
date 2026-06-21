---
layout: farshid_default
title: "Solutions — How I Help Businesses"
---

<style>
.toc-hero {
  text-align: center;
  padding: 48px 24px 32px;
}
.toc-hero h1 {
  font-size: 2.2rem;
  background: linear-gradient(135deg, #0a84ff, #bf5af2);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 8px;
}
.toc-hero p { color: var(--text-muted); font-size: 1.05rem; }

.toc-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  max-width: 1000px;
  margin: 0 auto 40px;
  padding: 0 16px;
}
.toc-card {
  border-radius: 18px;
  padding: 24px;
  background: var(--glass-bg);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid var(--glass-border);
  box-shadow: var(--glass-shadow);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  position: relative;
  overflow: hidden;
}
.toc-card::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: linear-gradient(135deg, rgba(255,255,255,0.5) 0%, rgba(255,255,255,0) 50%);
  pointer-events: none;
  opacity: 0.5;
}
.toc-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(0,0,0,0.12);
}
.toc-card h2 {
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.toc-card ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
.toc-card li {
  margin-bottom: 6px;
}
.toc-card a {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  border-radius: 10px;
  text-decoration: none;
  color: var(--text);
  font-size: 0.9rem;
  transition: all 0.15s ease;
  background: rgba(255,255,255,0.05);
}
.toc-card a:hover {
  background: rgba(10,132,255,0.1);
  transform: translateX(3px);
}
.toc-card a .arr {
  opacity: 0;
  color: #0a84ff;
  transition: opacity 0.15s ease;
  font-size: 0.8rem;
}
.toc-card a:hover .arr { opacity: 1; }
</style>

<div class="toc-hero">
  <h1>Solutions</h1>
  <p>Turn AI research into production-ready products</p>
</div>

<div class="toc-grid">

  <div class="toc-card">
    <h2>&#128640; AI 2026 — Courses</h2>
    <ul>
      <li><a href="/contents/ai2026/machine-learning-specialization/"><span class="arr">&#8594;</span> ML Specialization</a></li>
      <li><a href="/contents/ai2026/full-stack-deep-learning/"><span class="arr">&#8594;</span> Full Stack Deep Learning</a></li>
      <li><a href="/contents/ai2026/mlops/"><span class="arr">&#8594;</span> MLOps</a></li>
    </ul>
  </div>

  <div class="toc-card">
    <h2>&#128218; Workshops</h2>
    <ul>
      <li><a href="/contents/ai2026/edge-ai-summit/"><span class="arr">&#8594;</span> Edge AI Summit</a></li>
      <li><a href="/contents/ai2026/ai-hardware/"><span class="arr">&#8594;</span> AI Hardware</a></li>
      <li><a href="/contents/ai2026/embedded-iot/"><span class="arr">&#8594;</span> Embedded IoT</a></li>
    </ul>
  </div>

  <div class="toc-card">
    <h2>&#128161; Business</h2>
    <ul>
      <li><a href="/contents/public/StartUp/"><span class="arr">&#8594;</span> Startup Guide</a></li>
      <li><a href="/contents/public/SEO/"><span class="arr">&#8594;</span> SEO for LLMs</a></li>
      <li><a href="/contents/public/Prompts/"><span class="arr">&#8594;</span> Prompt Engineering</a></li>
    </ul>
  </div>

  <div class="toc-card">
    <h2>&#128218; Resources</h2>
    <ul>
      <li><a href="/contents/public/links/"><span class="arr">&#8594;</span> Curated Links</a></li>
      <li><a href="/contents/public/linkedin-top-posts/"><span class="arr">&#8594;</span> Top LinkedIn Posts</a></li>
      <li><a href="/contents/ai2026/book-summary/"><span class="arr">&#8594;</span> Book Summaries</a></li>
    </ul>
  </div>

  <div class="toc-card">
    <h2>&#128221; Connect</h2>
    <ul>
      <li><a href="https://www.linkedin.com/in/pirahansiah/" target="_blank" rel="noopener"><span class="arr">&#8594;</span> LinkedIn</a></li>
      <li><a href="https://github.com/pirahansiah" target="_blank" rel="noopener"><span class="arr">&#8594;</span> GitHub</a></li>
      <li><a href="/contents/sitemap/"><span class="arr">&#8594;</span> Full Sitemap</a></li>
    </ul>
  </div>

</div>
