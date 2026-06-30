#!/usr/bin/env bash
# Build / update the knowledge graph from all markdown notes in contents/.
# Uses the local Ollama model (qwen3.5:4b-mlx) when reachable, otherwise falls
# back to local TF-IDF + fuzzy + tag/link techniques only.
# Outputs:
#   - assets/graph.json  (for Jekyll site /graph/ page via graph-view.js)
#   - assets/knowledge_graph.html (standalone viewer)
set -euo pipefail

cd "$(dirname "$0")"

# Remove macOS resource fork artifacts that confuse file scanning.
find "$(dirname "$0")/.." -name '._*' -delete 2>/dev/null || true

MODEL="${OLLAMA_MODEL:-qwen3.5:4b-mlx}"
HOST="${OLLAMA_HOST:-http://127.0.0.1:11434}"

# Reuse the existing conda env per workspace policy (never create a new one).
if command -v conda >/dev/null 2>&1; then
  # shellcheck disable=SC1091
  source "$(conda info --base)/etc/profile.d/conda.sh" || true
  conda activate py314 || true
fi

python knowledge_graph.py --model "$MODEL" --host "$HOST" "$@"

# Copy standalone HTML to Jekyll assets so /graph/ can serve it.
DEST="/Volumes/4tb/myWebsite/assets/knowledge_graph.html"
cp knowledge_graph.html "$DEST"
echo "[OK] Copied to $DEST"

echo "[OK] graph.json written to assets/ — Jekyll site will use it at /graph/"

# Open the standalone HTML in the default browser.
if command -v open >/dev/null 2>&1; then
  open knowledge_graph.html || true
elif command -v xdg-open >/dev/null 2>&1; then
  xdg-open knowledge_graph.html || true
fi
