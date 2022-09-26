# Experimental Design

---

# Review

---

## Quiz

1. According to the Simple View of Reading, what are the two basic components of reading, and how are the related?
2. Which two "natural" senses did I claim reading combines, to form a "sixth sense"?
3. What do psycholinguists mean by "visual word recognition", and what are some of the factors than can affect it?

---

# Cause and effect

---

### Good questions


<div id = "left">

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/2022/Resources/reading_skull2.png?raw=true" width="500"/>
</div>



<div id = "right">

::: {.incremental}

- What "causes" this to happen?
- What is the underlying mechansim?
- How does this work?

:::

</div>

---

### Two (somewhat naive?) answers
<div id = "left">

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/2022/Resources/reading_skull2.png?raw=true" width="500"/>

</div>



<div id = "right">

::: {.incremental}

1. We look at each letter in turn, and then combine the "sounds" to make the word
2. We just look at the word, and hear the sound

:::



</div>

---

### A cognitive model



<div id = "left">

Research question

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/2022/Resources/reading_skull2.png?raw=true" width="500"/>

</div>




<div id = "right">

Cognitive model

```{.mermaid format=svg  theme=neutral width=400 }
graph TB
A(See word) -->B(Segment graphemes)
B-->C(Recognize graphemes) 
C-->D(Convert graphemes to phonemes)
D --> E("Hear" the word)

```





</div>


---

### Predictions from the model

<div id = "left">
Causal model
```{.mermaid format=svg theme=forest width=400} 
graph LR
A(grapheme-phoneme conversion time)-->B(reading time)

```

</div>

<div id = "right">
Cognitive model
```{.mermaid format=svg  theme=neutral width=400 }
graph TB
A(See word) -->B(Segment graphemes)
B-->C(Recognize graphemes) 
C-->D(Convert graphemes to phonemes)
D --> E("Hear" the word)

```
</div>

---

<div id = "left">
Causal model
```{.mermaid format=svg theme=forest width=400} 
graph LR
A(grapheme-phoneme conversion time)-->B(reading time)

```

</div>

<div id = "right">
Statistical model

Response time in a lexical decision task will increase linearly with the number of letters in the stimulus word

</div>

---

### A different cognitive model

<div id = "left">

Research question

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/2022/Resources/reading_skull2.png?raw=true" width="500"/>

</div>

<div id = "right">
Cognitive model
```{.mermaid format=svg  theme=neutral width=400 }
graph TB
A(See word) -->B(Segment graphemes)


```
</div>


---


<div id = "left">
```{.mermaid format=svg theme=forest width=400} 
graph LR
A(grapheme phoneme conversion)
B(reading time)

```

</div>

<div id = "right">
Statistical model

Response time in a lexical decision task will increase linearly with the number of letters in the stimulus word

</div>

---

# Variables

---



### Scales of measurement



