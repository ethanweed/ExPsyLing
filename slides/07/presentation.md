---
title: "Language Parsing as Prediction"
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

# Language Parsing as Prediction

## Predictive coding

:::: {.columns}
::: {.column width="50%"}
![](images/Lupyan and Clark Fig 3.png)
:::
::: {.column width="50%"}
![](images/Lupyan and Clark Fig 1.png)
:::
::::

[@lupyanWordsWorldPredictive2015]

## Connectionism

![](images/Plaut 2001 fig 3.gif)

[@plautCognitiveFunctionsNormal2001]

# N400s and ERPs

## EEG

![](images/ethan_eeg.jpg)

## EEG

![](images/raw_eeg.png)

## Stimuli

![](images/stage1_stimulus.gif){data-replay=""}

Animation created with Claude Code (Anthropic, Claude Opus 5.5)

## Raw data

![](images/stage2_raw.gif){data-replay=""}

Animation created with Claude Code (Anthropic, Claude Opus 5.5)

## Epoching

![](images/stage3_epoch.gif){data-replay=""}

Animation created with Claude Code (Anthropic, Claude Opus 5.5)

## Averaging

![](images/stage4_average.gif){data-replay=""}

Animation created with Claude Code (Anthropic, Claude Opus 5.5)

## Comparison

![](images/stage5_compare.gif){data-replay=""}

Animation created with Claude Code (Anthropic, Claude Opus 5.5)

## Scalp maps

![](images/stage6_scalp.gif){data-replay=""}

Animation created with Claude Code (Anthropic, Claude Opus 5.5)

# DeLong et al (2005)

## N400s: Prediction or Integration?

[@delongProbabilisticWordPreactivation2005]

## Cloze probability

- "The day was breezy, so the boy went outside to fly ___"
- "The day was breezy, so the boy went outside to fly a/an ___"

Cloze probabilities from 0 - 96 (article)/100 (noun)%

[@delongProbabilisticWordPreactivation2005]

## N400s

![](images/DeLong Fig1a.png)

[@delongProbabilisticWordPreactivation2005]

## Correlation with Cloze

![](images/DeLong Fig1b.png)

[@delongProbabilisticWordPreactivation2005]

## Scalp maps

![](images/DeLong Fig1c.png)

[@delongProbabilisticWordPreactivation2005]

# Integrating Prediction and Connectionism

## Prediction

![](images/Plaut 2001 fig 3.gif)

[@plautCognitiveFunctionsNormal2001]

## Prediction

![](images/delong_triangle_2_a.png)

adapted from [@plautCognitiveFunctionsNormal2001]

Animation created with Claude Code (Anthropic, Claude Opus 5.5)

## Prediction Error

![](images/delong_triangle_2_an.png)

adapted from [@plautCognitiveFunctionsNormal2001]

Animation created with Claude Code (Anthropic, Claude Opus 5.5)

# References

## References {.scrollable}

::: {#refs}
:::

```{=html}
<script>
// Restart play-once GIFs each time their slide is entered.
window.addEventListener('load', () => {
  const gifs = new Map();
  document.querySelectorAll('img[data-replay]').forEach(img => gifs.set(img, img.src));
  async function replay(slide) {
    for (const img of slide.querySelectorAll('img[data-replay]')) {
      const blob = await (await fetch(gifs.get(img))).blob();
      if (img.dataset.blobUrl) URL.revokeObjectURL(img.dataset.blobUrl);
      img.dataset.blobUrl = URL.createObjectURL(blob);
      img.src = img.dataset.blobUrl;
    }
  }
  Reveal.on('slidechanged', e => replay(e.currentSlide));
  replay(Reveal.getCurrentSlide());
});
</script>
```
