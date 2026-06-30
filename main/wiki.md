---
layout: farshid_default
title: "All Pages — pirahansiah.com"
permalink: /contents/wiki/
---

<style>
.wiki-wrap { max-width: 960px; margin: 0 auto; padding: 0 20px; font-family: -apple-system, 'Linux Libertine', Georgia, Times, serif; }
.wiki-title { font-size: 1.8rem; font-weight: 400; border-bottom: 1px solid var(--glass-border); padding-bottom: 8px; margin-bottom: 16px; color: var(--text); }
.wiki-sub { font-size: 0.85rem; color: var(--text-muted); margin-bottom: 20px; }
.wiki-toc { background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 8px; padding: 16px 20px; margin-bottom: 28px; display: inline-block; }
.wiki-toc-title { font-weight: 700; font-size: 0.95rem; margin-bottom: 8px; color: var(--text); }
.wiki-toc ol { margin: 0; padding-left: 20px; columns: 2; column-gap: 24px; }
.wiki-toc li { font-size: 0.85rem; margin-bottom: 4px; color: var(--text); }
.wiki-toc a { color: #0a84ff; text-decoration: none; }
.wiki-toc a:hover { text-decoration: underline; }
.wiki-section { margin-bottom: 28px; }
.wiki-section h2 { font-size: 1.25rem; font-weight: 400; border-bottom: 1px solid var(--glass-border); padding-bottom: 6px; margin-bottom: 12px; color: var(--text); }
.wiki-section h3 { font-size: 1.05rem; font-weight: 700; margin: 16px 0 8px; color: var(--text); }
.wiki-section p, .wiki-section li { font-size: 0.9rem; line-height: 1.6; color: var(--text); }
.wiki-section ul { padding-left: 22px; }
.wiki-section li { margin-bottom: 4px; }
.wiki-section a { color: #0a84ff; text-decoration: none; }
.wiki-section a:hover { text-decoration: underline; }
.wiki-cols { column-count: 2; column-gap: 28px; }
.wiki-cols li { break-inside: avoid; }
.wiki-badge { display: inline-block; font-size: 0.7rem; background: rgba(10,132,255,0.15); color: #0a84ff; padding: 1px 6px; border-radius: 4px; margin-left: 6px; vertical-align: middle; }
.wiki-search { margin-bottom: 24px; }
.wiki-search input { width: 100%; max-width: 400px; padding: 10px 14px; font-size: 0.9rem; border: 1px solid var(--glass-border); border-radius: 6px; background: var(--glass-bg); color: var(--text); outline: none; box-sizing: border-box; }
.wiki-search input:focus { border-color: #0a84ff; }
.wiki-search input::placeholder { color: var(--text-muted); }
.wiki-stat { display: inline-block; background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 6px; padding: 4px 10px; margin: 0 6px 6px 0; font-size: 0.8rem; color: var(--text); }
.wiki-stat strong { color: #0a84ff; }
@media (max-width: 600px) { .wiki-toc ol { columns: 1; } .wiki-cols { column-count: 1; } }
</style>

<div class="wiki-wrap">

  <h1 class="wiki-title">All Pages</h1>
  <p class="wiki-sub">From pirahansiah.com, the free knowledge base</p>

  <div class="wiki-search">
    <input type="text" id="wiki-filter" placeholder="Search pages..." oninput="filterWiki(this.value)">
  </div>

  <div>
    <span class="wiki-stat"><strong>{{ site.pages | size }}</strong> pages</span>
    <span class="wiki-stat"><strong>3</strong> patents</span>
    <span class="wiki-stat"><strong>6</strong> journals</span>
    <span class="wiki-stat"><strong>11</strong> papers</span>
    <span class="wiki-stat"><strong>7</strong> books</span>
    <span class="wiki-stat"><strong>19</strong> courses</span>
  </div>

  <div class="wiki-toc">
    <div class="wiki-toc-title">Contents</div>
    <ol>
      <li><a href="#home">Home</a></li>
      <li><a href="#computer-vision">Computer Vision</a></li>
      <li><a href="#ai-llm">AI &amp; LLMs</a></li>
      <li><a href="#cuda">CUDA &amp; GPU</a></li>
      <li><a href="#programming">Programming</a></li>
      <li><a href="#optimization">Optimization</a></li>
      <li><a href="#business">Business &amp; Career</a></li>
      <li><a href="#knowledge">PKM &amp; Knowledge</a></li>
      <li><a href="#patents">Patents</a></li>
      <li><a href="#journals">Journals</a></li>
      <li><a href="#papers">Conference Papers</a></li>
      <li><a href="#books">Books</a></li>
      <li><a href="#keynotes">Keynotes</a></li>
      <li><a href="#courses">Courses</a></li>
      <li><a href="#presentations">Presentations</a></li>
    </ol>
  </div>

  <div class="wiki-section" data-section="home">
    <h2 id="home">Home</h2>
    <ul>
      <li><a href="/">Dr. Farshid Pirahansiah</a> — Main landing page</li>
      <li><a href="/contents/public/enter/">Computer Vision</a> — CV overview and research</li>
    </ul>
  </div>

  <div class="wiki-section" data-section="cv">
    <h2 id="computer-vision">Computer Vision</h2>
    <ul class="wiki-cols">
      <li><a href="/contents/public/cv/3d/">3D Vision &amp; Multi-Camera Systems</a></li>
      <li><a href="/contents/public/cv/optical-flow/">Optical Flow</a> <span class="wiki-badge">AI</span></li>
      <li><a href="/contents/public/cv/multi-camera-systems/">Multi-Camera Systems</a></li>
      <li><a href="/contents/public/coaching/">CV Coaching Roadmap</a></li>
      <li><a href="/contents/public/product/">Product — Embedded CV &amp; Edge AI</a></li>
      <li><a href="/contents/public/enter/">Computer Vision Overview</a></li>
    </ul>
  </div>

  <div class="wiki-section" data-section="ai">
    <h2 id="ai-llm">AI &amp; LLMs</h2>
    <ul class="wiki-cols">
      <li><a href="/contents/public/ai-llm/advanced-llm-concepts/">Advanced LLM Concepts</a> <span class="wiki-badge">New</span></li>
      <li><a href="/contents/public/ai-llm/orchestrating-agents/">Orchestrating AI Agents</a></li>
      <li><a href="/contents/public/ai-llm/blog/">Blog: AI &amp; LLMs</a></li>
      <li><a href="/contents/public/ai-llm/avatar-generator/">Avatar Generator</a></li>
    </ul>
  </div>

  <div class="wiki-section" data-section="cuda">
    <h2 id="cuda">CUDA &amp; GPU</h2>
    <ul class="wiki-cols">
      <li><a href="/contents/public/cuda-gpu/numba-jit/">Numba JIT Tutorial</a></li>
      <li><a href="/contents/public/cuda-gpu/pycuda-kernels/">PyCUDA Kernels</a></li>
      <li><a href="/contents/public/cuda-gpu/vscode-cuda-windows/">CUDA in VS Code</a></li>
      <li><a href="/contents/public/cuda-gpu/mlx-coreml-metal/">MLX, CoreML &amp; Metal</a></li>
    </ul>
  </div>

  <div class="wiki-section" data-section="programming">
    <h2 id="programming">Programming</h2>
    <ul class="wiki-cols">
      <li><a href="/contents/public/CPP/">C++ Quick Reference</a></li>
      <li><a href="/contents/public/Python/">Python Configuration</a></li>
      <li><a href="/contents/public/setup/">Developer Tools &amp; Setup</a></li>
      <li><a href="/contents/public/shell-vim-quickref/">Shell &amp; Vim Reference</a></li>
    </ul>
  </div>

  <div class="wiki-section" data-section="optimization">
    <h2 id="optimization">Optimization</h2>
    <ul>
      <li><a href="/contents/public/Optimization/">CV, DL &amp; ML Optimization</a></li>
      <li><a href="/contents/public/Prompts/">Prompt Engineering</a></li>
    </ul>
  </div>

  <div class="wiki-section" data-section="business">
    <h2 id="business">Business &amp; Career</h2>
    <ul>
      <li><a href="/contents/public/StartUp/">Startup Guide</a> — Edge AI business in Germany</li>
      <li><a href="/contents/public/SEO/">SEO for LLMs</a></li>
      <li><a href="/contents/public/linkedin-top-posts/">Top LinkedIn Posts 2024</a></li>
    </ul>
  </div>

  <div class="wiki-section" data-section="knowledge">
    <h2 id="knowledge">PKM &amp; Knowledge</h2>
    <ul>
      <li><a href="/contents/public/index/">Content Hub</a></li>
      <li><a href="/contents/public/links/">Curated Links</a></li>
      <li><a href="/contents/pkm/use-cases/">Use Cases</a></li>
      <li><a href="/contents/pkm/links/">Links</a></li>
      <li><a href="/contents/pkm/proof/">Proof</a></li>
      <li><a href="/contents/pkm/TOC/">Table of Contents</a></li>
      <li><a href="/contents/public/Resources/">Portfolio &amp; Resources</a></li>
      <li><a href="/contents/sitemap/">Sitemap</a></li>
    </ul>
  </div>

  <div class="wiki-section" data-section="patents">
    <h2 id="patents">Patents</h2>
    <ul>
      <li><a href="/contents/publications/Patents/">All Patents</a> <span class="wiki-badge">3</span></li>
      <li><a href="/contents/publications/Patents/face-image-augmentation/">Face Image Augmentation</a></li>
      <li><a href="/contents/publications/Patents/vehicle-detection/">Vehicle Detection</a></li>
      <li><a href="/contents/publications/Patents/facial-analysis-advertisement/">Facial Analysis for Advertising</a></li>
    </ul>
  </div>

  <div class="wiki-section" data-section="journals">
    <h2 id="journals">Journal Articles</h2>
    <ul class="wiki-cols">
      <li><a href="/contents/publications/Journals/">All Journals</a> <span class="wiki-badge">6</span></li>
      <li><a href="/contents/publications/Journals/adaptive-thresholding-psnr/">Adaptive Thresholding PSNR</a></li>
      <li><a href="/contents/publications/Journals/gsft-psnr-fuzzy-threshold/">GSFT-PSNR Fuzzy Threshold</a></li>
      <li><a href="/contents/publications/Journals/psnr-threshold-segmentation/">PSNR Threshold Segmentation</a></li>
      <li><a href="/contents/publications/Journals/character-object-recognition/">Character &amp; Object Recognition</a></li>
      <li><a href="/contents/publications/Journals/3d-slam-humanoid-robots/">3D SLAM &amp; Humanoid Robots</a></li>
      <li><a href="/contents/publications/Journals/ant-colony-optimization/">Ant Colony Optimization</a></li>
    </ul>
  </div>

  <div class="wiki-section" data-section="papers">
    <h2 id="papers">Conference Papers</h2>
    <ul class="wiki-cols">
      <li><a href="/contents/publications/Papers/">All Papers</a> <span class="wiki-badge">11</span></li>
      <li><a href="/contents/publications/Papers/adaptive-image-segmentation-psnr/">Adaptive Segmentation PSNR</a></li>
      <li><a href="/contents/publications/Papers/license-plate-recognition-entropy/">License Plate — Entropy</a></li>
      <li><a href="/contents/publications/Papers/multi-threshold-license-plate/">Multi-threshold License Plate</a></li>
      <li><a href="/contents/publications/Papers/comparison-thresholding-handwritten/">Thresholding Handwritten</a></li>
      <li><a href="/contents/publications/Papers/camera-calibration-multi-modal/">Camera Calibration Multi-Modal</a></li>
      <li><a href="/contents/publications/Papers/pattern-image-calibration/">Pattern Image Calibration</a></li>
      <li><a href="/contents/publications/Papers/2d-3d-map-movement/">2D vs 3D Map Movement</a></li>
      <li><a href="/contents/publications/Papers/character-recognition-global-feature/">Character Recognition</a></li>
      <li><a href="/contents/publications/Papers/classification-geometrical-topological/">Classification Geometrical</a></li>
      <li><a href="/contents/publications/Papers/tafreshgrid-grid-computing/">TafreshGrid Grid Computing</a></li>
      <li><a href="/contents/publications/Papers/My_Conference_Paper/">Conference Paper on CV</a></li>
    </ul>
  </div>

  <div class="wiki-section" data-section="books">
    <h2 id="books">Books &amp; Chapters</h2>
    <ul class="wiki-cols">
      <li><a href="/contents/publications/Books/">All Books</a> <span class="wiki-badge">7</span></li>
      <li><a href="/contents/publications/Books/computational-intelligence-optical-flow/">Optical Flow for Video Stabilization</a></li>
      <li><a href="/contents/publications/Books/camera-calibration-video-stabilization/">Camera Calibration for Robotics</a></li>
      <li><a href="/contents/publications/Books/AI/computer-vision-meets-llm/">Computer Vision Meets LLM</a></li>
      <li><a href="/contents/publications/Books/AI/opencv5-chapter0-introduction/">OpenCV 5 — Ch.0 Introduction</a></li>
      <li><a href="/contents/publications/Books/AI/opencv5-chapter1-image-basics/">OpenCV 5 — Ch.1 Image Basics</a></li>
      <li><a href="/contents/publications/Books/AI/opencv5-chapter2-feature-detection/">OpenCV 5 — Ch.2 Feature Detection</a></li>
      <li><a href="/contents/publications/Books/AI/opencv5-chapter3-advanced/">OpenCV 5 — Ch.3 Advanced Topics</a></li>
    </ul>
  </div>

  <div class="wiki-section" data-section="keynotes">
    <h2 id="keynotes">Keynotes</h2>
    <ul>
      <li><a href="/contents/publications/Keynotes/">All Keynotes</a></li>
      <li><a href="/contents/publications/Keynotes/llms-meet-computer-vision/">LLMs Meet Computer Vision</a></li>
      <li><a href="/contents/publications/CV/">Curriculum Vitae</a></li>
      <li><a href="/contents/publications/10Years/">Lessons from 10 Years of Fixing Bugs</a></li>
    </ul>
  </div>

  <div class="wiki-section" data-section="courses">
    <h2 id="courses">Courses &amp; Workshops</h2>
    <ul class="wiki-cols">
      <li><a href="/contents/ai2026/topics/">All Topics</a></li>
      <li><a href="/contents/ai2026/machine-learning-specialization/">ML Specialization</a></li>
      <li><a href="/contents/ai2026/full-stack-deep-learning/">Full Stack Deep Learning</a></li>
      <li><a href="/contents/ai2026/mlops/">MLOps</a></li>
      <li><a href="/contents/ai2026/ros/">ROS</a></li>
      <li><a href="/contents/ai2026/parallel-programming/">Parallel Programming</a></li>
      <li><a href="/contents/ai2026/modern-cpp/">Modern C++</a></li>
      <li><a href="/contents/ai2026/cloud-native/">Cloud-Native</a></li>
      <li><a href="/contents/ai2026/tensorflow-deployment/">TensorFlow Deployment</a></li>
      <li><a href="/contents/ai2026/risc-v/">RISC-V</a></li>
      <li><a href="/contents/ai2026/edge-ai-summit/">Edge AI Summit</a></li>
      <li><a href="/contents/ai2026/embedded-iot/">Embedded IoT</a></li>
      <li><a href="/contents/ai2026/tesla/">Tesla AI</a></li>
      <li><a href="/contents/ai2026/ai-hardware/">AI Hardware</a></li>
      <li><a href="/contents/ai2026/openvino/">OpenVINO</a></li>
      <li><a href="/contents/ai2026/metaverse/">Metaverse</a></li>
      <li><a href="/contents/ai2026/book-summary/">Book Summaries</a></li>
      <li><a href="/contents/ai2026/iot-scholarship/">IoT Scholarship</a></li>
    </ul>
  </div>

  <div class="wiki-section" data-section="presentations">
    <h2 id="presentations">Presentations</h2>
    <ul>
      <li><a href="/contents/ppt/farshid-ai-cv-llm-presentation/">Reducing Token Usage in AI-Assisted Development</a></li>
    </ul>
  </div>

  <div style="border-top: 1px solid var(--glass-border); margin-top: 32px; padding-top: 12px; font-size: 0.8rem; color: var(--text-muted);">
    Content is available under the site terms. Last updated: June 2026.
  </div>

</div>

<script>
function filterWiki(q) {
  q = q.toLowerCase();
  document.querySelectorAll('.wiki-section').forEach(s => {
    s.style.display = s.textContent.toLowerCase().includes(q) ? '' : 'none';
  });
}
</script>
