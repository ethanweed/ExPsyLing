#!/bin/bash

pandoc presentation.md -t revealjs --self-contained --standalone --citeproc --slide-level=2 \
  --metadata date="$(date +'%B %d, %Y')" \
  -o presentation.html

echo "All done!"