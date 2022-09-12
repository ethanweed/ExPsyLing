#!/bin/bash

## Course Planning
pandoc --standalone /Users/ethan/Documents/GitHub/ExPsyLing/2022/Syllabus-2022.md -o /Users/ethan/Documents/GitHub/ExPsyLing/2022/Syllabus-2022.html 


## Lecture Slides

cd /Users/ethan/Documents/GitHub/ExPsyLing/2022/Slides/

for i in *.md ; do echo "$i" && pandoc metadata.yaml -s -t revealjs -s -V revealjs-url=https://unpkg.com/reveal.js/  --include-in-header=styles.css $i --filter=/Users/ethan/opt/miniconda3/lib/python3.9/site-packages/pandoc_mermaid_filter-0.1.0.dist-info -o html/"${i%.*}".html; done





# Push to github

git add -A
git commit -m "auto-updated with build.sh"
git push origin master
