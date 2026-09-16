#!/bin/bash
# Make a new directory with template files for revealjs presentation.
# Usage: ./new-deck.sh [name]
#   name  optional dir name (e.g. "03"). Defaults to next
#         zero-padded number after the highest existing numeric dir.

set -euo pipefail
cd "$(dirname "$0")"

if [ -n "${1:-}" ]; then
  DIR_NAME="$1"
else
  LAST=0
  for d in [0-9][0-9]; do
    [ -d "$d" ] || continue
    n=$((10#$d))
    [ "$n" -gt "$LAST" ] && LAST=$n
  done
  DIR_NAME=$(printf "%02d" "$((LAST + 1))")
fi

if [ -e "$DIR_NAME" ]; then
  echo "Error: $DIR_NAME already exists" >&2
  exit 1
fi

mkdir -p "$DIR_NAME/images"

cat > "$DIR_NAME/build.sh" <<'EOF'
#!/bin/bash

MD_FILE="presentation.md"

TITLE=$(sed -n 's/^title: *"\(.*\)"/\1/p' "$MD_FILE" | head -n1)
SLUG=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | sed -e 's/[^a-z0-9]/-/g' -e 's/-\+/-/g' -e 's/^-//' -e 's/-$//')
OUT_FILE="${SLUG}.html"

pandoc "$MD_FILE" -t revealjs --self-contained --standalone --citeproc --slide-level=2 \
  --metadata date="$(date +'%B %d, %Y')" \
  -o "$OUT_FILE"

echo "All done! Created $OUT_FILE"
EOF
chmod +x "$DIR_NAME/build.sh"

cat > "$DIR_NAME/presentation.md" <<'EOF'
---
title: ""
author: "Ethan Weed"
date: "date"
bibliography: refs.bib
csl: ../shared/apa.csl
theme: white
customTheme: "catppuccin-latte"
css: ../shared/slide-styles.css
revealjs-url: https://cdn.jsdelivr.net/npm/reveal.js@5
slideNumber: true
progress: true
---
EOF

touch "$DIR_NAME/refs.bib"
touch "$DIR_NAME/images/.gitkeep"

echo "Created $DIR_NAME/ with build.sh, presentation.md, refs.bib, images/"
