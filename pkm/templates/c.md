---
layout: default
title: Markdown with Mindmap markmap
hashtags: markmap

---

<!-- START OF HERO SECTION -->
<div class="hero-container">
    <div class="glass-title-card">
        <h1 class="liquid-heading">
            Architecting <br>
            <span class="refractive-text">Intelligent Perception</span>
        </h1>
        <p class="strategy-subtitle">
            Strategic Technical Product Management & Consultancy <br>
            <span>Bridging the gap between R&D curiosity and Production-grade AI Vision.</span>
        </p>
        
        <div class="cta-group">
            <a href="#consultancy" class="glass-btn primary">Strategic Audit</a>
            <a href="#projects" class="glass-btn secondary">View Case Studies</a>
        </div>
    </div>
</div>

<style>
/* iOS 26 LIQUID GLASS TYPOGRAPHY */
:root {
    --ios-blue: #007AFF;
    --glass-white: rgba(255, 255, 255, 0.15);
}

.hero-container {
    height: 80vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.glass-title-card {
    padding: 4rem;
    border-radius: 50px;
    background: var(--glass-white);
    backdrop-filter: blur(40px) saturate(180%);
    -webkit-backdrop-filter: blur(40px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 40px 100px rgba(0, 0, 0, 0.3);
    /* The "Liquid" SVG filter from previous steps is applied here */
    filter: url(#liquid-refraction); 
    max-width: 900px;
}

.liquid-heading {
    font-size: 5rem;
    font-weight: 800;
    line-height: 1.1;
    margin: 0;
    color: white;
    letter-spacing: -0.04em;
}

/* The Refractive Mask Effect */
.refractive-text {
    background: linear-gradient(135deg, #fff 0%, rgba(255,255,255,0.4) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    position: relative;
}

.refractive-text::after {
    content: "Intelligent Perception";
    position: absolute;
    left: 0;
    top: 0;
    z-index: -1;
    filter: blur(15px);
    opacity: 0.5;
    background: linear-gradient(90deg, #007AFF, #5AC8FA);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.strategy-subtitle {
    font-size: 1.5rem;
    margin-top: 2rem;
    color: rgba(255, 255, 255, 0.8);
    font-weight: 400;
    letter-spacing: -0.01em;
}

.strategy-subtitle span {
    display: block;
    font-size: 1.1rem;
    margin-top: 10px;
    opacity: 0.6;
}

/* CTA BUTTONS */
.cta-group {
    margin-top: 3rem;
    display: flex;
    gap: 20px;
    justify-content: center;
}

.glass-btn {
    padding: 15px 35px;
    border-radius: 20px;
    text-decoration: none;
    font-weight: 600;
    font-size: 1.1rem;
    transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
    border: 1px solid rgba(255, 255, 255, 0.3);
}

.glass-btn.primary {
    background: white;
    color: black;
}

.glass-btn.secondary {
    background: rgba(255, 255, 255, 0.1);
    color: white;
    backdrop-filter: blur(10px);
}

.glass-btn:hover {
    transform: scale(1.05) translateY(-5px);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
}
</style>