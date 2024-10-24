---
title: Experiment Design
---

# Review

---

## Discuss

1. Theoretical constructs
2. Measures
3. Operationalization
4. Variables
	1. Predictor / Independent variables
	2. Outcome / Dependent variables


---

# Inductive inference

---

## "Bottom-up" reasoning

---

## "Bottom-up" reasoning

The first 5 songs on this playlist are good.  
.˙. The next song will be good too.

---

## A linguistic example

<div id = "left">

Marc Dax (1770 - 1837): 3 patients  

Gustave Dax (1815 - 1893):140 patients  

Paul Broca (1824 - 1880): 1 patient

</div>


<div id = "right">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Plaque_Marc_Dax_Sommières.jpg/440px-Plaque_Marc_Dax_Sommières.jpg" width=""/>

</div>



---

## Hume's problem

<div id = "left">

- David Hume (1711-1776)
- Empiricist
- Skeptic

</div>

<div id = "right">


<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Painting_of_David_Hume.jpg/440px-Painting_of_David_Hume.jpg" width=""/>


</div>
---

## Black swans



<div id = "right">

All swans so far observed are white.  

.˙. All swans are white.

</div>



---

## Black swans



<div id = "right">

All swans so far observed are white.  

.˙. All swans are white.

</div>


<div id = "right">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Black_Swan_2_-_Pitt_Town_Lagoon.jpg/440px-Black_Swan_2_-_Pitt_Town_Lagoon.jpg" width=""/>

</div>


---

## Black swans

<div id = "left">

```
When any one asks me how I can best describe my experiences of nearly forty years at sea I merely say uneventful. Of course, there have been Winter gales and storms and fog and the like, but in all my experience I have never been in an accident of any sort worth speaking about. I have seen but one vessel in distress in all my years at sea, a brig, the crew of which was taken off in a small boat in charge of my third officer. I never saw a wreck and have never been wrecked, nor was I ever in any predicament that threatened to end in disaster of any sort.
- Captain E. J. Smith (writing in 1907)

```

</div>

<div id = "right">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/RMS_Titanic_3.jpg/600px-RMS_Titanic_3.jpg" width=""/>

RMS _Titanic_ 1912
</div>




---

## Knowledge production

<img src="https://ethanweed.github.io/Studium_Generale/StudiumGenerale2022/Slides/Images/knowledge-creation-1.png" width=""/>



---

## Proof

Induction will never prove anything.

---

## Proof

Induction has never and will never prove anything.

---

## Proof only exists in mathematics

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/P._Oxy._I_29.jpg/600px-P._Oxy._I_29.jpg" width=""/>

Papyrus Oxyrhynchus 29 (ca. 100 AD?)

---

## So what good is induction?


---

# Modelling induction

---

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/Slides/Images/SantaBall.png?raw=true" width="500"/>




---

# McElreath globe exercise
# re-envisioned as the SantaBall exercise

```python

import matplotlib.pyplot as plt
import numpy as np
import scipy

number_red = 0
throws = 0


prob = np.linspace(0, 1, num=10)
y = scipy.stats.binom.pmf(number_red, throws, prob)     # number of successes, number of trials, probability of a single success

fig, ax = plt.subplots()
ax.plot(prob, y)

ax.set(xlabel='probability', ylabel='binomial liklihood',
       title='Estimate of proportion of red on the Santa Ball')
ax.grid()

```

---

Null Hypothesis Significance Testing (NHST)

---

Null hypothesis (H0)
Alternative hypothesis (H1)

---

## Two types of errors

|             | retain H0        | reject H0        |
|-------------|------------------|------------------|
| H0 is true  | correct decision | error (type I)   |
| H0 is false | error (type II)  | correct decision |

---

alpha values 

p-values

---


# References

---


<div id = "refs">


[references still loading...]

</div>