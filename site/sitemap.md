---
layout: farshid_default
title: "Sitemap — All Pages"
permalink: /notes/sitemap/
---

<style>
.sitemap-hero {
  text-align: center;
  padding: 48px 24px 32px;
  margin-bottom: 32px;
}
.sitemap-hero h1 {
  font-size: 2.4rem;
  background: linear-gradient(135deg, #22D3EE, #06B6D4, #0284C7);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 8px;
}
.sitemap-hero p {
  color: var(--text-muted);
  font-size: 1.1rem;
}

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

.section-icon {
  font-size: 2rem;
  margin-bottom: 12px;
  display: block;
}

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
  background: rgba(34, 211, 238,0.2);
  color: #22D3EE;
  padding: 2px 8px;
  border-radius: 20px;
  font-weight: 600;
}

.sitemap-links {
  list-style: none;
  padding: 0;
  margin: 0;
}

.sitemap-links li {
  margin-bottom: 6px;
}

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
  background: rgba(34, 211, 238,0.12);
  border-color: rgba(34, 211, 238,0.3);
  transform: translateX(4px);
}
.sitemap-links a .link-arrow {
  opacity: 0;
  transition: opacity 0.2s ease;
  font-size: 0.8rem;
  color: #22D3EE;
}
.sitemap-links a:hover .link-arrow {
  opacity: 1;
}

.sitemap-search {
  max-width: 500px;
  margin: 0 auto 40px;
  text-align: center;
}
.sitemap-search input {
  width: 100%;
  padding: 14px 20px 14px 44px;
  font-size: 16px;
  border: 1px solid rgba(255,255,255,0.3);
  border-radius: 14px;
  background: rgba(255,255,255,0.12);
  color: var(--text);
  outline: none;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  box-sizing: border-box;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}
.sitemap-search input:focus {
  border-color: #22D3EE;
  box-shadow: 0 0 0 3px rgba(34, 211, 238,0.15);
}
.sitemap-search input::placeholder { color: var(--text-muted); }
.sitemap-search .search-icon {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-muted);
  font-size: 1.1rem;
}

