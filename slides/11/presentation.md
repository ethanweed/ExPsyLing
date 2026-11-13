---
title: "Data visualization"
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
header-includes: |
  <style>
  .reveal .slides section img { max-width: 100%; max-height: 540px; }
  .reveal .caption { font-size: 0.7em; }
  .reveal .fixy img { height: 400px; width: auto; max-width: 100%; max-height: none; }
  .reveal .fixy button { font-family: inherit; font-size: 0.5em; color: #CD5909; background: white; border: 1.5px solid #CD5909; border-radius: 6px; padding: 4px 14px; margin-top: 8px; cursor: pointer; }
  .reveal .wugfit img { height: 470px; }
  .reveal .fixy button:hover { background: #CD5909; color: white; }
  .reveal .tiny { font-size: 0.45em; line-height: 1.3; display: inline-block; vertical-align: top; padding-top: 0.6em; }
  .reveal .vcenter { align-items: center; }
  .reveal .bwquote blockquote { font-size: 0.6em; width: 90%; }
  .reveal .testdesc { font-size: 0.8em; text-align: left; padding-top: 3em; }
  .reveal .testtable table { font-size: 0.6em; }
  .reveal .testtable td:first-child { white-space: nowrap; color: #4C827B; font-weight: bold; }
  .reveal .slides .plotstack p { margin: 0; line-height: 0; }
  .reveal .slides .plotstack img { max-width: 100%; max-height: none; height: 152px; width: auto; margin: 0 auto 4px; }
  .reveal .codecol pre { font-size: 0.42em; width: 100%; box-shadow: none; }
  .reveal details.codebox summary { font-size: 0.5em; color: #CD5909; cursor: pointer; }
  .reveal details.codebox pre { font-size: 0.4em; width: 100%; margin: 0; }
  .reveal .codecol pre code { max-height: 600px; }
  </style>
---

## Key concepts

- Graphics *reveal* data
- Graphics tell a *story*
- Lie factor
- Data-ink ratio
- Data density
- Revision

# A short history

## John Snow's cholera map

![](images/snow_map.jpg){height=520px}

[John Snow's 1854 map of cholera deaths]{.caption}

## Data visualization is a modern invention

:::: {.columns}
::: {.column width="50%"}
**William Playfair** (1759–1823)

- [millwright, engineer, draftsman, accountant, inventor, silversmith, merchant, investment broker, economist, statistician, pamphleteer, translator, publicist, land speculator, banker, ardent royalist, de facto intelligence officer, convict, editor, blackmailer and journalist (Wikipedia)]{.tiny}
- Founder of statistical graphics
- inventor of the bar graph, the pie chart, and the line chart
:::
::: {.column width="50%"}
![](images/playfair.jpg){width=80%}
:::
::::

## Edward Tufte

:::: {.columns .vcenter}
::: {.column width="50%"}
![](images/tufte_vdqi.jpg){style="height:440px; width:auto; max-height:none;"}
:::
::: {.column width="50%"}
![](images/tufte_portrait.jpg){style="height:400px; width:auto; max-height:none;"}

[Photo: Keegan Peterzell, CC BY-SA 4.0, via Wikimedia Commons]{.tiny}
:::
::::

[@tufte2001]{.caption}

# What graphics do

## Graphics *reveal* data

:::: {.columns}
::: {.column width="40%"}
![](images/Anscombe1.png)
:::
::: {.column width="60%"}
```{=html}
<iframe src="anscombe_demo.html" style="width:100%; height:440px; border:1px solid var(--ctp-surface2); border-radius:10px; background:white;"></iframe>
```
:::
::::

[Anscombe's quartet [@anscombe1973]]{.caption}

## The Datasaurus Dozen

![](images/DinoSequentialSmaller.gif){width=100%}

[Same summary statistics, very different data [@datasaurus2026]]{.caption}

## Datawug

```{=html}
<div class="fixy wugfit">
<img class="orig" src="images/wug_datasaurus.png">
<img class="fixed" src="images/wug_datasaurus_fit.png" style="display:none">
<button onclick="const d=this.parentNode, o=d.querySelector('.orig'), f=d.querySelector('.fixed'), show=f.style.display==='none'; f.style.display=show?'block':'none'; o.style.display=show?'none':'block'; this.textContent=show?'Hide regression line':'Add regression line';">Add regression line</button>
</div>
```

## Garbage in, garbage out

![](images/SillyPlot.png){height=520px}

[@tufte2001]{.caption}

## Garbage in, garbage out

![](images/SpuriousCorrelation1.png){width=80%}

[r = 0.80 ("strong") [@vigen2015]]{.caption}

## Graphics tell a *story*

![](images/TimesWeather.jpg){width=100%}

[A picture speaks 1888 numbers [@tufte2001]]{.caption}

## Graphics tell a *story*

![](images/MinardNapaleonsArmy.jpg){width=100%}

[Charles Joseph Minard (1869). Translation by Dawn Finley, redrawing by Elaine Morse]{.caption}

## Four variables, one picture

:::: {.columns}
::: {.column width="60%"}
![](images/MinardNapaleonsArmy.jpg)
:::
::: {.column width="40%"}
- Size of the army
- Location
- Direction of movement
- Temperature during the retreat
:::
::::

## Best and worst

:::: {.columns}
::: {.column width="50%" .bwquote}
![](images/MinardNapaleonsArmy.jpg)

> "It may well be the best statistical graphic ever drawn"
:::
::: {.column width="50%" .fragment .bwquote}
![](images/TheWorstGraphicEver.png){style="height:330px; width:auto;"}

> "It may well be the worst graphic ever to find its way into print"
:::
::::

[@tufte2001]{.caption}

## The worst graphic ever

![](images/TheWorstGraphicEver.png){height=540px}

# What makes a good graphic?

## Most information, least time

![](images/LookingAtPlots.png){height=520px}

[@tufte2001]{.caption}

## A good graphic is truthful

::: {.formula style="font-size:1.3em"}
$$\text{lie factor} = \frac{\text{size of effect shown in graph}}{\text{size of effect in data}}$$
:::

[@tufte2001]{.caption}



## No y-axis labels

:::: {.columns .vcenter}
::: {.column width="40%"}
::: {.formula style="font-size:0.7em"}
$$\text{lie factor} = \frac{\text{size of effect shown in graph}}{\text{size of effect in data}}$$
:::
:::
::: {.column width="60%"}
```{=html}
<div class="fixy">
<img class="orig" src="images/buzz1.jpg">
<img class="fixed" src="images/fixed_buzz1.png" style="display:none">
<button onclick="const d=this.parentNode, o=d.querySelector('.orig'), f=d.querySelector('.fixed'), show=f.style.display==='none'; f.style.display=show?'block':'none'; o.style.display=show?'none':'block'; this.textContent=show?'Show original':'Fix y axis';">Fix y axis</button>
</div>
```
:::
::::

[@notopoulos2014]{.caption}

## Very selective y-axis labels

:::: {.columns .vcenter}
::: {.column width="40%"}
::: {.formula style="font-size:0.7em"}
$$\text{lie factor} = \frac{\text{size of effect shown in graph}}{\text{size of effect in data}}$$
:::
:::
::: {.column width="60%"}
```{=html}
<div class="fixy">
<img class="orig" src="images/buzz2.jpg">
<img class="fixed" src="images/fixed_buzz2.png" style="display:none">
<button onclick="const d=this.parentNode, o=d.querySelector('.orig'), f=d.querySelector('.fixed'), show=f.style.display==='none'; f.style.display=show?'block':'none'; o.style.display=show?'none':'block'; this.textContent=show?'Show original':'Fix y axis';">Fix y axis</button>
</div>
```
:::
::::

[@notopoulos2014]{.caption}

## Again, no y-axis labels

:::: {.columns .vcenter}
::: {.column width="40%"}
::: {.formula style="font-size:0.7em"}
$$\text{lie factor} = \frac{\text{size of effect shown in graph}}{\text{size of effect in data}}$$
:::
:::
::: {.column width="60%"}
```{=html}
<div class="fixy">
<img class="orig" src="images/buzz3.jpg">
<img class="fixed" src="images/fixed_buzz3.png" style="display:none">
<button onclick="const d=this.parentNode, o=d.querySelector('.orig'), f=d.querySelector('.fixed'), show=f.style.display==='none'; f.style.display=show?'block':'none'; o.style.display=show?'none':'block'; this.textContent=show?'Show original':'Fix y axis';">Fix y axis</button>
</div>
```
:::
::::

[@notopoulos2014]{.caption}

## Two different y-axes

:::: {.columns .vcenter}
::: {.column width="40%"}
::: {.formula style="font-size:0.7em"}
$$\text{lie factor} = \frac{\text{size of effect shown in graph}}{\text{size of effect in data}}$$
:::
:::
::: {.column width="60%"}
![](images/reddit_axes.jpg){style="height:420px; width:auto; max-width:100%; max-height:none;"}
:::
::::

[@dst]{.caption}

## Tufte's five principles

- Above all else show the data
- Maximize the data-ink ratio
- Erase non-data ink
- Erase redundant data-ink
- Revise and edit

[@tufte2001]{.caption}

## Maximize data density

::: {.formula style="font-size:1.3em"}
$$\text{data density} = \frac{\text{number of data points}}{\text{area of data graphic}}$$
:::

## Low data density

:::: {.columns .vcenter}
::: {.column width="40%"}
::: {.formula style="font-size:0.7em"}
$$\text{data density} = \frac{\text{number of data points}}{\text{area of data graphic}}$$
:::
:::
::: {.column width="60%"}
![](images/LowDataDensity.png){style="height:420px; width:auto; max-width:100%; max-height:none;"}
:::
::::

[0.02 numbers per cm² [@tufte2001]]{.caption}

## High data density

:::: {.columns .vcenter}
::: {.column width="35%"}
::: {.formula style="font-size:0.7em"}
$$\text{data density} = \frac{\text{number of data points}}{\text{area of data graphic}}$$
:::
:::
::: {.column width="65%"}
![](images/TimesWeather.jpg){style="width:100%; height:auto; max-width:100%; max-height:none;"}
:::
::::

[28 numbers per cm²]{.caption}

## Revision

:::: {.columns}
::: {.column width="50%"}
![](images/Playfair1.jpg)

[Playfair (1785)]{.caption}
:::
::: {.column width="50%" .fragment}
![](images/Playfair2.jpg)

[Playfair (1786)]{.caption}
:::
::::

# Plotting paired data

## Fake data: a Stroop-like experiment

:::: {.columns}
::: {.column width="60%" .codecol}
```python
import numpy as np, pandas as pd
import seaborn as sns
import pingouin as pg

rng = np.random.default_rng(11)
n = 20
base = rng.normal(600, 80, n)   # subjects differ a lot
incon = base + rng.normal(0, 20, n)
con = base - 30 + rng.normal(0, 20, n)  # small, consistent effect

df = pd.DataFrame({"subject": range(n),
                   "Congruent": con,
                   "Incongruent": incon})
# long format: one row per observation
long = df.melt("subject", var_name="condition",
               value_name="rt")

pg.ttest(df.Incongruent, df.Congruent, paired=True)
```
:::
::: {.column width="40%"}
- 20 participants
- Each sees **both** conditions
- Paired *t*-test: *t*(19) = 4.90, *p* < .001
- Mean difference = 23 ms
:::
::::

## Don't do this

![](images/paired_bad_bar.png){height=560px}

## Bar plot

:::: {.columns}
::: {.column width="50%" .codecol}
```python
pal = {"Congruent": "#4C827B", "Incongruent": "#CD5909"}

sns.barplot(long, x="condition", y="rt",
            hue="condition", palette=pal,
            errorbar="se")
```
:::
::: {.column width="50%"}
![](images/paired_bar.png)

[Means ± SE. Where are the data?]{.caption}
:::
::::

## Bar plot, zoomed in

:::: {.columns}
::: {.column width="50%" .codecol}
```python
pal = {"Congruent": "#4C827B", "Incongruent": "#CD5909"}

ax = sns.barplot(long, x="condition", y="rt",
                 hue="condition", palette=pal,
                 errorbar="se")
ax.set(ylim=(560, 640))
```
:::
::: {.column width="50%"}
![](images/paired_bar_zoom.png)

[Same data. Lie factor?]{.caption}
:::
::::

## Box plot

:::: {.columns}
::: {.column width="50%" .codecol}
```python
pal = {"Congruent": "#4C827B", "Incongruent": "#CD5909"}

sns.boxplot(long, x="condition", y="rt",
            hue="condition", palette=pal,
            width=0.5)
```
:::
::: {.column width="50%"}
![](images/paired_box.png)

[Shows distributions, but hides within-participant effects]{.caption}
:::
::::

## Violin + strip plot

:::: {.columns}
::: {.column width="50%" .codecol}
```python
pal = {"Congruent": "#4C827B", "Incongruent": "#CD5909"}

sns.violinplot(long, x="condition", y="rt",
               hue="condition", palette=pal,
               inner=None, alpha=0.3)
sns.stripplot(long, x="condition", y="rt",
              hue="condition", palette=pal,
              size=7, jitter=0.08)
```
:::
::: {.column width="50%"}
![](images/paired_violin_strip.png)

[All the data, but also hides within-participant differences]{.caption}
:::
::::

## Paired lines

:::: {.columns}
::: {.column width="50%" .codecol}
```python
pal = {"Congruent": "#4C827B", "Incongruent": "#CD5909"}

# one grey line per subject
sns.lineplot(long, x="condition", y="rt",
             units="subject", estimator=None,
             color="#9ca0b0", lw=1)
sns.stripplot(long, x="condition", y="rt",
              hue="condition", palette=pal,
              size=7, jitter=False)
# group means ± SE
sns.pointplot(long, x="condition", y="rt",
              color="black", errorbar="se",
              markers="D")
```
:::
::: {.column width="50%"}
![](images/paired_lines.png)

[Now the pairing is visible: most lines go up]{.caption}
:::
::::

## Paired lines, with and without violins

:::: {.columns}
::: {.column width="50%"}
![](images/paired_lines.png)
:::
::: {.column width="50%"}
![](images/paired_violin_lines.png)
:::
::::

<details class="codebox"><summary>Code for violin + lines</summary>
```python
sns.violinplot(long, x="condition", y="rt",
               hue="condition", palette=pal,
               inner=None, alpha=0.3)
sns.lineplot(long, x="condition", y="rt",
             units="subject", estimator=None,
             color="#9ca0b0", lw=1)
sns.stripplot(long, x="condition", y="rt",
              hue="condition", palette=pal,
              size=7, jitter=False)
```
</details>

## Three ways to show the pairing

:::: {.columns}
::: {.column width="33%"}
![](images/paired_lines.png)

[Paired lines]{.caption}
:::
::: {.column width="33%"}
![](images/paired_violin_lines.png)

[Violin + lines]{.caption}
:::
::: {.column width="33%"}
![](images/paired_raincloud.png)

[Raincloud]{.caption}
:::
::::

## Scatter against the identity line

:::: {.columns}
::: {.column width="50%" .codecol}
```python
below = df.Incongruent < df.Congruent
ax = sns.scatterplot(df, x="Congruent",
                     y="Incongruent", hue=below,
                     palette={False: "#1e66f5",
                              True: "#d20f39"},
                     s=70, legend=False)
lo, hi = 390, 765
ax.plot([lo, hi], [lo, hi],
        color="#9ca0b0", ls="--")   # y = x
ax.set(xlim=(lo, hi), ylim=(lo, hi),
       aspect="equal")
```
:::
::: {.column width="50%"}
![](images/paired_scatter.png)

[Points above the line: slower when incongruent]{.caption}
:::
::::

## Difference scores

:::: {.columns}
::: {.column width="50%" .codecol}
```python
diff = df.Incongruent - df.Congruent

sns.stripplot(y=diff, color="#1e66f5",
              size=7, jitter=0.08)
# mean difference with 95% CI
ax = sns.pointplot(y=diff, color="#CD5909",
                   errorbar=("ci", 95),
                   markers="D")
ax.axhline(0, color="#9ca0b0", ls="--")
```
:::
::: {.column width="50%"}
![](images/paired_diff.png)

[What the paired t-test actually tests, but maybe less intuitive to read?]{.caption}
:::
::::


# Reading figures

## Which test?

::: {.testtable}
| Test | When to use it |
|------|----------------|
| Paired *t*-test | Two conditions, **same** participants in both; continuous outcome |
| Independent *t*-test | Two groups of **different** participants; continuous outcome |
| One-way ANOVA | Three or more groups (one factor); continuous outcome |
| Two-way ANOVA | Two factors at once; tests each main effect and their interaction |
| Linear regression | Continuous outcome predicted by one or more continuous (or categorical) predictors |
| Logistic regression | Binary outcome (0/1, yes/no, correct/incorrect) predicted by one or more continuous (or categorical) predictors |
:::

## Paired *t*-test

:::: {.columns}
::: {.column width="70%"}
![](images/read_paired.png){style="height:470px; width:auto; max-width:none; max-height:none;"}
:::
::: {.column width="30%" .plotstack}
![](images/paired_bar.png)
![](images/paired_violin_strip.png)
![](images/paired_box.png)
:::
::::

[Same people, different conditions]{.caption}

## Independent *t*-test

:::: {.columns}
::: {.column width="60%"}
![](images/read_indep.png){style="height:440px; width:auto; max-width:100%; max-height:none;"}
:::
::: {.column width="40%" .testdesc}
- Two groups of **different** participants
- Continuous outcome
:::
::::

[Different people in each group.]{.caption}

## One-way ANOVA

:::: {.columns}
::: {.column width="60%"}
![](images/read_anova1.png){style="height:440px; width:auto; max-width:100%; max-height:none;"}
:::
::: {.column width="40%" .testdesc}
- Three or more groups (one factor)
- Continuous outcome
:::
::::

[Do the group means differ more than the noise within groups?]{.caption}

## Two-way ANOVA

:::: {.columns}
::: {.column width="60%"}
![](images/read_anova2.png){style="height:440px; width:auto; max-width:100%; max-height:none;"}
:::
::: {.column width="40%" .testdesc}
- Two factors at once
- Tests each main effect and their interaction
:::
::::

[Two main effects + an interaction]{.caption}

## Linear regression

:::: {.columns}
::: {.column width="60%"}
![](images/read_lm.png){style="height:440px; width:auto; max-width:100%; max-height:none;"}
:::
::: {.column width="40%" .testdesc}
- Continuous outcome
- One or more continuous (or categorical) predictors
:::
::::

[How much does *y* change per unit of *x*?]{.caption}

## Logistic regression

:::: {.columns}
::: {.column width="60%"}
![](images/read_logit.png){style="height:440px; width:auto; max-width:100%; max-height:none;"}
:::
::: {.column width="40%" .testdesc}
- Binary outcome (0/1, yes/no, correct/incorrect)
- One or more continuous (or categorical) predictors
:::
::::

[How does the probability of a 1 change with *x*?]{.caption}


## Categorical predictors

:::: {.columns}
::: {.column width="50%"}
![](images/read_logit_cat1.png){style="height:420px; width:auto; max-width:100%; max-height:none;"}

[One factor (grey = one participant)]{.caption}
:::
::: {.column width="50%"}
![](images/read_logit_cat2.png){style="height:420px; width:auto; max-width:100%; max-height:none;"}

[Two factors]{.caption}
:::
::::

# References

## References {.scrollable}

::: {#refs}
:::
