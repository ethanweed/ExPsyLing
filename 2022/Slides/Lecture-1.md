# Experimental Psycholinguistics


---

# Thinking about thinking



---


<img src="https://uploads6.wikiart.org/images/edward-hopper/gas.jpg!Large.jpg" width="900"/>

---

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Moby-Dick_%281851%29_US_edition.djvu/page33-1024px-Moby-Dick_%281851%29_US_edition.djvu.jpg" width="400"/>

---


# Warmup

---

### Observation 1


<img src="https://cdn.imgbin.com/1/8/14/imgbin-powerlifting-3ZUAsdgLH9dpFTdUx7dbeGEkH.jpg">

Hearing a backwards count interfered with my ability to count forwards.

---

### Observation 2


<img src="https://cdn.imgbin.com/1/8/14/imgbin-powerlifting-3ZUAsdgLH9dpFTdUx7dbeGEkH.jpg">

Hearing other language does not interfere with my ability to count forwards.

---

### Discuss

- What could explain this phemonenon?
- What hypothesis/hypotheses does your explanation generate?
- How could you test your hypothesis/hypotheses?

---



# This course

----------------------------------------


## Today

1. Warmup: observations, hypotheses, and tests
2. Course goals
3. Course structure
4. Exam
5. Evaluation of intro week (10 minutes)
6. Introductions
7. Why so much computer stuff?

---

#### Course goals 

Learn to...

::: incremental

- translate theories to research hypotheses
- translate research hypotheses to statistical hypotheses
- interpret statistical results in relation to theories

:::

---

#### Course goals 

Learn to...

::: incremental

- Understand the relationship between theoretical concepts and data
- Operationalize theoretical concepts experimentally through measurable indices
- Analyze and interpret findings in a critical way
- Communicate experimental findings in a clear way to both expert and lay audiences

:::


---

### Course structure

- Lectures
- Labs
- Instructor Sessions

---

## Introductions

---

#### Exam

Pass/fail portfolio

1. Three lab reports, completed throughout  the semester, using the <a href="https://github.com/ethanweed/ExPsyLing/raw/master/2021/Resources/Experimental%20Report%20Template.doc" target="_blank">lab report template</a>
2. Proof of completion of online GDPR course in either <a href="https://brightspace.au.dk/d2l/le/discovery/view/course/27011" target="_blank">Danish</a> or <a href="https://brightspace.au.dk/d2l/le/discovery/view/course/30198" target="_blank">English</a>
3. Design Your Own Experiment: Introduction and Methods sections for a proposed experiment on a topic of your choice

---

#### Why so much computer stuff?



<img src="https://clipground.com/images/computer-help-clipart-5.jpg" width="40%">

---


#### Humanities Computing


<img src="https://github.com/ethanweed/ExPsyLing/blob/master/2022/Resources/HumanitiesComputing.png?raw=true" width="600"/>


---

> "computing belongs within the humanities because it accords  with their central project: to help scholars ask better questions."

\- McCarty(2003)

---

#### Concordance of the Bible

<img src="https://upload.wikimedia.org/wikipedia/commons/7/77/Excerpt_from_%22A_complete_concordance_to_the_Holy_Scriptures%22_by_Alexander_Cruden.png" width="60%">

"commonplace physical devices for manipulating knowledge" \-McCarty(2003)

---

#### Concordance of the Bible

The first concordance of the Latin Bible was completed in 1230, and is said to have been written by 500 Dominican munks.

---

The first concordance of the Hebrew Bible was written by a single person, Rabbi Mordecai Nathan, and was completed in 1448 after 10 years of work.

---

It took me 10 minutes to find every occurrence of "this world" in the King James bible:

```
bigrams = []
for i, val in enumerate(text2):
    if val == "world":
        if text2[i-1] == "this":
            bigrams.append(str(' '.join(text2[i-5:i+5])))
```

---

Here are they are:

```
['for the children of this world are in their generation',
 'them, the children of this world marry, and are given',
 'hateth his life in this world shall keep it unto',
 'shall the prince of this world be cast out. ',
 'should depart out of this world unto the father, having',
 'for the prince of this world cometh, and hath nothing',
 'because the prince of this world is judged.  16:12',
 'of the princes of this world knew: for had they',
 'for the wisdom of this world is foolishness with god.',
 'for the fashion of this world passeth away.  7:32',
 'whom the god of this world hath blinded the minds',
 'chosen the poor of this world rich in faith, and',
 'saying, the kingdoms of this world are become the kingdoms']
 ```

