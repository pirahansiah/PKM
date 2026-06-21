---
layout: farshid_default
title: "Product — Embedded CV & Edge AI"
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
  <h1>Product</h1>
  <p>What I build: embedded computer vision & edge AI systems</p>
</div>

<div class="toc-grid">

  <div class="toc-card">
    <h2>&#128065; Computer Vision</h2>
    <ul>
      <li><a href="/contents/public/cv/3d/"><span class="arr">&#8594;</span> 3D Vision & Multi-Camera</a></li>
      <li><a href="/contents/public/cv/optical-flow/"><span class="arr">&#8594;</span> Optical Flow</a></li>
      <li><a href="/contents/public/cv/multi-camera-systems/"><span class="arr">&#8594;</span> Multi-Camera Systems</a></li>
    </ul>
  </div>

  <div class="toc-card">
    <h2>&#129302; AI & LLMs</h2>
    <ul>
      <li><a href="/contents/public/ai-llm/advanced-llm-concepts/"><span class="arr">&#8594;</span> Advanced LLM Concepts</a></li>
      <li><a href="/contents/public/ai-llm/orchestrating-agents/"><span class="arr">&#8594;</span> Orchestrating AI Agents</a></li>
      <li><a href="/contents/public/ai-llm/blog/"><span class="arr">&#8594;</span> AI Blog</a></li>
    </ul>
  </div>

  <div class="toc-card">
    <h2>&#9889; CUDA & GPU</h2>
    <ul>
      <li><a href="/contents/public/cuda-gpu/numba-jit/"><span class="arr">&#8594;</span> Numba JIT</a></li>
      <li><a href="/contents/public/cuda-gpu/pycuda-kernels/"><span class="arr">&#8594;</span> PyCUDA Kernels</a></li>
      <li><a href="/contents/public/cuda-gpu/mlx-coreml-metal/"><span class="arr">&#8594;</span> MLX, CoreML & Metal</a></li>
    </ul>
  </div>

  <div class="toc-card">
    <h2>&#9881; Optimization</h2>
    <ul>
      <li><a href="/contents/public/Optimization/"><span class="arr">&#8594;</span> CV/DL/ML Optimization</a></li>
      <li><a href="/contents/public/coaching/"><span class="arr">&#8594;</span> CV Coaching Roadmap</a></li>
    </ul>
  </div>

  <div class="toc-card">
    <h2>&#128187; Programming</h2>
    <ul>
      <li><a href="/contents/public/CPP/"><span class="arr">&#8594;</span> C++ Reference</a></li>
      <li><a href="/contents/public/Python/"><span class="arr">&#8594;</span> Python Config</a></li>
      <li><a href="/contents/public/setup/"><span class="arr">&#8594;</span> Developer Tools</a></li>
    </ul>
  </div>

</div>
