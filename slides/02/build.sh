#!/bin/bash

pandoc presentation.md -t revealjs --self-contained --standalone --citeproc --slide-level=2 --include-after-body=../shared/chalkboard.html \
  --metadata date="$(date +'%B %d, %Y')" \
  -o presentation.html

echo "All done!"