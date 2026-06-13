#!/bin/bash
# Generates a list of all files in contents/ and appends it to system-design.md
# Run manually or via git pre-commit hook

REPO_ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
CONTENTS_DIR="$REPO_ROOT/contents"
TARGET="$REPO_ROOT/contents/pkm/technology/system-design.md"

if [ ! -d "$CONTENTS_DIR" ]; then
  echo "contents/ directory not found at $CONTENTS_DIR"
  exit 1
fi

# Collect all files (excluding .git, hidden files, and this script itself)
FILE_LIST=$(find "$CONTENTS_DIR" -type f \
  -not -path '*/.git/*' \
  -not -name '.*' \
  -not -name 'update-file-list.sh' \
  -not -name '.gitignore' \
  -not -name 'system-design.md' \
  | sort \
  | while read -r f; do
    rel="${f#$CONTENTS_DIR/}"
    # Create markdown link — URL encode spaces, keep as-is
    echo "- [$rel](/contents/$rel)"
  done)

# Read existing frontmatter (between --- markers)
FRONTMATTER=""
if grep -q "^---" "$TARGET"; then
  # Extract everything up to and including the second ---
  FRONTMATTER=$(awk '/^---$/{n++; if(n==2){print; exit}} 1' "$TARGET")
fi

# Write updated file
cat > "$TARGET" << EOF
$FRONTMATTER

## All Files in contents/

$FILE_LIST
EOF

echo "[update-file-list] Updated $TARGET with $(echo "$FILE_LIST" | wc -l | tr -d ' ') files"
