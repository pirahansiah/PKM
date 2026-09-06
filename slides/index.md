---
layout: farshid_default
title: "Presentation Decks"
description: "Collection of presentation decks on Hermes Agent — research assistance, big computer vision projects, and the complete feature guide."
tags: [presentation, slides, hermes-agent, computer-vision, research]
hashtags: "#presentation #slides #hermes-agent #computervision #research"
permalink: /notes/slides/
---

# Presentation Decks

A collection of slide decks built with [Reveal.js](https://revealjs.com), ready to present or reuse. Click any card to open the full deck.

---

<div class="slides-grid">

  <a class="slide-card" href="/notes/slides/presentation/">
    <div class="slide-thumb">🎓</div>
    <h3>Hermes Agent for Research Assistance</h3>
    <p>Using Hermes Agent for university research — literature review, code reproduction, experimentation, and paper writing.</p>
    <span class="slide-tags">#research #hermes-agent #llm</span>
  </a>

  <a class="slide-card" href="/notes/slides/presentation-cv/">
    <div class="slide-thumb">🖥️</div>
    <h3>Hermes Agent for Big Computer Vision Projects</h3>
    <p>Production-scale CV engineering: setup, bots, multi-agent orchestration, profiling, cron jobs, messaging, group bots, and artifacts.</p>
    <span class="slide-tags">#computervision #multiagent #production</span>
  </a>

  <a class="slide-card" href="/notes/slides/presentation-updates/">
    <div class="slide-thumb">🚀</div>
    <h3>Hermes Agent — Recent Updates & Complete Feature Guide</h3>
    <p>Recent 2026 updates plus a complete tour of every feature, each with a runnable example.</p>
    <span class="slide-tags">#features #update #hermes-agent</span>
  </a>

  <a class="slide-card" href="/notes/slides/research-tools/">
    <div class="slide-thumb">🔬</div>
    <h3>The New Era of Research Tools</h3>
    <p>From passive chat to autonomous workflows: Hermes, LeapSpace, PaperBanana, AI citation finders, agent swarms, peer review, and your Obsidian second brain.</p>
    <span class="slide-tags">#researchtools #hermes-agent #ai #llm</span>
  </a>

</div>

<style>
.slides-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 22px;
  max-width: 1000px;
  margin: 32px auto 56px;
  padding: 0 16px;
}
.slide-card {
  display: block;
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  border-radius: 20px;
  padding: 26px 22px;
  text-decoration: none;
  color: inherit;
  backdrop-filter: blur(20px) saturate(160%);
  -webkit-backdrop-filter: blur(20px) saturate(160%);
  box-shadow: var(--glass-shadow);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.slide-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 14px 40px rgba(34, 211, 238, 0.18);
}
.slide-thumb {
  font-size: 2.4rem;
  margin-bottom: 10px;
}
.slide-card h3 {
  font-size: 1.15rem;
  font-weight: 700;
  margin-bottom: 8px;
  color: #22D3EE;
}
.slide-card p {
  font-size: 0.9rem;
  color: var(--text-muted);
  line-height: 1.55;
  margin-bottom: 12px;
}
.slide-tags {
  font-size: 0.78rem;
  color: #38bdf8;
  font-weight: 600;
}
</style>
