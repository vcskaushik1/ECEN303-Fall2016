import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

__author__ = "Rebecca Sontheimer"  # EDIT
__NetID__ = "sont89"  # EDIT
__GitHubID__ = "sont89"  # EDIT
__SelfGrade__ = ""  # EDIT
__Challenge__ = "5"

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5
"""

'''
PART 1
'''

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

'''
PART 2
'''

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


'''
PART 3
'''

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

'''
PART 4
'''

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


'''
Answers:

1.

2.

3.

4.

5.

6.

7.

8.

9.

10.

11.

12.

13.

14.

15.



'''
