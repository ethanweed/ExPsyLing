#!/bin/bash

# build html documents

# in case you need it:
#-V revealjs-url=https://unpkg.com/reveal.js@^4/

# Lecture slides

pandoc -t revealjs -s -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Slides/Lecture_02.html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Slides/Lecture_02.md -V theme=solarized -V revealjs-url=https://unpkg.com/reveal.js@3.9.2/


#Lab slides


pandoc -t revealjs -s -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Slides/Lab_02_Why.html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Slides/Lab_02_Why.md -V theme=solarized -V revealjs-url=https://unpkg.com/reveal.js@3.9.2/
	



# Other
pandoc --standalone /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Syllabus.md -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Syllabus.html

pandoc --standalone /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Schedule.md -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Schedule.html

# Push to github

git add -A
git commit -m "auto updated with build.sh"
git push origin master