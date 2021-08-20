

## Experimental Psycholinguistics

Teacher: Ethan Weed

Instructor: Niels Aalund Krogsgaard


---

## Today

1. Course goals
2. Course structure
3. Exam
4. Introductions

---

#### Course goals 1

We will investigate the cognitive systems involved in...

---


::: incremental

- working memory
- the categorization of meaning
- accessing our lexical representations
- understanding language in context

:::







---

#### Course goals 2

Learn to: 

---

::: incremental

- translate theories to research hypotheses
- translate research hypotheses to statistical hypotheses
- interpret statistical results in relation to theories

:::


---


---

#### Course goals 3

Taken together, the overall goal of the course is for you to learn to...

---

1. Understand the relationship between theoretical concepts and data

---

2. Operationalize theoretical concepts experimentally through measurable indices

---

3. Analyze and interpret findings in a critical way

---

4. Communicate experimental findings in a clear way to both expert and lay audiences

---

#### Course structure

- Lectures
- Labs
- Instructor Sessions

---

#### Why so much computer stuff?



<img src="https://clipground.com/images/computer-help-clipart-5.jpg" width="40%">

---


#### Humanities Computing



<img src="Images/HumanitiesComputingModel.png" width="60%">


---

> "computing belongs within the humanities because it accords  with their central project: to help scholars ask better questions."

\- McCarty(2003)

---

#### Concordance of the Bible

<img src="https://upload.wikimedia.org/wikipedia/commons/7/77/Excerpt_from_%22A_complete_concordance_to_the_Holy_Scriptures%22_by_Alexander_Cruden.png" width="60%">

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


::: {.container}
:::: {.col}
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
::::
:::: {.col}
<img src="https://upload.wikimedia.org/wikipedia/commons/7/77/Excerpt_from_%22A_complete_concordance_to_the_Holy_Scriptures%22_by_Alexander_Cruden.png" width="40%">
::::
:::

---

<section class="hbox"> 
<div class="container"> 
<div class="flex-col" data-markdown> 
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
	</div> <div class="flex-col" data-markdown> 
	<img src="https://upload.wikimedia.org/wikipedia/commons/7/77/Excerpt_from_%22A_complete_concordance_to_the_Holy_Scriptures%22_by_Alexander_Cruden.png" width="40%"> 
	</div> 
	</div> 
</section>

---
#### References


