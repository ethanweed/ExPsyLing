[[Planning]]

## Deconstructing response time

What are some of the many factors that affect response time? That is, what are we _actually_ measuring, when we measure response time?

## Model 1

```mermaid
graph BT
Cognition-->RT
Motor-->RT
```


## Model 2

```mermaid
graph BT
Cognition-->RT
Motor-->RT
Perception-->Cognition
Decision-->Cognition
```

## Model 3

```mermaid
graph BT
Cognition-->RT
Motor-->RT
Perception-->Cognition
Decision-->Cognition
Age-.->Motor
Age-.->Decision
Age-.->Perception
```
## Model 4

```mermaid
graph BT
Cognition-->RT
Motor-->RT
Perception-->Cognition
Decision-->Cognition
Age-.->Motor
Age-.->Decision
Age-.->Perception
Sleep-.->Motor
Sleep-.->Decision
Sleep-.->Perception
```

## Model 5


```mermaid
graph BT
Cognition-->RT
Motor-->RT
Perception-->Cognition
Decision-->Cognition
Age-.->Motor
Age-.->Decision
Age-.->Perception
Sleep-.->Motor
Sleep-.->Decision
Sleep-.->Perception
Attention-.->Perception
Attention-.->Decision
Sleep-.->Attention
```

## Model 6

```mermaid
graph BT
Cognition-->RT
Motor-->RT
Perception-->Cognition
Decision-->Cognition
Age-.->Motor
Age-.->Decision
Age-.->Perception
Age-.->Sleep-.->Attention
Sleep-.->Motor
Sleep-.->Decision
Sleep-.->Perception
Attention-.->Perception
Attention-.->Decision
Sleep-.->Attention
```


---

## Experiment 1a: Hypotheses

### Cognitive model
Making a decision in response to a cue requires more cognitive effort than simply responding immediately to the cue, therefore we expect that on average, RT will be slower when a decision is required.

```mermaid
graph BT
boxd(Perception)--Motor-->boxe(button press)
boxa(Perception)--Cognitive Processing-->boxb(Decision)--Motor-->boxc(button press)
```

### Statistical model(s)

## $RT_{Perception} < RT_{Perception + Decision}$
(One-tailed)

## $RT_{Perception} ≠ RT_{Perception + Decision}$
(Two-tailed)


---

## Experiment 1b: Hypotheses

### Cognitive model
Deciding whether a string of letters is a word or not is more cogntively demanding than recognizing a color. Therefore, we expect RT to slower in a lexical decision task than in a color recognition task.

```mermaid
graph BT
boxa(Perception)-->boxb(Color recognition)--Motor-->boxc(button press)
boxd(Perception)-->boxe(Letter recognition)-->boxf(Pattern matching)--Motor-->boxg(button press)
```

### Statistical model(s)

## $RT_{ColorCategorization} < RT_{LexicalDecision}$
(One-tailed)

## $RT_{ColorCategorization} ≠ RT_{LexicalDecision}$
(Two-tailed)


