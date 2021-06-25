#!/bin/bash

# build html documents



# Slides
pandoc -t revealjs -s -o /Users/ethan/Documents/GitHub/ExPsyLing/_build/html/Slides_week_02.html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Slides_week_02.md -V revealjs-url=https://unpkg.com/reveal.js@3.9.2/




# Other
pandoc --standalone /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Syllabus.md -o /Users/ethan/Documents/GitHub/ExPsyLing/_build/html/Syllabus.html

# Push to github pages
#ghp-import -n -p -f _build/html

ghp-import -p -f _build/html