.stats-bar {
  display: flex;
  justify-content: center;
  gap: 32px;
  margin-bottom: 40px;
  flex-wrap: wrap;
}
.stat-item {
  text-align: center;
}
.stat-num {
  font-size: 2rem;
  font-weight: 800;
  background: linear-gradient(135deg, #22D3EE, #06B6D4);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.stat-label {
  font-size: 0.8rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

@media (max-width: 768px) {
  .sitemap-grid { grid-template-columns: 1fr; padding: 0 8px; }
  .sitemap-hero h1 { font-size: 1.8rem; }
  .stats-bar { gap: 16px; }
}
</style>

<div class="sitemap-hero">
  <h1>Sitemap</h1>
  <p>Navigate through all pages on pirahansiah.com</p>
</div>

<div class="sitemap-search" style="position:relative;">
  <span class="search-icon">&#128269;</span>
  <input type="text" id="sitemap-filter" placeholder="Filter pages..." oninput="filterSitemap(this.value)">
</div>

<div class="stats-bar">
  <div class="stat-item"><div class="stat-num">{{ site.pages | size }}</div><div class="stat-label">Pages</div></div>
  <div class="stat-item"><div class="stat-num">3</div><div class="stat-label">Patents</div></div>
  <div class="stat-item"><div class="stat-num">6</div><div class="stat-label">Journals</div></div>
  <div class="stat-item"><div class="stat-num">11</div><div class="stat-label">Papers</div></div>
</div>

<div class="sitemap-grid" id="sitemap-grid">

  <!-- Home -->
  <div class="sitemap-section" data-section="home">
    <span class="section-icon">&#127968;</span>
    <div class="section-title">Home <span class="badge">Landing</span></div>
    <ul class="sitemap-links">
      <li><a href="/"><span class="link-arrow">&#8594;</span> Dr. Farshid Pirahansiah</a></li>
    </ul>
  </div>

  <!-- Computer Vision -->
  <div class="sitemap-section" data-section="cv">
    <span class="section-icon">&#128065;</span>
    <div class="section-title">Computer Vision <span class="badge">AI</span></div>
    <ul class="sitemap-links">
      <li><a href="/notes/docs/cv/3d/"><span class="link-arrow">&#8594;</span> 3D Vision & Multi-Camera</a></li>
      <li><a href="/notes/docs/cv/optical-flow/"><span class="link-arrow">&#8594;</span> Optical Flow</a></li>
      <li><a href="/notes/docs/cv/multi-camera/"><span class="link-arrow">&#8594;</span> Multi-Camera Systems</a></li>
      <li><a href="/notes/docs/coaching/"><span class="link-arrow">&#8594;</span> CV Coaching Roadmap</a></li>
    </ul>
  </div>

  <!-- AI & LLMs -->
  <div class="sitemap-section" data-section="ai">
    <span class="section-icon">&#129302;</span>
    <div class="section-title">AI & LLMs <span class="badge">New</span></div>
    <ul class="sitemap-links">
      <li><a href="/notes/docs/llm/llm-concepts/"><span class="link-arrow">&#8594;</span> Advanced LLM Concepts</a></li>
      <li><a href="/notes/docs/llm/agents/"><span class="link-arrow">&#8594;</span> Orchestrating AI Agents</a></li>
      <li><a href="/notes/docs/llm/blog/"><span class="link-arrow">&#8594;</span> Blog: AI & LLMs</a></li>
      <li><a href="/notes/docs/llm/avatar/"><span class="link-arrow">&#8594;</span> Avatar Generator</a></li>
    </ul>
  </div>

  <!-- CUDA & GPU -->
  <div class="sitemap-section" data-section="cuda">
    <span class="section-icon">&#9889;</span>
    <div class="section-title">CUDA & GPU <span class="badge">Dev</span></div>
    <ul class="sitemap-links">
      <li><a href="/notes/docs/cuda/numba/"><span class="link-arrow">&#8594;</span> Numba JIT Tutorial</a></li>
      <li><a href="/notes/docs/cuda/pycuda/"><span class="link-arrow">&#8594;</span> PyCUDA Kernels</a></li>
      <li><a href="/notes/docs/cuda/cuda-vscode/"><span class="link-arrow">&#8594;</span> CUDA in VS Code</a></li>
      <li><a href="/notes/docs/cuda/apple-ml/"><span class="link-arrow">&#8594;</span> MLX, CoreML & Metal</a></li>
    </ul>
  </div>

  <!-- Programming -->
  <div class="sitemap-section" data-section="prog">
    <span class="section-icon">&#128187;</span>
    <div class="section-title">Programming <span class="badge">Tools</span></div>
    <ul class="sitemap-links">
      <li><a href="/notes/docs/cpp/"><span class="link-arrow">&#8594;</span> C++ Quick Reference</a></li>
      <li><a href="/notes/docs/python/"><span class="link-arrow">&#8594;</span> Python Configuration</a></li>
      <li><a href="/notes/docs/dev-tools/"><span class="link-arrow">&#8594;</span> Developer Tools & Setup</a></li>
      <li><a href="/notes/docs/shell-vim/"><span class="link-arrow">&#8594;</span> Shell & Vim Reference</a></li>
    </ul>
  </div>

  <!-- Optimization -->
  <div class="sitemap-section" data-section="opt">
    <span class="section-icon">&#9889;</span>
    <div class="section-title">Optimization <span class="badge">ML</span></div>
    <ul class="sitemap-links">
      <li><a href="/notes/docs/optimization/"><span class="link-arrow">&#8594;</span> CV, DL & ML Optimization</a></li>
      <li><a href="/notes/docs/prompts/"><span class="link-arrow">&#8594;</span> Prompt Engineering</a></li>
    </ul>
  </div>

  <!-- Business -->
  <div class="sitemap-section" data-section="biz">
    <span class="section-icon">&#128640;</span>
    <div class="section-title">Business & Career</div>
    <ul class="sitemap-links">
      <li><a href="/notes/docs/startup/"><span class="link-arrow">&#8594;</span> Startup Guide</a></li>
      <li><a href="/notes/docs/seo/"><span class="link-arrow">&#8594;</span> SEO for LLMs</a></li>
      <li><a href="/notes/docs/linkedin/"><span class="link-arrow">&#8594;</span> Top LinkedIn Posts 2024</a></li>
    </ul>
  </div>

  <!-- Resources -->
  <div class="sitemap-section" data-section="res">
    <span class="section-icon">&#128218;</span>
    <div class="section-title">Resources</div>
    <ul class="sitemap-links">
      <li><a href="/notes/docs/resources/"><span class="link-arrow">&#8594;</span> Portfolio & Publications</a></li>
      <li><a href="/notes/docs/links/"><span class="link-arrow">&#8594;</span> Curated Links</a></li>
      <li><a href="/notes/docs/"><span class="link-arrow">&#8594;</span> Content Hub</a></li>
    </ul>
  </div>

  <!-- Patents -->
  <div class="sitemap-section" data-section="patents">
    <span class="section-icon">&#128220;</span>
    <div class="section-title">Patents <span class="badge">3</span></div>
    <ul class="sitemap-links">
      <li><a href="/notes/pubs/patents/"><span class="link-arrow">&#8594;</span> All Patents</a></li>
      <li><a href="/notes/pubs/patents/face-augmentation/"><span class="link-arrow">&#8594;</span> Face Image Augmentation</a></li>
      <li><a href="/notes/pubs/patents/vehicle-detection/"><span class="link-arrow">&#8594;</span> Vehicle Detection</a></li>
      <li><a href="/notes/pubs/patents/facial-analysis/"><span class="link-arrow">&#8594;</span> Facial Analysis Advertising</a></li>
    </ul>
  </div>

  <!-- Journals -->
  <div class="sitemap-section" data-section="journals">
    <span class="section-icon">&#128196;</span>
    <div class="section-title">Journal Articles <span class="badge">6</span></div>
    <ul class="sitemap-links">
      <li><a href="/notes/pubs/journals/"><span class="link-arrow">&#8594;</span> All Journals</a></li>
      <li><a href="/notes/pubs/journals/adaptive-thresholding/"><span class="link-arrow">&#8594;</span> Adaptive Thresholding PSNR</a></li>
      <li><a href="/notes/pubs/journals/fuzzy-thresholding/"><span class="link-arrow">&#8594;</span> GSFT-PSNR Fuzzy Threshold</a></li>
      <li><a href="/notes/pubs/journals/psnr-segmentation/"><span class="link-arrow">&#8594;</span> PSNR Threshold Segmentation</a></li>
      <li><a href="/notes/pubs/journals/character-recognition/"><span class="link-arrow">&#8594;</span> Character & Object Recognition</a></li>
      <li><a href="/notes/pubs/journals/slam-humanoid/"><span class="link-arrow">&#8594;</span> 3D SLAM & Humanoid Robots</a></li>
      <li><a href="/notes/pubs/journals/ant-colony/"><span class="link-arrow">&#8594;</span> Ant Colony Optimization</a></li>
    </ul>
  </div>

  <!-- Papers -->
  <div class="sitemap-section" data-section="papers">
    <span class="section-icon">&#128197;</span>
    <div class="section-title">Conference Papers <span class="badge">11</span></div>
    <ul class="sitemap-links">
      <li><a href="/notes/pubs/papers/"><span class="link-arrow">&#8594;</span> All Papers</a></li>
      <li><a href="/notes/pubs/papers/adaptive-segmentation/"><span class="link-arrow">&#8594;</span> Adaptive Segmentation PSNR</a></li>
      <li><a href="/notes/pubs/papers/license-plate/"><span class="link-arrow">&#8594;</span> License Plate — Entropy</a></li>
      <li><a href="/notes/pubs/papers/multi-threshold-plate/"><span class="link-arrow">&#8594;</span> Multi-threshold License Plate</a></li>
      <li><a href="/notes/pubs/papers/handwritten-thresholding/"><span class="link-arrow">&#8594;</span> Thresholding Handwritten</a></li>
      <li><a href="/notes/pubs/papers/multimodal-calibration/"><span class="link-arrow">&#8594;</span> Camera Calibration Multi-Modal</a></li>
      <li><a href="/notes/pubs/papers/pattern-calibration/"><span class="link-arrow">&#8594;</span> Pattern Image Calibration</a></li>
      <li><a href="/notes/pubs/papers/2d-3d-mapping/"><span class="link-arrow">&#8594;</span> 2D vs 3D Map Movement</a></li>
      <li><a href="/notes/pubs/papers/global-feature-recognition/"><span class="link-arrow">&#8594;</span> Character Recognition</a></li>
      <li><a href="/notes/pubs/papers/geometrical-topological/"><span class="link-arrow">&#8594;</span> Classification Geometrical</a></li>
      <li><a href="/notes/pubs/papers/grid-computing/"><span class="link-arrow">&#8594;</span> TafreshGrid Grid Computing</a></li>
    </ul>
  </div>

  <!-- Books -->
  <div class="sitemap-section" data-section="books">
    <span class="section-icon">&#128214;</span>
    <div class="section-title">Books & Chapters <span class="badge">7</span></div>
    <ul class="sitemap-links">
      <li><a href="/notes/pubs/books/"><span class="link-arrow">&#8594;</span> All Books</a></li>
      <li><a href="/notes/pubs/books/computational-intelligence/"><span class="link-arrow">&#8594;</span> Optical Flow for Video Stabilization</a></li>
      <li><a href="/notes/pubs/books/camera-calibration/"><span class="link-arrow">&#8594;</span> Camera Calibration for Robotics</a></li>
      <li><a href="/notes/pubs/books/ai/cv-meets-llm/"><span class="link-arrow">&#8594;</span> Computer Vision Meets LLM</a></li>
      <li><a href="/notes/pubs/books/ai/opencv5-ch1/"><span class="link-arrow">&#8594;</span> OpenCV 5 — Ch.1 Image Basics</a></li>
      <li><a href="/notes/pubs/books/ai/opencv5-ch2/"><span class="link-arrow">&#8594;</span> OpenCV 5 — Ch.2 Feature Detection</a></li>
      <li><a href="/notes/pubs/books/ai/opencv5-ch3/"><span class="link-arrow">&#8594;</span> OpenCV 5 — Ch.3 Advanced Topics</a></li>
    </ul>
  </div>

  <!-- Keynotes -->
  <div class="sitemap-section" data-section="keynotes">
    <span class="section-icon">&#127908;</span>
    <div class="section-title">Keynotes</div>
    <ul class="sitemap-links">
      <li><a href="/notes/pubs/keynotes/"><span class="link-arrow">&#8594;</span> All Keynotes</a></li>
      <li><a href="/notes/pubs/keynotes/llm-cv/"><span class="link-arrow">&#8594;</span> LLMs Meet Computer Vision</a></li>
    </ul>
  </div>

  <!-- Tiziran Courses -->
  <div class="sitemap-section" data-section="ai2026">
    <span class="section-icon">&#128218;</span>
    <div class="section-title">Courses & Workshops <span class="badge">AI 2026</span></div>
    <ul class="sitemap-links">
      <li><a href="/notes/courses/ml-spec/"><span class="link-arrow">&#8594;</span> ML Specialization</a></li>
      <li><a href="/notes/courses/fsdl/"><span class="link-arrow">&#8594;</span> Full Stack Deep Learning</a></li>
      <li><a href="/notes/courses/fsdl-2022/"><span class="link-arrow">&#8594;</span> FSDL 2022</a></li>
      <li><a href="/notes/courses/mlops/"><span class="link-arrow">&#8594;</span> MLOps</a></li>
      <li><a href="/notes/courses/ros/"><span class="link-arrow">&#8594;</span> ROS</a></li>
      <li><a href="/notes/courses/parallel/"><span class="link-arrow">&#8594;</span> Parallel Programming</a></li>
      <li><a href="/notes/courses/modern-cpp/"><span class="link-arrow">&#8594;</span> Modern C++</a></li>
      <li><a href="/notes/courses/cloud-native/"><span class="link-arrow">&#8594;</span> Cloud-Native</a></li>
      <li><a href="/notes/courses/tf-deploy/"><span class="link-arrow">&#8594;</span> TensorFlow Deployment</a></li>
      <li><a href="/notes/courses/risc-v/"><span class="link-arrow">&#8594;</span> RISC-V</a></li>
      <li><a href="/notes/courses/edge-ai-summit/"><span class="link-arrow">&#8594;</span> Edge AI Summit</a></li>
      <li><a href="/notes/courses/iot/"><span class="link-arrow">&#8594;</span> Embedded IoT</a></li>
      <li><a href="/notes/courses/tesla/"><span class="link-arrow">&#8594;</span> Tesla AI</a></li>
      <li><a href="/notes/courses/ai-hardware/"><span class="link-arrow">&#8594;</span> AI Hardware</a></li>
      <li><a href="/notes/courses/openvino/"><span class="link-arrow">&#8594;</span> OpenVINO</a></li>
      <li><a href="/notes/courses/metaverse/"><span class="link-arrow">&#8594;</span> Metaverse</a></li>
      <li><a href="/notes/courses/book-summary/"><span class="link-arrow">&#8594;</span> Book Summaries</a></li>
      <li><a href="/notes/courses/iot-scholarship/"><span class="link-arrow">&#8594;</span> IoT Scholarship</a></li>
      <li><a href="/notes/courses/"><span class="link-arrow">&#8594;</span> All Topics</a></li>
    </ul>
  </div>

</div>

<script>
function filterSitemap(query) {
  const q = query.toLowerCase();
  document.querySelectorAll('.sitemap-section').forEach(section => {
    const text = section.textContent.toLowerCase();
    section.style.display = text.includes(q) ? '' : 'none';
  });
}

document.addEventListener('DOMContentLoaded', () => {
  const sections = document.querySelectorAll('.sitemap-section');
  sections.forEach((s, i) => {
    s.style.opacity = '0';
    s.style.transform = 'translateY(20px)';
    setTimeout(() => {
      s.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
      s.style.opacity = '1';
      s.style.transform = 'translateY(0)';
    }, i * 60);
  });
});
</script>
