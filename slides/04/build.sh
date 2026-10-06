#!/bin/bash

PANDOC=pandoc
if ! pandoc --version >/dev/null 2>&1 && [ -x /opt/homebrew/bin/pandoc ]; then
  PANDOC=/opt/homebrew/bin/pandoc
fi

"$PANDOC" presentation.md -t revealjs --embed-resources --standalone --citeproc --slide-level=2 \
  --metadata date="$(date +'%B %d, %Y')" \
  -o presentation.html

echo "All done!"
