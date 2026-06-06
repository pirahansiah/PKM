---
layout: default
title: Knowledge Graph
tags: pkm knowledge graph graph database ontology semantics
categories: atlas
links: https://pirahansiah.github.io/atlas/knowledge-graph/
references: system-design, strategic-connections
related: technology, research
backlinks: /contents/pkm/about/company.md

## Core Concept

A **knowledge graph** is a semantic network representing entities and their relationships. Unlike traditional databases, it captures meaning through structure - nodes represent concepts, edges represent relations.

### Why Knowledge Graphs?
- **Contextual Understanding**: Relationships matter more than isolated facts
- **Reasoning Capabilities**: Infer new knowledge from existing connections
- **Scalable Semantics**: Human-readable ontology that machines can execute

### Implementation Stack
- Storage: Property graphs (Neo4j, JanusGraph) or RDF triples (Jena, Stardog)
- Querying: Cypher, SPARQL, or custom graph DSL
- Visualization: D3.js force-directed layouts, Markmap WebAssembly

---

## All Knowledge Pages

<script>
// Auto-generate list of all .md files from GitHub API - no build required
async function loadMdFiles() {
  try {
    const response = await fetch('https://api.github.com/repos/pirahansiah/pirahansiah.github.io/contents/pkm');
    const files = await response.json();
    
    // Filter .md files and convert to readable links (without .md extension)
    const mdFiles = files.filter(f => f.name.endsWith('.md')).map(file => {
      return `<a href="/${file.path}" target="_blank">${file.name.replace('.md', '')}</a>`;
    }).join(', ');
    
    // Display in a simple list format
    document.body.insertAdjacentHTML('beforeend', 
      '<div style="padding: 20px; font-family: system-ui, sans-serif;">' +
        '<h3>📚 All Knowledge Pages</h3>' +
        '<ul style="line-height: 2;">' + mdFiles.split(',').map(f => `<li><a href="/${f}" target="_blank">${f.replace('.md', '')}</a></li>`).join('') + '</ul>' +
      '</div>'
    );
  } catch (error) {
    document.body.insertAdjacentHTML('beforeend', 
      '<p style="color: #666;">Unable to load page list. Please refresh or check your connection.</p>'
    );
  }
}

// Load when page loads
loadMdFiles();
</script>