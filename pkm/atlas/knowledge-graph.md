
---
layout: default
title: Knowledge Graph
tags: pkm knowledge graph graph database ontology semantics
categories: atlas
links: https://pirahansiah.github.io/atlas/knowledge-graph/
references: system-design, strategic-connections
related: technology, research
backlinks: /contents/pkm/about/company.md

---

<script>
async function getAllMdFiles(path = 'contents', files = []) {
  try {
    const response = await fetch(`https://api.github.com/repos/pirahansiah/pirahansiah.github.io/contents/${path}`);
    if (!response.ok) return files;
    
    const items = await response.json();
    if (!Array.isArray(items)) return files;
    
    for (const item of items) {
      if (item.name.startsWith('.')) continue;
      
      if (item.type === 'file' && item.name.endsWith('.md')) {
        files.push({
          name: item.name.replace('.md', ''),
          path: item.path.replace('contents/', '').replace('.md', '')
        });
      } else if (item.type === 'dir') {
        await getAllMdFiles(item.path, files);
      }
    }
  } catch (error) {
    console.error('Error fetching files:', error);
  }
  
  return files;
}

async function renderMdLinks() {
  const files = await getAllMdFiles();
  files.sort((a, b) => a.name.localeCompare(b.name));
  
  const linksList = files.map(f => 
    `<li><a href="/${f.path}/">${f.name}</a></li>`
  ).join('');
  
  const container = document.querySelector('main') || document.body;
  container.insertAdjacentHTML('beforeend', `
    <section style="margin-top: 40px; padding: 20px; border-top: 1px solid #ccc;">
      <h2>📚 All Knowledge Pages</h2>
      <ul style="column-count: 2; column-gap: 30px; line-height: 1.8;">
        ${linksList}
      </ul>
    </section>
  `);
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', renderMdLinks);
} else {
  renderMdLinks();
}
</script>