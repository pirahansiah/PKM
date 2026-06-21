---
layout: farshid_default
title: "Product — Embedded CV & Edge AI"
---

<style>
.sitemap-hero {
  text-align: center;
  padding: 48px 24px 32px;
}
.sitemap-hero h1 {
  font-size: 2.4rem;
  background: linear-gradient(135deg, #0a84ff, #bf5af2, #ff375f);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 8px;
}
.sitemap-hero p { color: var(--text-muted); font-size: 1.1rem; }

.sitemap-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 20px;
  padding: 0 16px;
  max-width: 1200px;
  margin: 0 auto;
}

.sitemap-section {
  border-radius: 20px;
  padding: 28px 24px;
  background: var(--glass-bg);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid var(--glass-border);
  box-shadow: var(--glass-shadow);
  transition: transform 0.3s cubic-bezier(0.4,0,0.2,1), box-shadow 0.3s ease;
  position: relative;
  overflow: hidden;
}
.sitemap-section::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: linear-gradient(135deg, rgba(255,255,255,0.5) 0%, rgba(255,255,255,0) 50%);
  pointer-events: none;
  opacity: 0.6;
}
.sitemap-section:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(0,0,0,0.15);
}

.section-icon { font-size: 2rem; margin-bottom: 12px; display: block; }

.section-title {
  font-size: 1.15rem;
  font-weight: 700;
  margin-bottom: 14px;
  color: var(--text);
  display: flex;
  align-items: center;
  gap: 8px;
}

.section-title .badge {
  font-size: 0.7rem;
  background: rgba(10,132,255,0.2);
  color: #0a84ff;
  padding: 2px 8px;
  border-radius: 20px;
  font-weight: 600;
}

.sitemap-links {
  list-style: none;
  padding: 0;
  margin: 0;
}

.sitemap-links li { margin-bottom: 6px; }

.sitemap-links a {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  border-radius: 10px;
  text-decoration: none;
  color: var(--text);
  font-size: 0.92rem;
  transition: background 0.2s ease, transform 0.15s ease;
  background: rgba(255,255,255,0.06);
  border: 1px solid transparent;
}
.sitemap-links a:hover {
  background: rgba(10,132,255,0.12);
  border-color: rgba(10,132,255,0.3);
  transform: translateX(4px);
}
.sitemap-links a .link-arrow {
  opacity: 0;
  transition: opacity 0.2s ease;
  font-size: 0.8rem;
  color: #0a84ff;
}
.sitemap-links a:hover .link-arrow { opacity: 1; }

.back-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 24px;
  padding: 8px 16px;
  border-radius: 10px;
  text-decoration: none;
  color: var(--text-muted);
  font-size: 0.9rem;
  background: rgba(255,255,255,0.08);
  transition: all 0.2s ease;
}
.back-link:hover {
  background: rgba(10,132,255,0.1);
  color: var(--text);
}

@media (max-width: 768px) {
  .sitemap-grid { grid-template-columns: 1fr; padding: 0 8px; }
  .sitemap-hero h1 { font-size: 1.8rem; }
}
</style>

<div class="sitemap-hero">
  <h1>Product</h1>
  <p>Embedded computer vision & edge AI systems</p>
</div>

<div style="text-align:center; padding: 0 16px;">
  <a href="/" class="back-link">&#8592; Home</a>
  <a href="/contents/public/research/" class="back-link">Research</a>
  <a href="/contents/public/solutions/" class="back-link">Solutions</a>
</div>

<div class="sitemap-grid">

  <div class="sitemap-section">
    <span class="section-icon">&#128065;</span>
    <div class="section-title">Computer Vision <span class="badge">Core</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/public/cv/3d/"><span class="link-arrow">&#8594;</span> 3D Vision & Multi-Camera</a></li>
      <li><a href="/contents/public/cv/optical-flow/"><span class="link-arrow">&#8594;</span> Optical Flow</a></li>
      <li><a href="/contents/public/cv/multi-camera-systems/"><span class="link-arrow">&#8594;</span> Multi-Camera Systems</a></li>
      <li><a href="/contents/public/coaching/"><span class="link-arrow">&#8594;</span> CV Coaching Roadmap</a></li>
    </ul>
  </div>

  <div class="sitemap-section">
    <span class="section-icon">&#129302;</span>
    <div class="section-title">AI & LLMs <span class="badge">New</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/public/ai-llm/advanced-llm-concepts/"><span class="link-arrow">&#8594;</span> Advanced LLM Concepts</a></li>
      <li><a href="/contents/public/ai-llm/orchestrating-agents/"><span class="link-arrow">&#8594;</span> Orchestrating AI Agents</a></li>
      <li><a href="/contents/public/ai-llm/blog/"><span class="link-arrow">&#8594;</span> AI Blog</a></li>
      <li><a href="/contents/public/ai-llm/avatar-generator/"><span class="link-arrow">&#8594;</span> Avatar Generator</a></li>
    </ul>
  </div>

  <div class="sitemap-section">
    <span class="section-icon">&#9889;</span>
    <div class="section-title">CUDA & GPU <span class="badge">Dev</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/public/cuda-gpu/numba-jit/"><span class="link-arrow">&#8594;</span> Numba JIT Tutorial</a></li>
      <li><a href="/contents/public/cuda-gpu/pycuda-kernels/"><span class="link-arrow">&#8594;</span> PyCUDA Kernels</a></li>
      <li><a href="/contents/public/cuda-gpu/vscode-cuda-windows/"><span class="link-arrow">&#8594;</span> CUDA in VS Code</a></li>
      <li><a href="/contents/public/cuda-gpu/mlx-coreml-metal/"><span class="link-arrow">&#8594;</span> MLX, CoreML & Metal</a></li>
    </ul>
  </div>

  <div class="sitemap-section">
    <span class="section-icon">&#9881;</span>
    <div class="section-title">Optimization <span class="badge">ML</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/public/Optimization/"><span class="link-arrow">&#8594;</span> CV/DL/ML Optimization</a></li>
      <li><a href="/contents/public/Prompts/"><span class="link-arrow">&#8594;</span> Prompt Engineering</a></li>
    </ul>
  </div>

  <div class="sitemap-section">
    <span class="section-icon">&#128187;</span>
    <div class="section-title">Programming</div>
    <ul class="sitemap-links">
      <li><a href="/contents/public/CPP/"><span class="link-arrow">&#8594;</span> C++ Quick Reference</a></li>
      <li><a href="/contents/public/Python/"><span class="link-arrow">&#8594;</span> Python Configuration</a></li>
      <li><a href="/contents/public/setup/"><span class="link-arrow">&#8594;</span> Developer Tools</a></li>
      <li><a href="/contents/public/shell-vim-quickref/"><span class="link-arrow">&#8594;</span> Shell & Vim</a></li>
    </ul>
  </div>

</div>
