#!/bin/bash

pandoc presentation.md -t revealjs --self-contained --standalone --citeproc --slide-level=2 -o presentation.html

echo "All done!"