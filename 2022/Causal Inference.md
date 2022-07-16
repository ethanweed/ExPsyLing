

https://www.youtube.com/watch?v=KNPYUVmY3NM

Ptolomeic model predicts the regression of Mars very accurately, but is completely wrong.

Knowing a cause means being able to predict the consequences of an intervention. What happens if I do _this_?

Non-causal statistics

Adversarial image research neural networks

AIC would happily chose Ptolomey's model of the solar system


DAG's make no statements about _how_ a variable influences an outcome

```mermaid
graph LR
Rain-->Wet
```

```mermaid
graph LR
boxa(Power)-->boxb(Lamp on)
boxc(Bulb)-->boxb(Lamp on)
```
Reserachers with lots of domain knowledge can make very complicated DAGs

McElreath (1:10) in https://www.youtube.com/watch?v=KNPYUVmY3NM:
"Hang on! Which part of this do we care about?"

"Obviously the whole world is one causal system, but you don't have to analyze it at once!"


Fork:

```mermaid
graph LR
boxa(z)-->boxb(x)
boxa(z)-->boxc(y)
```

Pipe:

```mermaid
graph LR
boxa(x)-->boxb(z)
boxb(z)-->boxc(y)
```

Collider:

```mermaid
graph LR
boxa(x)-->boxb(z)
boxc(y)-->boxb(z)
```




The fork and the pipe **look the same** in the data alone. We need _other_ scientific knowledge to distinguish them.

Collider example: Restaurants

```mermaid
graph LR
boxa(Location)-->boxb($Profit$)
boxc(Food quality)-->boxb(Profit $)
```

A restaurant in a good location does not need to have good food to survive.
A restaurant in a bad location needs something else (e.g. good food) to survive.
The only restaurants that survive have at least one of these.
In the restaurants that survive, there tends to be a negative correlation between how good the location is, and how good the food is.
Selection bias.

