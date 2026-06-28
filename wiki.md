---
layout: farshid_default
title: "wiki page of my website for All Pages"
---

<style>
.sitemap-hero {
  text-align: center;
  padding: 48px 24px 32px;
  margin-bottom: 32px;
}
.sitemap-hero h1 {
  font-size: 2.4rem;
  background: linear-gradient(135deg, #0a84ff, #bf5af2, #ff375f);
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
  border-color: #0a84ff;
  box-shadow: 0 0 0 3px rgba(10,132,255,0.15);
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
  background: linear-gradient(135deg, #0a84ff, #5ac8fa);
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
  <h1>All Pages</h1>
  <p>Navigate through every page on pirahansiah.com</p>
</div>

<div class="sitemap-search" style="position:relative;">
  <span class="search-icon">&#128269;</span>
  <input type="text" id="sitemap-filter" placeholder="Filter pages..." oninput="filterSitemap(this.value)">
</div>

<div class="stats-bar">
  <div class="stat-item"><div class="stat-num">{{ site.pages | size }}</div><div class="stat-label">Pages</div></div>
  <div class="stat-item"><div class="stat-num">3</div><div class="stat-label">Patents</div></div>
  <div class="stat-item"><div class="stat-num">6</div><div class="stat-label">Journals</div></div>
  <div class="stat-item"><div class="stat-num">12</div><div class="stat-label">Papers</div></div>
  <div class="stat-item"><div class="stat-num">8</div><div class="stat-label">Books</div></div>
</div>

<div class="sitemap-grid" id="sitemap-grid">

  <!-- Home -->
  <div class="sitemap-section" data-section="home">
    <span class="section-icon">&#127968;</span>
    <div class="section-title">Home <span class="badge">Landing</span></div>
    <ul class="sitemap-links">
      <li><a href="/"><span class="link-arrow">&#8594;</span> Dr. Farshid Pirahansiah</a></li>
      <li><a href="/contents/public/enter/"><span class="link-arrow">&#8594;</span> Computer Vision (Legacy Home)</a></li>
    </ul>
  </div>

  <!-- Portfolio & Navigation -->
  <div class="sitemap-section" data-section="nav">
    <span class="section-icon">&#128195;</span>
    <div class="section-title">Portfolio & Navigation <span class="badge">Hub</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/public/product/"><span class="link-arrow">&#8594;</span> Product — Embedded CV & Edge AI</a></li>
      <li><a href="/contents/public/research/"><span class="link-arrow">&#8594;</span> Research — Publications & Patents</a></li>
      <li><a href="/contents/public/solutions/"><span class="link-arrow">&#8594;</span> Solutions — How I Help Businesses</a></li>
      <li><a href="/contents/public/projects/Solutions/"><span class="link-arrow">&#8594;</span> Solutions (Mind Map)</a></li>
      <li><a href="/contents/public/Resources/"><span class="link-arrow">&#8594;</span> Portfolio & Resources</a></li>
      <li><a href="/contents/public/index/"><span class="link-arrow">&#8594;</span> Content Hub</a></li>
      <li><a href="/contents/public/links/"><span class="link-arrow">&#8594;</span> Curated Links & Resources</a></li>
    </ul>
  </div>

  <!-- Computer Vision -->
  <div class="sitemap-section" data-section="cv">
    <span class="section-icon">&#128065;</span>
    <div class="section-title">Computer Vision <span class="badge">AI</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/public/cv/3d/"><span class="link-arrow">&#8594;</span> 3D Vision & Real-Time Multi-Camera Systems</a></li>
      <li><a href="/contents/public/cv/optical-flow/"><span class="link-arrow">&#8594;</span> Optical Flow: Challenges and Solutions</a></li>
      <li><a href="/contents/public/cv/multi-camera-systems/"><span class="link-arrow">&#8594;</span> Real-Time Multi-Camera Vision Systems</a></li>
      <li><a href="/contents/public/coaching/"><span class="link-arrow">&#8594;</span> CV Coaching & Teaching Roadmap</a></li>
    </ul>
  </div>

  <!-- AI & LLMs -->
  <div class="sitemap-section" data-section="ai">
    <span class="section-icon">&#129302;</span>
    <div class="section-title">AI & LLMs <span class="badge">New</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/public/ai-llm/advanced-llm-concepts/"><span class="link-arrow">&#8594;</span> Mind Map: Advanced LLM Concepts</a></li>
      <li><a href="/contents/public/ai-llm/orchestrating-agents/"><span class="link-arrow">&#8594;</span> Mind Map: Orchestrating AI Agents</a></li>
      <li><a href="/contents/public/ai-llm/blog/"><span class="link-arrow">&#8594;</span> Blog: AI, LLMs, and Computer Vision</a></li>
      <li><a href="/contents/public/ai-llm/avatar-generator/"><span class="link-arrow">&#8594;</span> Local Video Avatar Generator with Ollama</a></li>
    </ul>
  </div>

  <!-- CUDA & GPU -->
  <div class="sitemap-section" data-section="cuda">
    <span class="section-icon">&#9889;</span>
    <div class="section-title">CUDA & GPU <span class="badge">Dev</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/public/cuda-gpu/numba-jit/"><span class="link-arrow">&#8594;</span> Accelerate Python with Numba's @jit</a></li>
      <li><a href="/contents/public/cuda-gpu/pycuda-kernels/"><span class="link-arrow">&#8594;</span> How PyCUDA Reads and Runs C Kernels</a></li>
      <li><a href="/contents/public/cuda-gpu/vscode-cuda-windows/"><span class="link-arrow">&#8594;</span> CUDA Dev Environment in VS Code on Windows</a></li>
      <li><a href="/contents/public/cuda-gpu/mlx-coreml-metal/"><span class="link-arrow">&#8594;</span> MLX, CoreML, and Metal for Apple Silicon</a></li>
    </ul>
  </div>

  <!-- Programming -->
  <div class="sitemap-section" data-section="prog">
    <span class="section-icon">&#128187;</span>
    <div class="section-title">Programming <span class="badge">Tools</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/public/CPP/"><span class="link-arrow">&#8594;</span> C++ Quick Reference: Memory, Data Structures & Tools</a></li>
      <li><a href="/contents/public/Python/"><span class="link-arrow">&#8594;</span> Python Configuration Management & Tips</a></li>
      <li><a href="/contents/public/setup/"><span class="link-arrow">&#8594;</span> Developer Tools, Shell & Setup Tips</a></li>
      <li><a href="/contents/public/shell-vim-quickref/"><span class="link-arrow">&#8594;</span> Shell, Vim & Developer Tools Quick Reference</a></li>
      <li><a href="/contents/public/python/"><span class="link-arrow">&#8594;</span> Python Config (Mind Map)</a></li>
    </ul>
  </div>

  <!-- Optimization -->
  <div class="sitemap-section" data-section="opt">
    <span class="section-icon">&#128200;</span>
    <div class="section-title">Optimization <span class="badge">ML</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/public/Optimization/"><span class="link-arrow">&#8594;</span> Optimization of CV, DL, and ML Systems</a></li>
      <li><a href="/contents/public/optimization/"><span class="link-arrow">&#8594;</span> Optimization (Mind Map)</a></li>
      <li><a href="/contents/public/Prompts/"><span class="link-arrow">&#8594;</span> Prompt Engineering Templates</a></li>
      <li><a href="/contents/public/prompts/"><span class="link-arrow">&#8594;</span> Prompts (Mind Map)</a></li>
    </ul>
  </div>

  <!-- Business -->
  <div class="sitemap-section" data-section="biz">
    <span class="section-icon">&#128640;</span>
    <div class="section-title">Business & Career</div>
    <ul class="sitemap-links">
      <li><a href="/contents/public/StartUp/"><span class="link-arrow">&#8594;</span> Startup Guide: Edge AI Business, Fundraising & Strategy in Germany</a></li>
      <li><a href="/contents/public/SEO/"><span class="link-arrow">&#8594;</span> The New Era of SEO: Optimizing for LLMs</a></li>
      <li><a href="/contents/public/seo/"><span class="link-arrow">&#8594;</span> SEO for LLMs (Mind Map)</a></li>
      <li><a href="/contents/public/linkedin-top-posts/"><span class="link-arrow">&#8594;</span> My Top LinkedIn Posts of 2024</a></li>
    </ul>
  </div>

  <!-- PKM & Knowledge -->
  <div class="sitemap-section" data-section="pkm">
    <span class="section-icon">&#128218;</span>
    <div class="section-title">PKM & Knowledge</div>
    <ul class="sitemap-links">
      <li><a href="/contents/pkm/AboutMe/"><span class="link-arrow">&#8594;</span> Dr. Farshid Pirahansiah — AI & Computer Vision Engineer</a></li>
      <li><a href="/contents/pkm/use-cases/"><span class="link-arrow">&#8594;</span> Complete Portfolio</a></li>
      <li><a href="/contents/pkm/proof/"><span class="link-arrow">&#8594;</span> All Links — pirahansiah.com</a></li>
      <li><a href="/contents/pkm/links/"><span class="link-arrow">&#8594;</span> Use Cases</a></li>
      <li><a href="/contents/pkm/TOC/"><span class="link-arrow">&#8594;</span> Data & DevOps</a></li>
      <li><a href="/contents/pkm/graph/"><span class="link-arrow">&#8594;</span> AI Knowledge Graph</a></li>
    </ul>
  </div>

  <!-- Publications Overview -->
  <div class="sitemap-section" data-section="pub-overview">
    <span class="section-icon">&#128196;</span>
    <div class="section-title">Publications Overview</div>
    <ul class="sitemap-links">
      <li><a href="/contents/publications/CV/"><span class="link-arrow">&#8594;</span> Curriculum Vitae — Dr. Farshid Pirahansiah</a></li>
      <li><a href="/contents/publications/10Years/"><span class="link-arrow">&#8594;</span> Lessons from 10 Years of Fixing Bugs in CV</a></li>
    </ul>
  </div>

  <!-- Patents -->
  <div class="sitemap-section" data-section="patents">
    <span class="section-icon">&#128220;</span>
    <div class="section-title">Patents <span class="badge">3</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/publications/Patents/"><span class="link-arrow">&#8594;</span> All Patents</a></li>
      <li><a href="/contents/publications/Patents/face-image-augmentation/"><span class="link-arrow">&#8594;</span> Face Image Augmentation</a></li>
      <li><a href="/contents/publications/Patents/vehicle-detection/"><span class="link-arrow">&#8594;</span> Vehicle Detection</a></li>
      <li><a href="/contents/publications/Patents/facial-analysis-advertisement/"><span class="link-arrow">&#8594;</span> Facial Analysis for Advertising</a></li>
    </ul>
  </div>

  <!-- Journals -->
  <div class="sitemap-section" data-section="journals">
    <span class="section-icon">&#128196;</span>
    <div class="section-title">Journal Articles <span class="badge">6</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/publications/Journals/"><span class="link-arrow">&#8594;</span> All Journals</a></li>
      <li><a href="/contents/publications/Journals/adaptive-thresholding-psnr/"><span class="link-arrow">&#8594;</span> Adaptive Thresholding PSNR</a></li>
      <li><a href="/contents/publications/Journals/gsft-psnr-fuzzy-threshold/"><span class="link-arrow">&#8594;</span> GSFT-PSNR Fuzzy Threshold</a></li>
      <li><a href="/contents/publications/Journals/psnr-threshold-segmentation/"><span class="link-arrow">&#8594;</span> PSNR Threshold Segmentation</a></li>
      <li><a href="/contents/publications/Journals/character-object-recognition/"><span class="link-arrow">&#8594;</span> Character & Object Recognition</a></li>
      <li><a href="/contents/publications/Journals/3d-slam-humanoid-robots/"><span class="link-arrow">&#8594;</span> 3D SLAM & Humanoid Robots</a></li>
      <li><a href="/contents/publications/Journals/ant-colony-optimization/"><span class="link-arrow">&#8594;</span> Ant Colony Optimization</a></li>
    </ul>
  </div>

  <!-- Papers -->
  <div class="sitemap-section" data-section="papers">
    <span class="section-icon">&#128197;</span>
    <div class="section-title">Conference Papers <span class="badge">12</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/publications/Papers/"><span class="link-arrow">&#8594;</span> All Papers</a></li>
      <li><a href="/contents/publications/Papers/adaptive-image-segmentation-psnr/"><span class="link-arrow">&#8594;</span> Adaptive Segmentation PSNR</a></li>
      <li><a href="/contents/publications/Papers/license-plate-recognition-entropy/"><span class="link-arrow">&#8594;</span> License Plate — Entropy</a></li>
      <li><a href="/contents/publications/Papers/multi-threshold-license-plate/"><span class="link-arrow">&#8594;</span> Multi-threshold License Plate</a></li>
      <li><a href="/contents/publications/Papers/comparison-thresholding-handwritten/"><span class="link-arrow">&#8594;</span> Thresholding Handwritten</a></li>
      <li><a href="/contents/publications/Papers/camera-calibration-multi-modal/"><span class="link-arrow">&#8594;</span> Camera Calibration Multi-Modal</a></li>
      <li><a href="/contents/publications/Papers/pattern-image-calibration/"><span class="link-arrow">&#8594;</span> Pattern Image Calibration</a></li>
      <li><a href="/contents/publications/Papers/2d-3d-map-movement/"><span class="link-arrow">&#8594;</span> 2D vs 3D Map Movement</a></li>
      <li><a href="/contents/publications/Papers/character-recognition-global-feature/"><span class="link-arrow">&#8594;</span> Character Recognition Global Feature</a></li>
      <li><a href="/contents/publications/Papers/classification-geometrical-topological/"><span class="link-arrow">&#8594;</span> Classification Geometrical</a></li>
      <li><a href="/contents/publications/Papers/tafreshgrid-grid-computing/"><span class="link-arrow">&#8594;</span> TafreshGrid Grid Computing</a></li>
      <li><a href="/contents/publications/Papers/My_Conference_Paper/"><span class="link-arrow">&#8594;</span> My Conference Paper</a></li>
    </ul>
  </div>

  <!-- Books -->
  <div class="sitemap-section" data-section="books">
    <span class="section-icon">&#128214;</span>
    <div class="section-title">Books & Chapters <span class="badge">8</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/publications/Books/"><span class="link-arrow">&#8594;</span> All Books</a></li>
      <li><a href="/contents/publications/Books/computational-intelligence-optical-flow/"><span class="link-arrow">&#8594;</span> Optical Flow for Video Stabilization</a></li>
      <li><a href="/contents/publications/Books/camera-calibration-video-stabilization/"><span class="link-arrow">&#8594;</span> Camera Calibration for Robotics</a></li>
      <li><a href="/contents/publications/Books/AI/computer-vision-meets-llm/"><span class="link-arrow">&#8594;</span> Computer Vision Meets LLM — Book 2025</a></li>
      <li><a href="/contents/publications/Books/AI/opencv5-chapter0-introduction/"><span class="link-arrow">&#8594;</span> OpenCV 5 — Chapter 0: Introduction</a></li>
      <li><a href="/contents/publications/Books/AI/opencv5-chapter1-image-basics/"><span class="link-arrow">&#8594;</span> OpenCV 5 — Chapter 1: Image Basics</a></li>
      <li><a href="/contents/publications/Books/AI/opencv5-chapter2-feature-detection/"><span class="link-arrow">&#8594;</span> OpenCV 5 — Chapter 2: Feature Detection</a></li>
      <li><a href="/contents/publications/Books/AI/opencv5-chapter3-advanced/"><span class="link-arrow">&#8594;</span> OpenCV 5 — Chapter 3: Advanced Topics</a></li>
    </ul>
  </div>

  <!-- Keynotes -->
  <div class="sitemap-section" data-section="keynotes">
    <span class="section-icon">&#127908;</span>
    <div class="section-title">Keynotes</div>
    <ul class="sitemap-links">
      <li><a href="/contents/publications/Keynotes/"><span class="link-arrow">&#8594;</span> All Keynotes</a></li>
      <li><a href="/contents/publications/Keynotes/llms-meet-computer-vision/"><span class="link-arrow">&#8594;</span> LLMs Meet Computer Vision — Keynote</a></li>
    </ul>
  </div>

  <!-- AI 2026 Courses -->
  <div class="sitemap-section" data-section="courses">
    <span class="section-icon">&#128218;</span>
    <div class="section-title">Courses & Workshops <span class="badge">AI 2026</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/ai2026/topics/"><span class="link-arrow">&#8594;</span> Topics & Projects</a></li>
      <li><a href="/contents/ai2026/machine-learning-specialization/"><span class="link-arrow">&#8594;</span> Machine Learning Specialization</a></li>
      <li><a href="/contents/ai2026/full-stack-deep-learning/"><span class="link-arrow">&#8594;</span> Full Stack Deep Learning</a></li>
      <li><a href="/contents/ai2026/fsdl-2022/"><span class="link-arrow">&#8594;</span> Full Stack Deep Learning 2022</a></li>
      <li><a href="/contents/ai2026/mlops/"><span class="link-arrow">&#8594;</span> MLOps</a></li>
      <li><a href="/contents/ai2026/ros/"><span class="link-arrow">&#8594;</span> ROS — Robot Operating System</a></li>
      <li><a href="/contents/ai2026/parallel-programming/"><span class="link-arrow">&#8594;</span> Parallel Programming for Computer Vision</a></li>
      <li><a href="/contents/ai2026/modern-cpp/"><span class="link-arrow">&#8594;</span> Modern C++ for Image Processing</a></li>
      <li><a href="/contents/ai2026/cloud-native/"><span class="link-arrow">&#8594;</span> Cloud-Native Infrastructure with Kubernetes</a></li>
      <li><a href="/contents/ai2026/tensorflow-deployment/"><span class="link-arrow">&#8594;</span> TensorFlow: Data and Deployment Specialization</a></li>
      <li><a href="/contents/ai2026/risc-v/"><span class="link-arrow">&#8594;</span> RISC-V for AI</a></li>
      <li><a href="/contents/ai2026/edge-ai-summit/"><span class="link-arrow">&#8594;</span> Edge AI Summit 2020</a></li>
      <li><a href="/contents/ai2026/embedded-iot/"><span class="link-arrow">&#8594;</span> Embedded IoT</a></li>
      <li><a href="/contents/ai2026/tesla/"><span class="link-arrow">&#8594;</span> Tesla AI</a></li>
      <li><a href="/contents/ai2026/ai-hardware/"><span class="link-arrow">&#8594;</span> AI Hardware Accelerators</a></li>
      <li><a href="/contents/ai2026/openvino/"><span class="link-arrow">&#8594;</span> OpenVINO Deep Learning</a></li>
      <li><a href="/contents/ai2026/metaverse/"><span class="link-arrow">&#8594;</span> Metaverse & XR</a></li>
      <li><a href="/contents/ai2026/book-summary/"><span class="link-arrow">&#8594;</span> Book Summaries</a></li>
      <li><a href="/contents/ai2026/iot-scholarship/"><span class="link-arrow">&#8594;</span> IoT Scholarship Foundation</a></li>
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