::: {.container}
:::: {.col}
![](https://lh4.googleusercontent.com/ZdmcnWR6MhAj9Cg_vI3Ip-XB-XdJbTtblvOobiF0lAerSgiBbpG_EhevI-jY28-RSMKLrJE2TG3YLDAGRuM9kJDJKCbDI6472EgptiqDU_7ovNUrv1RzyZWVozU62mbDO7PifSBFUY0=s0)
::::
:::: {.col}
- **Nominal**: names (no calculations)  
- **Ordinal:** order (no calculations)  
- **Ratio:** (0=0; mulitiplication and division ok)  
::::
:::




---

### Scales of measurement


	
::: {.container}
:::: {.col}
<img src="https://lh3.googleusercontent.com/JOTbMGt8Z7rIz3ShSO2bwOzFqWdeOtHl_t3n0wFSELp00CPP3CaJ0R4EZJ1Lu-_YGxY1091TvkAX7VkC7IWSPkllnjnBQZynATtCTP4wMx-Z-Cu0Uga8LiNQ56h92gYUOuC7hGk85JY=s0" width=300 style="transform:rotate(180deg);"> 
::::
:::: {.col}
**Interval**: 
	
- differences between numbers meaningful  
-  zero ≠ zero
::::
:::



---

### Continuous versus discrete variables

<table style="border-collapse:collapse;border-spacing:0" class="tg"><thead><tr><th style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"></th><th style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">continuous</th><th style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">discrete</th></tr></thead><tbody><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">nominal</td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">✓</td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">ordinal</td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">✓</td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">interval</td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">✓</td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">✓</td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">ratio</td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">✓</td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">✓</td></tr></tbody></table>

_Possible combinations_ 

---



#### Data types

<table style="border-collapse:collapse;border-spacing:0" class="tg"><thead><tr><th style="border-color:inherit;border-style:solid;border-width:1px;color:#333333;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:normal">Year</span></th><th style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">Freshness</span></th><th style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">BoxOffice</span></th><th style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">MovieTitle</span></th></tr></thead><tbody><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">2009</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">0.33</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">146.3</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">Paul Blart: Mall Cop</span></td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">2009</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">0.68</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">51.8</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">Funny People</span></td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">2010</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">0.1</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">162</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">Grown Ups</span></td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">2011</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">0.19</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">103</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">Just Go with It</span></td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">2011</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">0.14</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">80.4</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">Zookeeper</span></td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">2011</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">0.03</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">74.2</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">Jack and Jill</span></td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">2011</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">0</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">2.3</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">Bucky Larson: Born to Be a Star</span></td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">2012</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">0.44</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">148.3</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">Hotel Transylvania</span></td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">2012</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">0.2</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">36.9</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">That's My Boy</span></td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">2013</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">0.07</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">133.7</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">Grown Ups 2</span></td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">2014</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">0.14</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">46.3</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">Blended</span></td></tr><tr><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">2015</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">0.06</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">69.3</span></td><td style="border-color:inherit;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal"><span style="font-weight:400;font-style:normal;text-decoration:none">Paul Blart: Mall Cop 2</span></td></tr></tbody></table>

---

#### The “role” of variables: predictors and outcomes

<table style="border-collapse:collapse;border-spacing:0" class="tg"><thead><tr><th style="border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">ROLE OF THE VARIABLE</th><th style="border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">CLASSICAL NAME</th><th style="border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">MODERN NAME</th></tr></thead><tbody><tr><td style="border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">to be explained</td><td style="border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">dependent variable (DV)</td><td style="border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">outcome (response)</td></tr><tr><td style="border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">to do the explaining</td><td style="border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">independent variable (IV)</td><td style="border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:left;vertical-align:top;word-break:normal">predictor</td></tr></tbody></table>

---

#### Predictor vs Outcome Measures

<img src="https://lh3.googleusercontent.com/2qf96oYbtsgxZBOaaHUcUVsUXzfMd3NenspyKJwz2MPkbuYi5zTLJr6o7TThsSsz86Fk4VFt9LihCCFmSxjYGc499RiNwyM1F-7tPElGQPRukwFNDbjaReXSA676mw3vPPsiUt9IUWU=s0" width="500">

---



---

# Experimental Design



#### Experimental Design

<img src="https://lh5.googleusercontent.com/wOGT16KzzKxooBeCbWM7F2ryeH1sIlBdR8hAerqNOJWrJ-0JaZ6zVS-TPXg0L5tnh30PofFwg1y9EgArG8Sod5-2fWcN9bCsTgZorirBEufN4DEH6fyq1IYqzOu1Dl23Pf0XD91bjiA=s0" width="550">

---


**A theoretical construct** is the thing that you’re trying to take a measurement of, like “age”, “gender” or an “opinion”. A theoretical construct can’t be directly observed, and often they’re actually a bit vague.

---
    
**A measure**  refers to the method or the tool that you use to make your observations. A question in a survey, a behavioural observation or a brain scan could all count as a measure.
    
---
	
**An operationalisation** refers to the logical connection between the measure and the theoretical construct, or to the process by which we try to derive a measure from a theoretical construct.


---

**A variable** is what we end up with when we apply our measure to something in the world. That is, variables are the actual “data” that we end up with in our data sets.

---


### Operationalisation: 
#### Define your measurement

:::incremental
-   Be precise about what you are trying to measure.
	- What is the relevant unit of "age" for your experiment?
    - What does it mean for a participant to "have dyslexia"?
    - What do we mean when we say a participant "likes" something?
:::

---------------------------------------- 


### Operationalisation: 
#### Define your measurement

:::incremental
-   Determine what method you will use to measure what you want to measure. 
	-   Age: Self-report? Parental report? How will you phrase the question?
	-   Liking: Self-report? Response time? Eye-tracking? Forced choice?
:::

---------------------------------------- 


### Operationalisation: 
#### Define your measurement

:::incremental
-   Define the set of the allowable values that the measurement can take.
	-   Response time: how precise?
	-   Accuracy: how will measure accuracy?
	-   Labels: how many? which?
	-   Written responses: how will you code them?
:::


---


# References

---

## References


<div id = "refs">




</div>







