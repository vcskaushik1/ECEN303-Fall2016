import random
import math
import numpy
import pylab
import matplotlib.pyplot as plt

__author__ = "Juan Gomez"
__NetID__ = "juanigomez"
__GitHubID__ = "juanigomez95"
__SelfGrade__ = "5"
__Answer1__ = "Gaussian"
__Answer2__ = "Mean 1 Variance 1"
__Answer3__ = "Gaussian"
__Answer4__ = "Mean 1 Variance 1"
__Challenge__ = "4"

TrialNumber = 10000
Uvariable = []
for trial in range(0, TrialNumber):
	Uvariable.append(random.random())

numBins = 100
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

def g(x):
        return -1.0*math.log(1.0-x)
Vvariable = []
for trial in range(0, len(Uvariable)):
	Vvariable.append(g(Uvariable[trial]))

numBins = 100
plt.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

def h(x):
    return math.sqrt(-2.0*math.log(1.0-x))
Wvariable = []
for trial in range(0, len(Uvariable)):
	Wvariable.append(h(Uvariable[trial]))


numBins = 100
plt.hist(Wvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

Uknown1 = []
Uknown2 = []
for trial in range(0, TrialNumber):
    Uvariable1 = random.random()
    Uvariable2 = random.random()
    Uknown1.append(math.sqrt(- 2 * np.log(Uvariable1) * math.cos(2 * math.pi * Uvariable2)))
    Uknown2.append(math.sqrt(- 2 * np.log(Uvariable1) * math.cos(2 * math.pi * Uvariable2)))


numBins = 100
plt.hist(Uknown1, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show
numBins = 100
plt.hist(Uknown2, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show


'''
1. What is the type of random variable Unkown1?
2. What is its mean and variance?
3. What is the type of random variable Unkown2?
4. What is its mean and variance?
'''
