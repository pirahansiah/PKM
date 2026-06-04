---
layout: default
title: Farshid Pirahansiah

---
---
layout: default
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

computer vision in IoT
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
defaults write com.apple.desktopservices DSDontWriteUSBStores -bool TRUE
dot_clean -m /Volumes/4tb
sudo mdutil -i off /Volumes/4tb
touch /Volumes/4tb/.metadata_never_index

cd /Volumes/4tb/2026-6/pirahansiah.github.io
git submodule update --remote --merge