---

#### Interesting comparisons

<div id = "left">

```
['for the children of this world are in their generation',
 'them, the children of this world marry, and are given',
 'hateth his life in this world shall keep it unto',
 'shall the prince of this world be cast out. ',
 'should depart out of this world unto the father, having',
 'for the prince of this world cometh, and hath nothing',
 'because the prince of this world is judged.  16:12',
 'of the princes of this world knew: for had they',
 'for the wisdom of this world is foolishness with god.',
 'for the fashion of this world passeth away.  7:32',
 'whom the god of this world hath blinded the minds',
 'chosen the poor of this world rich in faith, and',
 'saying, the kingdoms of this world are become the kingdoms']
 ```


</div>



<div id = "right">

<img src="https://upload.wikimedia.org/wikipedia/commons/7/77/Excerpt_from_%22A_complete_concordance_to_the_Holy_Scriptures%22_by_Alexander_Cruden.png" width="200%">

</div>





---

#### Algorithmic thinking: find musical phrases

![](Images/MusicalPatterns.png)

---

#### Algorithmic thinking leads to [ontological](https://en.wikipedia.org/wiki/Ontology) thinking


"the interest lies in the questions raised by such algorithmic thinking, especially by the inevitable mismatch between any algorithm and data of the sort normal to the humanities. This mismatch forces ontological questions that lead back to one or more fundamental problems in the discipline of origin and may at the same time illuminate basic methodological issues relevant beyond it."

---

#### Metalinguistic thinking: tagging utterances with XML

html:
```
I study at <a href="https://www.au.dk">Aarhus Universitet</a>.

```

xml (source: http://www.talkbank.org)
```
  <u who="MOT" uID="u25">
    <w>what</w>
    <w>are</w>
    <w>these</w>
    <t type="q"></t>

    <a type="coding">$LAN:E $ADD:CHI</a>
  </u>

```

---


#### Metalinguistic thinking leads to clear thinking

"deep encoding is very laborious, and it is precisely the kind of task in which the full range of scholarly abilities are required. It thus demonstrates that encoding can itself be a form of rather than preparation for scholarship. This new form is shaped by the two imperatives of computational tractability, namely **total explicitness** and **absolute consistency.**"

---

#### Representational thinking: visualizing authorial voice

<div id = "left">

[Lucy Hutchinson](https://en.wikipedia.org/wiki/Lucy_Hutchinson) (1618–1681)


</div>

Translator, poet, and biographer


<div id = "right">

<img src="https://nottinghamcityofliterature.com/uploads/images/Lucy.jpg" width="400"/>

</div>

---

#### Representational thinking: visualizing authorial voice


<img src="https://github.com/ethanweed/ExPsyLing/blob/master/2021/Slides/Images/AuthorshipAnalysis2.png?raw=true" width="600"/>

---

#### Representational thinking: visualizing authorial voice


<img src="https://github.com/ethanweed/ExPsyLing/blob/master/2021/Slides/Images/AuthorshipAnalysis.png?raw=true" width="600"/>

---

#### Representational thinking leads to new insights

"... arranging, formatting, or otherwise transforming the appearance of data \[leading to] what Arnheim has called 'visual thinking'"

---

Computers are tools that encourage:

1. Algorithmic thinking  
2. Metalinguistic thinking  
3. Representational thinking  

---



---

# References

---

## References




<div id = "refs">  



Burrows, J., & Craig, H. (2001). Lucy Hutchinson and the authorship of two seventeenth-century poems: a computational approach. _The Seventeenth Century_, _16_(2), 259-282.

Cambouropoulos, E., Crawford, T., & Iliopoulos, C. S. (2001). Pattern processing in melodic sequences: Challenges, caveats and prospects. _Computers and the Humanities_, _35_(1), 9-21.

McCarty, W. (2003). Humanities computing. _Encyclopedia of library and information science_, _2_, 1224.

Paradis, J., Nicoladis, E., & Genesee, F. (2000) Early emergence of structural constraints on code-mixing: Evidence from French-English bilingual children. Bilingualism: Language and Cognition, 3: 245-261.




<em>IMAGES:</em>

[Edward Hopper (1940) "Gas"](https://www.wikiart.org/en/edward-hopper/gas)

[Herman Melville (1851) "Moby Dick, or, The Whale"](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Moby-Dick_%281851%29_US_edition.djvu/page33-1024px-Moby-Dick_%281851%29_US_edition.djvu.jpg)

</div>


---

