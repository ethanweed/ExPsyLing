#!/bin/bash


## Lecture Slides

#cd /Users/ethan/Documents/GitHub/ExPsyLing/2022/Slides/

for i in /Users/ethan/Documents/GitHub/ExPsyLing/2022/Slides/*.md ; do echo "$i" && pandoc metadata.yaml -s -t revealjs -s -V revealjs-url=https://unpkg.com/reveal.js/ --include-in-header=styles.css $i -o html/"${i%.*}".html ; done

# Push to github

git add -A
git commit -m "auto-updated with build.sh"
git push origin master
