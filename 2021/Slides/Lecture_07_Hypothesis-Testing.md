## Hypothesis Testing

<style>
.container{
  display: flex;
}
.col {
  flex: 1;
}
</style>

---

> Facts cannot be explained by a hypothesis more extraordinary than these facts themselves; and of various hypotheses the least extraordinary must be adopted

> Charles S. Peirce, quoted in Sebeok & Umiker-Sebeok (1979).


---


#### A simple ESP experiment

:::incremental
1. Participant sees a card that is black on one side and white on the other. 
2. The experimenter takes the card away, and places it black side up or white side up completely at random in the room next door. 
3. A second experimenter comes in and asks the participant which side of the card is now facing upwards. 
4. Each participant sees only one card, and gives only one answer
:::

---

#### Research hypotheses versus statistical hypotheses

- If ESP _does not_ exist, then each participant's chances of answering correctly are 50/50.

- If ESP _does_ exist, then each participant's chances of answering correctly are _not_ 50/50

---

#### Research hypotheses versus statistical hypotheses

- My research hypothesis: “ESP exists”

- My statistical hypothesis: 𝜃 ≠ 0.5


---

#### What are Sternberg's research and statistical hypotheses?

<img src="https://github.com/ethanweed/ExPsyLing/blob/master/2021/Slides/Images/Sternberg_Experiment1.png?raw=true" width="400"/>

---

#### Sternberg's research and statistical hypotheses

Something like...

:::incremental
- Research hypothesis: People need to scan through the contents of their working memory to access it: they cannot access it all at once
- Statistical hypothesis: The slope of the straight line modelling the relation between set size and response time will not be 0: slope ≠ 0
:::

---


#### ESP in space

Astronaut Edgar Mitchell and his  
ESP experimental materials

::: {.container}
:::: {.col}
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Edgar_Mitchell_S70-55388.jpg/797px-Edgar_Mitchell_S70-55388.jpg" width=""/>
::::
:::: {.col}
<img src="https://www.cabinetmagazine.org/issues/5/cabinet_005_backstrom_fia_001.jpg" width=""/>
::::
:::

---

#### ESP in space results

Out of 4 psychics trying to guess which symbols Mitchell was sending to them telepathically from space...

:::incremental
- 2 did better than chance
- 2 did not.
:::

---

#### Null hypothesis significance testing (NHST)

:::incremental
- I think that maybe ESP exists
- I collect some data
- I test whether my data supports the hypothesis that ESP _does not_ exist
:::

---

#### Null hypotheses and alternative hypotheses

- My research hypothesis: “ESP exists”

---

#### Null hypotheses and alternative hypotheses

- ~~My research hypothesis: “ESP exists”~~

---
	
#### Null hypotheses and alternative hypotheses

::: {.container}
:::: {.col}
:::incremental
- My null hypothesis ( $H_0$ ): "ESP does not exist"

- My alternative hypothesis ( $H_1$ ): “ESP exists"
:::
::::
:::: {.col}
:::incremental
- The goal of a hypothesis test is _not_ to show that the alternative hypothesis is (probably) true
- The goal is to show that the null hypothesis is (probably) false.
:::
::::
:::


---

#### What NHST cannot do

:::incremental
- NHST can _never_ prove anything
- NHST can _never_ tell you the probability that the null hypothesis is true
- NHST can _never_ tell you the probability that the alternative hypothesis is true
:::

---

#### What NHST can do

:::incremental
- NHST can _only_ tell you how unlikely the data you have observed would be if the null hypothesis were in fact true
:::

---

#### The ESP experiment can be modelled with a binomial distribution



$P(X | \theta, N) = \frac{N!}{X! (N-X)!}  \theta^X (1-\theta)^{N-X}$


---

#### The ESP experiment can be modelled with a binomial distribution




::: {.container}
:::: {.col}

$$
P(X | \theta, N)
$$
	
::::
:::: {.col}



::::
:::


---

#### We can estimate results if  $H_0$  is true by sampling from the binomial distribution

::: {.container}
:::: {.col}

	# sample from a binomial distribution
	
	data = random.binomial(n=100, p=.5, size=10000)

	esp = sns.histplot(data, bins=20,binwidth=0.5)
	
	esp.set(xlim=(20,80))
	
::::
:::: {.col}

<img src="https://ethanweed.github.io/pythonbook/_images/04.04-hypothesis-testing_11_1.png" width=""/>

::::
:::

---


#### Two types of errors


::: {.container}
:::: {.col}

|             | retain H0        | reject H0        |
|-------------|------------------|------------------|
| H0 is true  | correct decision | error (type I)   |
| H0 is false | error (type II)  | correct decision |

::::
:::


---

|             | retain H0                                     | reject H0                     |
|-------------|-----------------------------------------------|-------------------------------|
| H0 is true  | $1-\alpha$ (probability of correct retention) | $\alpha$ (type I error rate)  |
| H0 is false | $\beta$ (type II error rate)                  | $1-\beta$  (power of the test)|

---

#### Choosing an  $\alpha$  determines what we will consider statistically significant.


<img src="https://ethanweed.github.io/pythonbook/_images/04.04-hypothesis-testing_15_1.png" width=""/>

---








---




**One-sample t-test**


$$
t = {\frac {{\bar {x}}-\mu _{0}}{s/{\sqrt {n}}}}
$$

---



---



---

#### References

Navarro, D., & Weed, E. (2021). Learning statistics with python: A tutorial for psychology students and other beginners[Available online: https://ethanweed.github.io/pythonbook]

Sebeok, T. A., & Umiker-Sebeok, J. (1979). “You know my method”: a juxtaposition of Charles S. Peirce and Sherlock Holmes.

Wittgenstein, L. (2013). _Tractatus logico-philosophicus_. Routledge.