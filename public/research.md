---
layout: farshid_default
title: "Research — Publications & Patents"
description: "Complete list of patents, journal articles, conference papers, books, and keynotes."
markmap: |
  # Research
  ## Patents (3)
  - Face Augmentation
  - Vehicle Detection
  - Facial Analysis Advertising
  ## Papers (11)
  - Camera Calibration
  - Image Segmentation
  - License Plate Recognition
  ## Journals (6)
  - Adaptive Thresholding
  - 3D SLAM
  - Ant Colony Optimization
  ## Books (7)
  - OpenCV 5 Chapters
  - Optical Flow
  - Camera Calibration
  ## Keynotes
  - LLMs Meet Computer Vision
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
  <h1>Research</h1>
  <p>3 patents, 2 books, 6 journals, 11 conference papers, 1 keynote</p>
</div>

<div style="text-align:center; padding: 0 16px;">
  <a href="/" class="back-link">&#8592; Home</a>
  <a href="/contents/public/product/" class="back-link">Product</a>
  <a href="/contents/public/solutions/" class="back-link">Solutions</a>
</div>

<div class="sitemap-grid">

  <div class="sitemap-section">
    <span class="section-icon">&#128220;</span>
    <div class="section-title">Patents <span class="badge">3</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/publications/Patents/face-image-augmentation/"><span class="link-arrow">&#8594;</span> Face Image Augmentation — WO 2021/060971</a></li>
      <li><a href="/contents/publications/Patents/vehicle-detection/"><span class="link-arrow">&#8594;</span> Vehicle Detection — WO 2021/107761</a></li>
      <li><a href="/contents/publications/Patents/facial-analysis-advertisement/"><span class="link-arrow">&#8594;</span> Facial Analysis Advertising — WO 2020/141969</a></li>
    </ul>
  </div>

  <div class="sitemap-section">
    <span class="section-icon">&#128197;</span>
    <div class="section-title">Conference Papers <span class="badge">11</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/publications/Papers/adaptive-image-segmentation-psnr/"><span class="link-arrow">&#8594;</span> Adaptive Segmentation PSNR</a></li>
      <li><a href="/contents/publications/Papers/license-plate-recognition-entropy/"><span class="link-arrow">&#8594;</span> License Plate — Entropy</a></li>
      <li><a href="/contents/publications/Papers/multi-threshold-license-plate/"><span class="link-arrow">&#8594;</span> Multi-threshold License Plate</a></li>
      <li><a href="/contents/publications/Papers/comparison-thresholding-handwritten/"><span class="link-arrow">&#8594;</span> Thresholding Handwritten</a></li>
      <li><a href="/contents/publications/Papers/camera-calibration-multi-modal/"><span class="link-arrow">&#8594;</span> Camera Calibration Multi-Modal</a></li>
      <li><a href="/contents/publications/Papers/pattern-image-calibration/"><span class="link-arrow">&#8594;</span> Pattern Image Calibration</a></li>
      <li><a href="/contents/publications/Papers/2d-3d-map-movement/"><span class="link-arrow">&#8594;</span> 2D vs 3D Map Movement</a></li>
      <li><a href="/contents/publications/Papers/character-recognition-global-feature/"><span class="link-arrow">&#8594;</span> Character Recognition</a></li>
      <li><a href="/contents/publications/Papers/classification-geometrical-topological/"><span class="link-arrow">&#8594;</span> Classification Geometrical</a></li>
      <li><a href="/contents/publications/Papers/tafreshgrid-grid-computing/"><span class="link-arrow">&#8594;</span> TafreshGrid</a></li>
      <li><a href="/contents/publications/Papers/"><span class="link-arrow">&#8594;</span> All Papers &#8594;</a></li>
    </ul>
  </div>

  <div class="sitemap-section">
    <span class="section-icon">&#128196;</span>
    <div class="section-title">Journal Articles <span class="badge">6</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/publications/Journals/adaptive-thresholding-psnr/"><span class="link-arrow">&#8594;</span> Adaptive Thresholding PSNR</a></li>
      <li><a href="/contents/publications/Journals/gsft-psnr-fuzzy-threshold/"><span class="link-arrow">&#8594;</span> GSFT-PSNR Fuzzy Threshold</a></li>
      <li><a href="/contents/publications/Journals/psnr-threshold-segmentation/"><span class="link-arrow">&#8594;</span> PSNR Threshold Segmentation</a></li>
      <li><a href="/contents/publications/Journals/character-object-recognition/"><span class="link-arrow">&#8594;</span> Character & Object Recognition</a></li>
      <li><a href="/contents/publications/Journals/3d-slam-humanoid-robots/"><span class="link-arrow">&#8594;</span> 3D SLAM & Humanoid Robots</a></li>
      <li><a href="/contents/publications/Journals/ant-colony-optimization/"><span class="link-arrow">&#8594;</span> Ant Colony Optimization</a></li>
    </ul>
  </div>

  <div class="sitemap-section">
    <span class="section-icon">&#128214;</span>
    <div class="section-title">Books & Chapters <span class="badge">7</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/publications/Books/computer-vision-meets-llm/"><span class="link-arrow">&#8594;</span> Computer Vision Meets LLM</a></li>
      <li><a href="/contents/publications/Books/opencv5-chapter0-introduction/"><span class="link-arrow">&#8594;</span> OpenCV 5 — Ch.0 Introduction</a></li>
      <li><a href="/contents/publications/Books/opencv5-chapter1-image-basics/"><span class="link-arrow">&#8594;</span> OpenCV 5 — Ch.1 Image Basics</a></li>
      <li><a href="/contents/publications/Books/opencv5-chapter2-feature-detection/"><span class="link-arrow">&#8594;</span> OpenCV 5 — Ch.2 Feature Detection</a></li>
      <li><a href="/contents/publications/Books/opencv5-chapter3-advanced/"><span class="link-arrow">&#8594;</span> OpenCV 5 — Ch.3 Advanced Topics</a></li>
      <li><a href="/contents/publications/Books/computational-intelligence-optical-flow/"><span class="link-arrow">&#8594;</span> Optical Flow for Video Stabilization</a></li>
      <li><a href="/contents/publications/Books/camera-calibration-video-stabilization/"><span class="link-arrow">&#8594;</span> Camera Calibration for Robotics</a></li>
    </ul>
  </div>

  <div class="sitemap-section">
    <span class="section-icon">&#127908;</span>
    <div class="section-title">Keynotes <span class="badge">1</span></div>
    <ul class="sitemap-links">
      <li><a href="/contents/publications/Keynotes/llms-meet-computer-vision/"><span class="link-arrow">&#8594;</span> LLMs Meet Computer Vision</a></li>
    </ul>
  </div>

  <div class="sitemap-section">
    <span class="section-icon">&#128196;</span>
    <div class="section-title">Full CV</div>
    <ul class="sitemap-links">
      <li><a href="/contents/publications/CV/"><span class="link-arrow">&#8594;</span> Curriculum Vitae</a></li>
      <li><a href="/contents/publications/10Years/"><span class="link-arrow">&#8594;</span> 10 Years of CV Bug Fixing</a></li>
      <li><a href="/contents/public/Resources/"><span class="link-arrow">&#8594;</span> Portfolio & Resources</a></li>
    </ul>
  </div>

</div>
