For lecture 8, I did the McElreath globe-spinning task. Would be better with an inflatable globe, but the spinning one gives the opportunity to discuss measurement error / bias


Re-wrote the globe-spinning script in Python:

```python
# McElreath globe exercise



import matplotlib.pyplot as plt
import numpy as np
import scipy

number_water = 9
spins = 23


prob = np.linspace(0, 1, num=10)
y = scipy.stats.binom.pmf(number_water, spins, prob)

fig, ax = plt.subplots()
ax.plot(prob, y)

ax.set(xlabel='probability', ylabel='binomial liklihood',
       title='Estimate of water proportion')
ax.grid()

```

Talked about inductive inference, Hume's problem, Karl Popper and  falsification, and NHST.

We got as far as defining null hypotheses and talking about p-values.

For Thursday: 

- discuss alpha values
- two interpretations of p-values (Neymann and Fischer)

| Value of $\alpha$ | 0.05 | 0.04 | 0.03 | 0.02 | 0.01 |
|--------------------|------|------|------|------|------|
| Reject the null?   | Yes  | Yes  | Yes  | No   | No   |

- discuss type 1 and type 2 errors

|             | retain H0        | reject H0        |
|-------------|------------------|------------------|
| H0 is true  | correct decision | error (type I)   |
| H0 is false | error (type II)  | correct decision |


|             | retain H0                                     | reject H0                     |
|-------------|-----------------------------------------------|-------------------------------|
| H0 is true  | $1-\alpha$ (probability of correct retention) | $\alpha$ (type I error rate)  |
| H0 is false | $\beta$ (type II error rate)                  | $1-\beta$  (power of the test)|

- discuss hypothesis testing, starting with globe data:

```python
# Frequentist test

from scipy.stats import binom_test
pvalue = binom_test(x = number_water, n = spins, p = 0.5, alternative = 'two-sided')
print("probability of measuring values as extreme as our data if the null hypothesis is true, aka the p-value:", pvalue)

```

```python
# Bayes factor

import pingouin as pg
bf = float(pg.bayesfactor_binom(k = number_water, n = spins, p=0.5))
print("BF-null: %.3f, BF-alt: %.3f" % (1 / bf, bf))

```

- Bayes factors allow us to do what we really want: talk about how probable _our_ hypothesis is, compared to the null, instead of talking about _failure to reject the null_
