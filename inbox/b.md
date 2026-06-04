---
layout: presentation
title: Farshid Pirahansiah

---

<script src="https://cdn.jsdelivr.net/npm/markmap-autoloader"></script>

<style>
/* Smooth branch expand/collapse */
.markmap-node > path {
  transition: d 0.4s cubic-bezier(0.4, 0, 0.2, 1),
              opacity 0.3s ease;
}

/* Nodes fade + scale in */
.markmap-node {
  transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1),
              opacity 0.3s ease;
}

/* Circle pulse on click */
.markmap-node circle {
  transition: r 0.2s ease, fill 0.2s ease;
}
.markmap-node circle:hover {
  r: 8;
  fill: #f5a623;
  cursor: pointer;
}

/* Collapsed node — circle fills solid */
.markmap-node.markmap-fold circle {
  fill: currentColor !important;
  r: 6;
}

/* Smooth text fade */
.markmap-node text {
  transition: opacity 0.3s ease;
}

/* Lines draw smoothly */
.markmap-link {
  transition: d 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
</style>

<div class="markmap">

# My Project

## Frontend
### React
- Components
- Hooks
### CSS
- Tailwind
- Animations

## Backend
### Node.js
### Database
- Postgres
- Redis

## DevOps
- Docker
- CI/CD

</div>
