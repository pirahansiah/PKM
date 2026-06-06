---
layout: default
title: System Design
tags: architecture system design tech stack infrastructure
categories: technology
links: https://github.com/pirahansiah/pirahansiah.github.io
references: knowledge-graph, strategic-connections
related: system-design, technology
backlinks: /contents/pkm/atlas/knowledge-graph.md
---
## Architecture Overview

### Core Components
```
┌─────────────────┐      ┌──────────────────┐      ┌─────────────────┐
│ Data Ingestion  │────>  │ Knowledge Graph   │────>  │ Reasoning Engine │
└─────────────────┘      └──────────────────┘      └─────────────────┘
                                 │                     │
                                v                    v
                         ┌──────────────────┐      ┌─────────────────┐
                         │ Query Interface   │<────│ Visualization    │
                         └──────────────────┘      └─────────────────┘
```

### Tech Stack
- **Frontend**: React + Markmap (WebAssembly)
- **Backend**: Python/FastAPI for graph operations
- **Storage**: SQLite with full-text search indexes
- **Inference**: ONNX Runtime (INT8 quantized models)