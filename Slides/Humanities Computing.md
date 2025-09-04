---
title: "Humanities Computing"
theme: "serif"
transition: "slide"
highlightTheme: "github"
customTheme: "custom-styles"
---

# Humanities Computing

---



<figure>
   <img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/McCarty_HumanitiesComputing.png?raw=true" width="500"/>
    <figcaption>Figuring illustrating overview of the Humanities Computing landscape. McCarty (2003)</figcaption>
</figure>





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



```
['for the children of this world are in their generation',
 'them, the children of this world marry, and are given',
 'hateth his life in this world shall keep it unto',
 'shall the prince of this world be cast out. ',
 'should depart out of this world unto the father, having',
 'for the prince of this world cometh, and hath nothing',
 'because the prince of this world is judged.  16:12',
 ...]
 ```




<img src="https://upload.wikimedia.org/wikipedia/commons/7/77/Excerpt_from_%22A_complete_concordance_to_the_Holy_Scriptures%22_by_Alexander_Cruden.png" width="200%">





---

#### Algorithmic thinking: find musical phrases

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/MusicalPatterns.png?raw=true" width="800"/>

---

#### Algorithmic thinking leads to [ontological](https://en.wikipedia.org/wiki/Ontology) thinking


"the interest lies in the questions raised by such algorithmic thinking, especially by the inevitable mismatch between any algorithm and data of the sort normal to the humanities. This mismatch forces ontological questions that lead back to one or more fundamental problems in the discipline of origin and may at the same time illuminate basic methodological issues relevant beyond it."

---

#### Metalinguistic thinking: tagging utterances with XML

html:
```
I study at <a href="https://www.au.dk">Aarhus University</a>.

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


<div class="two-columns">
<div class="column">

[Lucy Hutchinson](https://en.wikipedia.org/wiki/Lucy_Hutchinson) (1618–1681)

</div>
<div class="column">

<div class="column">
Translator, poet, and biographer

- Memoirs of the Life of Colonel Hutchinson
- Lucretius 
- Original Poems 
- "anti-panegyric" 
- "Order and Disorder" Parts 1 and 2?


</div>
</div>



---

#### Representational thinking: visualizing authorial voice


<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/Burrows_et_al_AuthorshipAnalysis1.png?raw=true" width="600"/>

---

#### Representational thinking: visualizing authorial voice


<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/Burrows_et_al_AuthorshipAnalysis2.png?raw=true" width="600"/>

---

#### Representational thinking leads to new insights

"... arranging, formatting, or otherwise transforming the appearance of data \[leading to] what Arnheim has called 'visual thinking'"

---

Computers are tools that encourage:

1. Algorithmic thinking  
2. Metalinguistic thinking  
3. Representational thinking  



---

#### References {#references}


- Burrows, J., & Craig, H. (2001). Lucy Hutchinson and the authorship of two seventeenth-century poems: a computational approach. _The Seventeenth Century_, _16_(2), 259-282.

- Cambouropoulos, E., Crawford, T., & Iliopoulos, C. S. (2001). Pattern processing in melodic sequences: Challenges, caveats and prospects. _Computers and the Humanities_, _35_(1), 9-21.

- McCarty, W. (2003). Humanities computing. _Encyclopedia of library and information science_, _2_, 1224.

- Paradis, J., Nicoladis, E., & Genesee, F. (2000) Early emergence of structural constraints on code-mixing: Evidence from French-English bilingual children. Bilingualism: Language and Cognition, 3: 245-261.




---

