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

# option 1

<div id="knowledge-graph">Loading Intelligence...</div>

<script>
async function getFiles() {
  const repo = "YOUR_USERNAME/YOUR_REPO_NAME";
  const response = await fetch(`https://api.github.com/repos/${repo}/contents/`);
  const data = await response.json();
  
  let html = '<ul>';
  data.forEach(file => {
    if (file.name.endsWith('.md')) {
      html += `<li><a href="${file.html_url}">${file.name.replace('.md', '')}</a></li>`;
    }
  });
  html += '</ul>';
  document.getElementById('knowledge-graph').innerHTML = html;
}
getFiles();
</script>


---
# option 2:

---


# Knowledge Assets

{% assign categories = "pkm" | split: ", " %}

{% for category in categories %}
## {{ category | capitalize }}
<ul>
  {% for file in site.pages %}
    {% if file.path contains category and file.ext == ".md" %}
      <li><a href="{{ file.url | relative_url }}">{{ file.title | default: file.name }}</a></li>
    {% endif %}
  {% endfor %}
</ul>
{% endfor %}