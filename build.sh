#!/bin/bash

# build html documents

# in case you need it:
#-V revealjs-url=https://unpkg.com/reveal.js@^4/

# Notebooks

jupyter nbconvert --to html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Notebooks/Lab_02.ipynb
jupyter nbconvert --to html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Notebooks/Lab_02_solutions.ipynb
jupyter nbconvert --to html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Notebooks/Lab_04.ipynb
jupyter nbconvert --to html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Notebooks/Lab_04_assignment.ipynb

jupyter nbconvert --to html /Users/ethan/Documents/GitHub/ExPsyLing/datasets/Sternberg/scripts/SternbergPlotGallery.ipynb

####### Lecture slides

# Lecture 2
pandoc -t revealjs -s -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lecture_02_Intro.html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lecture_02_Intro.md -V theme=solarized -V revealjs-url=https://unpkg.com/reveal.js/

# Lecture 3
pandoc -t revealjs -s -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lecture_03_Psycholinguistics.html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lecture_03_Psycholinguistics.md -V theme=solarized -V revealjs-url=https://unpkg.com/reveal.js/

# Lecture 4
pandoc -t revealjs -s -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lecture_04_WorkingMemory.html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lecture_04_WorkingMemory.md -V theme=solarized -V transition=none -V revealjs-url=https://unpkg.com/reveal.js/

# Lecture 5
pandoc -t revealjs -s -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lecture_05_ResearchDesign.html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lecture_05_ResearchDesign.md -V theme=solarized -V transition=none -V revealjs-url=https://unpkg.com/reveal.js/

# Lecture 6
pandoc -t revealjs  --mathjax -s -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lecture_06_DescriptiveStatistics.html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lecture_06_DescriptiveStatistics.md -V theme=solarized -V transition=none -V revealjs-url=https://unpkg.com/reveal.js/

# Lecture 7
pandoc -t revealjs  --mathjax -s -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lecture_07_Hypothesis-Testing.html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lecture_07_Hypothesis-Testing.md -V theme=solarized -V transition=none -V revealjs-url=https://unpkg.com/reveal.js/


#Lab slides


pandoc -t revealjs -s -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lab_02_Why.html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lab_02_Why.md -V theme=solarized -V revealjs-url=https://unpkg.com/reveal.js/

pandoc -t revealjs -s -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lab_02_Why.html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lab_02_Why.md -V theme=solarized -V revealjs-url=https://unpkg.com/reveal.js/

pandoc -t revealjs --mathjax -s -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lab_06_VisualizingData.html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lab_06_VisualizingData.md -V theme=solarized -V transition=none -V revealjs-url=https://unpkg.com/reveal.js/

pandoc -t revealjs --mathjax -s -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lab_07_Sternberg-Design.html /Users/ethan/Documents/GitHub/ExPsyLing/2021/Slides/Lab_07_Sternberg-Design.md -V theme=solarized -V transition=none -V revealjs-url=https://unpkg.com/reveal.js/

#Assignments





# Other
pandoc --standalone /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Syllabus.md -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Syllabus.html

pandoc --standalone /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Schedule.md -o /Users/ethan/Documents/GitHub/ExPsyLing/2021/Planning/Schedule.html

# Push to github

git add -A
git commit -m "auto-updated with build.sh"
git push origin master