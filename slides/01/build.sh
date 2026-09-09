#!/bin/bash

MD_FILE="presentation.md"

TITLE=$(sed -n 's/^title: *"\(.*\)"/\1/p' "$MD_FILE" | head -n1)
SLUG=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | sed -e 's/[^a-z0-9]/-/g' -e 's/-\+/-/g' -e 's/^-//' -e 's/-$//')
OUT_FILE="${SLUG}.html"

pandoc "$MD_FILE" -t revealjs --self-contained --standalone --citeproc --slide-level=2 \
  --metadata date="$(date +'%B %d, %Y')" \
  -o "$OUT_FILE"

echo "All done! Created $OUT_FILE"
