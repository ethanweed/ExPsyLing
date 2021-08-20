#!/bin/bash

# build html documents


# Lecture slides
pandoc -t revealjs -s -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Slides/Slides_week_02.html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Slides/Lecture_02.md -V revealjs-url=https://unpkg.com/reveal.js@^4/


#Lab slides
#pandoc -t revealjs -s -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Slides/Lab1_Why.html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Slides/Lab1_Why.md -V revealjs-url=https://unpkg.com/reveal.js@^4/

pandoc -t revealjs -s -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Slides/Lab1_Why.html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Slides/Lab_02_Why.md -V theme=solarized -V revealjs-url=https://unpkg.com/reveal.js@3.9.2/
	


#pandoc -t revealjs -s -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Slides/Slides_week_02.html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Slides/#Slides_week_02.md -V revealjs-url=https://unpkg.com/reveal.js@3.9.2/



# Other
pandoc --standalone /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Syllabus.md -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Syllabus.html

pandoc --standalone /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Schedule.md -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Schedule.html

# Push to github

git add -A
git commit -m "auto updated with build.sh"
git push origin master