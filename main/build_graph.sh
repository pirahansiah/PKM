#!/usr/bin/env bash

set -euo pipefail

cd "$(dirname "$0")"

MODEL="${OLLAMA_MODEL:-qwen3.5:4b-mlx}"
HOST="${OLLAMA_HOST:-http://127.0.0.1:11434}"

# Reuse the existing conda env per workspace policy (never create a new one).
if command -v conda >/dev/null 2>&1; then
  # shellcheck disable=SC1091
  source "$(conda info --base)/etc/profile.d/conda.sh" || true
  conda activate py314 || true
fi

python knowledge_graph.py --model "$MODEL" --host "$HOST" "$@"

# Copy generated graph to Jekyll assets so the site can serve it.
DEST="/Volumes/4tb/myWebsite/assets/knowledge_graph.html"
cp knowledge_graph.html "$DEST"
echo "[OK] Copied to $DEST"

# Open in the default browser where possible.
if command -v open >/dev/null 2>&1; then
  open "$DEST" || true
elif command -v xdg-open >/dev/null 2>&1; then
  xdg-open "$DEST" || true
fi
