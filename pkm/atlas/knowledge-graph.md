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
    
    if (!response.ok) {
      console.error('API error:', response.status, response.statusText);
      return files;
    }
    
    const items = await response.json();
    
    for (const item of items) {
      // Skip hidden files and non-md files
      if (item.name.startsWith('.')) continue;
      
      if (item.type === 'file' && item.name.endsWith('.md')) {
        files.push({
          name: item.name.replace('.md', ''),
          path: '/' + item.path,
          url: '/' + item.path
        });
      } else if (item.type === 'dir') {
        const result = await getAllMdFiles(item.path, files);
        files = result;
      }
    }
  } catch (error) {
    console.error('Error fetching files:', error);
  }
  
  return files;
}

async function renderAllMdLinks() {
  const files = await getAllMdFiles();
  
  if (files.length === 0) {
    const container = document.querySelector('main') || document.body;
    container.insertAdjacentHTML('beforeend', `
      <section style="margin-top: 40px; padding: 20px; border-top: 1px solid #ccc;">
        <h2>📚 All Knowledge Pages</h2>
        <p>No .md files found.</p>
      </section>
    `);
    return;
  }
  
  const linksList = files.map(f => 
    `<li><a href="${f.url}">${f.name}</a></li>`
  ).join('');
  
  const container = document.querySelector('main') || document.body;
  container.insertAdjacentHTML('beforeend', `
    <section style="margin-top: 40px; padding: 20px; border-top: 1px solid #ccc;">
      <h2>📚 All Knowledge Pages (${files.length} documents)</h2>
      <ul style="column-count: 3; column-gap: 30px; line-height: 1.8;">
        ${linksList}
      </ul>
    </section>
  `);
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', renderAllMdLinks);
} else {
  renderAllMdLinks();

---

# 233333333


<div id="knowledge-explorer" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px;">
<div id="loader" style="padding: 40px; text-align: center; color: #666;">
<div class="spinner" style="border: 4px solid #f3f3f3; border-top: 4px solid #3498db; border-radius: 50%; width: 30px; height: 30px; animation: spin 2s linear infinite; margin: 0 auto 15px;"></div>
Initializing Intelligence Network...
</div>
</div>
<style>
@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
.category-block { margin-bottom: 40px; animation: fadeIn 0.5s ease-in; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
.knowledge-list { column-count: 2; column-gap: 40px; list-style-type: none; padding: 0; margin: 0; }
@media (max-width: 600px) { .knowledge-list { column-count: 1; } }
.knowledge-item { margin-bottom: 12px; break-inside: avoid; }
.knowledge-link { color: #0076df; text-decoration: none; font-size: 1.05rem; transition: color 0.2s; display: block; border-left: 3px solid #eee; padding-left: 12px; }
.knowledge-link:hover { color: #004a8d; border-left-color: #3498db; background: #f9f9f9; }
.category-title { font-size: 0.85rem; letter-spacing: 0.1em; color: #888; text-transform: uppercase; border-bottom: 1px solid #eee; padding-bottom: 8px; margin-bottom: 15px; font-weight: 600; }
</style>
<script>
async function buildKnowledgeAtlas() {
const container = document.getElementById('knowledge-explorer');
const loader = document.getElementById('loader');
const repo = "pirahansiah/pirahansiah.github.io";
const branch = "main";

try {
const response = await fetch(`https://api.github.com/repos/${repo}/git/trees/${branch}?recursive=1`);
if (!response.ok) throw new Error('API limit reached or Repository not found');

const data = await response.json();
const assets = data.tree
.filter(item =>
item.type === 'blob' &&
item.path.startsWith('contents/') &&
item.path.endsWith('.md') &&
!item.path.includes('index.md') &&
!item.path.split('/').some(p => p.startsWith('.'))
)
.map(item => {
const pathSegments = item.path.replace(/^contents\//, '').replace(/\.md$/, '').split('/');
const rawName = pathSegments.pop();
const category = pathSegments.length > 0 ? pathSegments.join(' / ') : 'Root';

return {
title: rawName.replace(/[-_]/g, ' ').replace(/\b\w/g, l => l.toUpperCase()),
url: `/${item.path.replace(/^contents\//, '').replace(/\.md$/, '')}/`,
category: category.toUpperCase()
};
});

if (assets.length === 0) {
container.innerHTML = '<h2>Atlas</h2><p>No intelligence assets found in /contents/ directory.</p>';
return;
}

assets.sort((a, b) => a.title.localeCompare(b.title));

const grouped = assets.reduce((acc, asset) => {
(acc[asset.category] = acc[asset.category] || []).push(asset);
return acc;
}, {});

loader.style.display = 'none';

let html = `<h1 style="margin-bottom: 40px; font-weight: 300; border-bottom: 2px solid #333; padding-bottom: 10px;">Strategic Atlas</h1>`;

for (const [category, items] of Object.entries(grouped)) {
html += `
<div class="category-block">
<div class="category-title">${category}</div>
<ul class="knowledge-list">
${items.map(f => `
<li class="knowledge-item">
<a href="${f.url}" class="knowledge-link">${f.title}</a>
</li>
`).join('')}
</ul>
</div>
`;
}

container.innerHTML = html;

} catch (err) {
console.error(err);
container.innerHTML = `
<div style="background: #fff5f5; border: 1px solid #feb2b2; padding: 20px; color: #c53030; border-radius: 8px;">
<strong>Connection Error:</strong> Could not retrieve Knowledge Graph from GitHub API.
<br><small>This may be due to rate limiting. Please refresh in a moment.</small>
</div>`;
}
}

if (document.readyState === 'loading') {
document.addEventListener('DOMContentLoaded', buildKnowledgeAtlas);
} else {
buildKnowledgeAtlas();
}
</script>