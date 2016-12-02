
# Challenge 6 – Limit Theorems
The **Law of Large Numbers** (LLN) and the **Central Limit Theorem** (CLT) are two fundamental results in probability.
The first theorem characterizes the convergence of empirical averages, whereas the second theorem seeks to capture the behavior of large sums of small, independent random components.
In this challenge, we explore these two results numerically.

## Gaussian Random Variables
The Gaussian distribution belongs to the family of stable distributions, which are the attractors of sums of independent, identically distributed random variables.
In particular, adding independent Gaussian random variables produces a Gaussian random variable.
This property makes sums of Gaussian random variables ideal to gain insight into limit theorems.

Below, we consider two distinct objects: an empirical average and a scaled sum.
The empirical average is obtained by adding *n* independent normal random variables and, subsequently, normalizing the sum by *n*.
Likewise, the scaled sum is produced by adding *n* independent normal random variables and, subsequently, dividing the sum by the square root of *n*.
This procedure is repeated over several *runs* and histograms of the outcomes are plotted.
Try to compute the means and variances associated with these two operations before executing the *code*, and verify that your intuition is correct.


```python
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

runs = 10000 # Number of points in histograms
sample = 100 # Number of random variables in each sum

average = [] # List of empirical averages
scaledsums = [] # List of empirical scaled sums
mean = 0.0
stddev = 1.0

for iteration in range(0, runs):
    sequence = []
    summation = 0.0
    for index in range(0, sample):
        trial = (random.gauss(mean, stddev) - mean) / stddev
        sequence.append(trial)
        summation += trial
    average.append(summation / sample) # LLN
    scaledsums.append(summation / math.sqrt(sample)) # CLT

bins = np.linspace(-5 / math.sqrt(sample), 5 / math.sqrt(sample), 100)
plt.hist(average, bins, normed=1, facecolor='blue', alpha=0.5)
plt.xlabel('Quantized Value')
plt.ylabel('Probability Density Function')
plt.show() # LLN

bins = np.linspace(-5, 5, 100)
plt.hist(scaledsums, bins, normed=1, facecolor='green', alpha=0.5)
plt.xlabel('Quantized Value')
plt.ylabel('Probability Density Function')
normal = mlab.normpdf(bins, 0.0, 1)
plt.plot(bins, normal, 'k--')
plt.show() # CLT

```

### Questions – Gaussian Random Variables
* What is the expected value of the empirical average?
  - ANSWER-01:
* What is the standard deviation of the empirical average?
  - ANSWER-02:
* What is the limit distribution of the empirical average as *n* becomes large?
  - ANSWER-03:
* What is the expected value of the empirical scaled sum?
  - ANSWER-04:
* What is the standard deviation of the empirical scaled sum?
  - ANSWER-05:
* In the limit, what is the distribution of the empirical scaled sum as *n* becomes large?
  - ANSWER-06:

## Bernoulli Random Variables
In this section, we repeat the above procedure with Bernoulli random variables.
Note that, while computing empirical sums, every trial is first centralized by subtracting the mean and, then, normalized by dividing by the standard deviation.
The empirical average is obtained by adding *n* such trials and normalizing the resulting sum by *n*.
The scaled sum is produced by adding *n* trials, but dividing the sum by the square root of *n* instead.
This procedure is repeated over several *runs* and histograms of the outcomes are plotted.


