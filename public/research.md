---
layout: farshid_default
title: "Research — Publications & Patents"
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
  <h1>Research</h1>
  <p>3 patents, 2 books, 6 journals, 11 conference papers</p>
</div>

<div class="toc-grid">

  <div class="toc-card">
    <h2>&#128220; Patents</h2>
    <ul>
      <li><a href="/contents/publications/Patents/face-image-augmentation/"><span class="arr">&#8594;</span> Face Image Augmentation</a></li>
      <li><a href="/contents/publications/Patents/vehicle-detection/"><span class="arr">&#8594;</span> Vehicle Detection</a></li>
      <li><a href="/contents/publications/Patents/facial-analysis-advertisement/"><span class="arr">&#8594;</span> Facial Analysis Advertising</a></li>
    </ul>
  </div>

  <div class="toc-card">
    <h2>&#128197; Conference Papers</h2>
    <ul>
      <li><a href="/contents/publications/Papers/adaptive-image-segmentation-psnr/"><span class="arr">&#8594;</span> Adaptive Segmentation PSNR</a></li>
      <li><a href="/contents/publications/Papers/camera-calibration-multi-modal/"><span class="arr">&#8594;</span> Camera Calibration</a></li>
      <li><a href="/contents/publications/Papers/"><span class="arr">&#8594;</span> All 11 Papers &#8594;</a></li>
    </ul>
  </div>

  <div class="toc-card">
    <h2>&#128196; Journals</h2>
    <ul>
      <li><a href="/contents/publications/Journals/adaptive-thresholding-psnr/"><span class="arr">&#8594;</span> Adaptive Thresholding</a></li>
      <li><a href="/contents/publications/Journals/3d-slam-humanoid-robots/"><span class="arr">&#8594;</span> 3D SLAM</a></li>
      <li><a href="/contents/publications/Journals/"><span class="arr">&#8594;</span> All 6 Journals &#8594;</a></li>
    </ul>
  </div>

  <div class="toc-card">
    <h2>&#128214; Books</h2>
    <ul>
      <li><a href="/contents/publications/Books/computer-vision-meets-llm/"><span class="arr">&#8594;</span> CV Meets LLM</a></li>
      <li><a href="/contents/publications/Books/opencv5-chapter0-introduction/"><span class="arr">&#8594;</span> OpenCV 5 Ch.0</a></li>
      <li><a href="/contents/publications/Books/"><span class="arr">&#8594;</span> All Books &#8594;</a></li>
    </ul>
  </div>

  <div class="toc-card">
    <h2>&#127908; Keynotes</h2>
    <ul>
      <li><a href="/contents/publications/Keynotes/llms-meet-computer-vision/"><span class="arr">&#8594;</span> LLMs Meet Computer Vision</a></li>
    </ul>
  </div>

  <div class="toc-card">
    <h2>&#128196; Full CV</h2>
    <ul>
      <li><a href="/contents/publications/CV/"><span class="arr">&#8594;</span> Curriculum Vitae</a></li>
      <li><a href="/contents/public/Resources/"><span class="arr">&#8594;</span> Portfolio & Resources</a></li>
    </ul>
  </div>

</div>
