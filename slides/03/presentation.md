---
title: "Response Time Distributional Analysis"
author: "Ethan Weed"
date: "date"
bibliography: refs.bib
csl: ../shared/apa.csl
theme: white
customTheme: "catppuccin-latte"
css: ../shared/slide-styles.css
revealjs-url: https://cdn.jsdelivr.net/npm/reveal.js@5
slideNumber: true
progress: true
---

# RTs and the mean

---

## Mental chronometry

:::::: {.two-col}

::: {}
![](images/helmholtz.jpg){width=70%}
_Hermann von Helmholtz_
:::

::: {}
![](images/donders.jpg)
_Franciscus Donders_
:::

::::::

---

## We love RTs and we love the mean!

notes from [@balotaYapMovingBeyond2011]

- 2010 survey of 285 articles in three leading journals
- 49% of studies used RT as a dependent measure
- Of those, 95% relied primarily on mean RT


---

## The normal distribution

:::::: {.two-col}

::: {}
![](images/normal_distribution.png)
_Normal distribution_
:::

::: {}

- Parameters: mean and standard deviation (mu and sigma)
- Summary statistics: mean and standard deviation
- Implicit model behind most reported statistics

:::

::::::

---



## RT distributions are positive (right) skewed

![](images/skew_mean_median.png)
_Skewed distributions_

# Beyond the mean

notes from [@balotaYapMovingBeyond2011]

---

## The ex-Gaussian function

:::::: {.two-col}

::: {}
![](images/exgaussian_pdf.png)
_Wikimedia Commons_
:::

::: {}

- Convolution of a Gaussian and an exponential distribution
- **mu, sigma** — mode and spread of the Gaussian component
- **tau** — mean (and spread) of the exponential component
- Fits empirical RT distributions well

:::

::::::

---

## Fig. 1 — patterns of change

:::::: {.two-col}

::: {}
![](images/balota_yap1.png)
:::

::: {}
![](images/balota_yap2.png)
:::

::::::

_Balota & Yap (2011) [@balotaYapMovingBeyond2011]_

- Shift: change in mu only
- Tail stretch: change in tau only
- Trade-off: mu and tau move in opposite directions — mean unchanged

---


## Examples

:::::: {.two-col}

::: {}
![](images/heathcote_1991.png)
_Stroop RT data [@heathcotePopielMewhort1991]_
:::

::: {}

- Semantic priming → pure shift
- Word frequency → shift + tail stretch
- Stroop-style effects → trade-offs that cancel in the mean

:::

::::::

---

# Our data: masked priming replication

notes from [@peelEffectsWordIdentity2022]

![](images/Peel_etal_2022.png)
_Subliminal priming [@peelEffectsWordIdentity2022]_

---

## Raw RT distribution

:::::: {.two-col}

::: {}
![](images/exgaussian_kde.png)
_Empirical KDE_
:::

::: {}
![](images/exgaussian_kde_fit.png)
_With theoretical ex-Gaussian fit (red)_
:::

::::::



---


## Quantile analysis

:::::: {.two-col}

::: {}

- Rank-order RTs per participant per condition
- Plot the deciles (.1, .2, … .9)
- Vincentile: compute quantiles per subject, then average across subjects

:::

::: {}
![](images/quantile_data.png)
:::

::::::

---

## Quantile plot — congruence

![](images/quantile_congruence.png)

---

## Raw group means

![](images/pointplot_params.png)


---

## Effects of each parameter

![](images/forest_plot.png)



---

## Raw mean vs mu

![](images/barplot_mean_vs_mu.png)



---

## A hidden effect

:::::: {.two-col}

::: {}
![](images/exgaussian_kde.png)
:::

::: {}
![](images/forest_plot.png)
:::

::: {}
![](images/balota_yap2.png)
:::

::::::

- theoretical mean = mu + tau
- Our numbers: mu ≈ −56 ms, tau ≈ +19 ms → mean ≈ −37 ms
- The raw mean understates the true modal-RT benefit of congruence
- Same pattern as Fig. 1 panel D (and Heathcote's stroop data)

---

# Beyond Balota & Yap: Testing the parameters

---

## Hypothesis tests

**raw mean**

| T | dof | p-val | CI95% | cohen-d | BF10 | power |
|---|---|---|---|---|---|---|
| -3.004 | 18 | 0.008 | [-62.59, -11.07] | 0.362 | 6.526 | 0.321 |

**mu**

| T | dof | p-val | CI95% | cohen-d | BF10 | power |
|---|---|---|---|---|---|---|
| -6.305 | 18 | <0.001 | [-74.52, -37.27] | 0.782 | 3466.506 | 0.897 |

---

## Takeaways

1. Skew is real and informative
2. Non-normal is not uninteresting
3. Effects on the mean can be a trade-off in disguise
4. Hidden effect in our data!

---

# References

::: {#refs}
:::
