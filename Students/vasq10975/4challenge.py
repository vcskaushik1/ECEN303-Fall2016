import random
import math
import numpy
import pylab
import matplotlib.pyplot as plt
import statistics

__author__ = "Jacob Vasquez"  # EDIT
__NetID__ = "vasq10975"  # EDIT
__GitHubID__ = "vasq10975"  # EDIT
__SelfGrade__ = "5"  # EDIT
__Answer1__ = "Rayleigh"
__Answer2__ = "Mean: .963 Var: .364"
__Answer3__ = "Rayleigh"
__Answer4__ = "Mean: .966 Var: .365 "
__Challenge__ = "4"

TrialNumber = 10000
Uvariable = []
for trial in range(0, TrialNumber):
    Uvariable.append(random.random())

numBins = 100
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()
plt.clf()


# Make sure to define the function 'g'
def g(x):
    return -1.0 * math.log(1.0 - x)

Vvariable = []
for trial in range(0, len(Uvariable)):
    Vvariable.append(g(Uvariable[trial]))

numBins = 100
plt.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()
plt.clf()


# Make sure to define the function 'h'
def h(x):
    return math.sqrt(-2.0 * (math.log(1.0 - x)))

Wvariable = []
for trial in range(0, len(Uvariable)):
    Wvariable.append(h(Uvariable[trial]))

numBins = 100
plt.hist(Wvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()
plt.clf()

Unknown1 = []
Unknown2 = []
for trial in range(0, TrialNumber):
    Uvariable1 = random.random()
    Uvariable2 = random.random()
    Unknown1.append(math.sqrt(- 2 * math.log(Uvariable1)) * math.cos(2 * math.pi * Uvariable2))
    Unknown2.append(math.sqrt(- 2 * math.log(Uvariable1)) * math.sin(2 * math.pi * Uvariable2))

numBins = 100
plt.hist(Unknown1, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()
plt.clf()
print(statistics.mean(Unknown1))
print(statistics.variance(Unknown1))
numBins = 100
plt.hist(Unknown2, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()
plt.clf()
print(statistics.mean(Unknown2))
print(statistics.variance(Unknown2))

'''
1. What is the type of random variable Unknown1? Rayleigh
2. What is its mean and variance?
3. What is the type of random variable Unknown2? Rayleigh
4. What is its mean and variance?
'''