```python
runs = 1000 # Number of points in histograms
sample = 10000 # Number of random variables in each sum

average = [] # List of empirical averages
scaledsums = [] # List of empirical scaled sums
mean = 0.5 # Mean of Bernoulli random variable
stddev = 0.5 # Standard deviation of Bernoulli random variable

for iteration in range(0, runs):
    sequence = []
    summation = 0.0
    for index in range(0, sample):
        trial = (random.getrandbits(1) - mean) / stddev
        sequence.append(trial)
        summation += trial
    average.append(summation / sample) # LLN
    scaledsums.append(summation / math.sqrt(sample)) # CLT

bins = np.linspace(-5 / math.sqrt(sample), 5 / math.sqrt(sample), 100)
plt.hist(average, bins, normed=1, facecolor='blue', alpha=0.5)
plt.xlabel('Quantized Value')
plt.ylabel('Probability Density Function')
plt.show() # LLN

bins = np.linspace(-5, 5, 100)
plt.hist(scaledsums, bins, normed=1, facecolor='green', alpha=0.5)
plt.xlabel('Quantized Value')
plt.ylabel('Probability Density Function')
normal = mlab.normpdf(bins, 0.0, 1)
plt.plot(bins, normal, 'k--')
plt.show() # CLT
```

### Questions – Bernoulli Random Variables
* What is the limit of the empirical average as *n* becomes large?
  - ANSWER-07:
* What is the expected value of the empirical scaled sum?
  - ANSWER-08:
* What is the standard deviation of the empirical scaled sum?
  - ANSWER-09:
* In the limit, what is the distribution of the empirical scaled sum as *n* becomes large?
  - ANSWER-10:

## Exponential Random Variables
In this section, we repeat the same procedure with exponential random variables.
Again, while computing empirical sums, every trial is first centralized by subtracting the mean and normalized by dividing by the standard deviation.


```python
runs = 1000 # Number of points in histograms
sample = 10000 # Number of random variables in each sum

average = [] # List of empirical averages
scaledsums = [] # List of empirical scaled sums
mean = 1.0 # Mean of Bernoulli random variable
stddev = 1.0 # Standard deviation of Bernoulli random variable

for iteration in range(0, runs):
    sequence = []
    summation = 0.0
    for index in range(0, sample):
        trial = (random.expovariate(mean) - mean) / stddev
        sequence.append(trial)
        summation += trial
    average.append(summation / sample) # LLN
    scaledsums.append(summation / math.sqrt(sample)) # CLT

bins = np.linspace(-5 / math.sqrt(sample), 5 / math.sqrt(sample), 100)
plt.hist(average, bins, normed=1, facecolor='blue', alpha=0.5)
plt.xlabel('Quantized Value')
plt.ylabel('Probability Density Function')
plt.show() # LLN

bins = np.linspace(-5, 5, 100)
plt.hist(scaledsums, bins, normed=1, facecolor='green', alpha=0.5)
plt.xlabel('Quantized Value')
plt.ylabel('Probability Density Function')
normal = mlab.normpdf(bins, 0.0, 1)
plt.plot(bins, normal, 'k--')
plt.show() # CLT
```

### Questions – Exponential Random Variables
* What is the limit of the empirical average as *n* becomes large?
  - ANSWER-11:
* What is the expected value of the empirical scaled sum?
  - ANSWER-12:
* What is the standard deviation of the empirical scaled sum?
  - ANSWER-13:
* In the limit, what is the distribution of the empirical scaled sum as *n* becomes large?
  - ANSWER-14:

## Cauchy Random Variables
In this last section, we explore empirical averages of standard Cauchy random variables.
Note that, due to the nature of these random variables, the average is computed differently.


```python
runs = 1000 # Number of points in histograms
sample = 1000 # Number of random variables in each sum

average = [] # List of empirical averages

for iteration in range(0, runs):
    sequence = []
    runningavg = 0.0
    for index in range(0, sample):
        trial = np.random.standard_cauchy()
        sequence.append(trial)
        runningavg += trial / sample
    average.append(runningavg) # LLN

bins = np.linspace(-5, 5, 100)
plt.hist(scaledsums, bins, normed=1, facecolor='green', alpha=0.5)
plt.xlabel('Quantized Value')
plt.ylabel('Probability Density Function')
normal = mlab.normpdf(bins, 0.0, 1)
plt.plot(bins, normal, 'k--')
plt.show() # LLN
```

### Questions – Cauchy Random Variables
* Do you think that the LLN applies to Cauchy random variables?
  - ANSWER-15:
