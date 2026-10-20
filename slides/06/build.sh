#!/bin/bash
set -euo pipefail

# miniconda's pandoc is x86_64 and silently fails under Rosetta-less arm64 --
# prefer the homebrew (arm64-native) build if present.
if [ -x /opt/homebrew/bin/pandoc ]; then
  PANDOC=/opt/homebrew/bin/pandoc
else
  PANDOC=pandoc
fi

MD_FILE="presentation.md"

TITLE=$(sed -n 's/^title: *"\(.*\)"/\1/p' "$MD_FILE" | head -n1)
SLUG=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | sed -e 's/[^a-z0-9]/-/g' -e 's/-\+/-/g' -e 's/^-//' -e 's/-$//')
OUT_FILE="${SLUG}.html"

"$PANDOC" "$MD_FILE" -t revealjs --embed-resources --standalone --citeproc --slide-level=2 \
  --metadata date="$(date +'%B %d, %Y')" \
  -o "$OUT_FILE"

echo "All done! Created $OUT_FILE"
