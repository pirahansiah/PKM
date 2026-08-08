#!/bin/bash
# Regenerate graph.json from content files
# Run after adding/modifying pages in reddit/
cd "$(dirname "$0")/.."
python3 scripts/generate-graph.py
echo ""
echo "To commit: git add assets/graph.json && git commit -m 'graph: regenerate from content'"
