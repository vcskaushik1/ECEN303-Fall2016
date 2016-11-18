# Programming Challenge 4


In this [Python](https://www.python.org) challenge, you will generate continuous random variables.
As before, this challenge will leverage the Python `random` and `math` modules, along with the `numpy` and `pylab` libraries.


```python
import random
import math
import numpy
import pylab
```


Generate pseudo-random numbers using `random.random()`. This method returns a random floating point number in the range [0.0, 1.0).


```python
TrialNumber = 10000
Uvariable = []
for trial in range(0, TrialNumber):
    Uvariable.append(random.random())


numBins = #number of evenly sized bins for histogram
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)
```


Next, use a real-valued function `V = g(U)` to produce a sequence of exponential variables. This process is explained in Section 9.3 in the notes. The form of the function `g()` can be derived from the CDF of V. For these exponential random variables, their common CDF should be `F_V(v) = 1 - math.exp(- lambda * v)`.


```python
for trial in range(0, len(Uvariable)):
    Vvariable.append(g(Uvariable[trial])


numBins = #number of evenly sized bins for histogram
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)
```


Again, use a real-valued function `W = h(U)` to produce a sequence of Rayleigh random variables. For these Rayleigh random variables, their common CDF should be  `F_W(w) = 1 - math.exp(- 0.5 * (w**2))` for `w > 0`.


```python
for trial in range(0, len(Uvariable)):
    Wvariable.append(h(Uvariable[trial])


numBins = #number of evenly sized bins for histogram
plt.hist(Wvariable, numBins, normed=1, facecolor='green', alpha=0.75)
```


In this part, uniform random variables will be employed to create random variables with different distributions. 


```python
Uknown1 = []
Uknown2 = []
for trial in range(0, TrialNumber):
    Uvariable1 = random.random()
    Uvariable2 = random.random()
    Unkown1.append(math.sqrt(- 2 * math.ln(Uvariable1) * math.cos(2 * math.PI * Uvariable2))
    Unkown2.append(math.sqrt(- 2 * math.ln(Uvariable1) * math.cos(2 * math.PI * Uvariable2))


numBins = #number of evenly sized bins for histogram
plt.hist(Unkown1, numBins, normed=1, facecolor='green', alpha=0.75)
numBins = #number of evenly sized bins for histogram
plt.hist(Unkown2, numBins, normed=1, facecolor='green', alpha=0.75)
```


Plot the empirical distributions associated with `Unkown1` and `Unkown2` using binning/quantization or cumulative distribution functions.


* What is the type of random variable `Unkown1`?
* What is its mean and variance?
* What is the type of random variable `Unkown2`?
* What is its mean and variance?


