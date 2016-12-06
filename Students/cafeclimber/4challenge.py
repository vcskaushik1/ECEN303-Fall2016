import random
import math
import numpy as np
import pylab

import matplotlib.pyplot as plt

__author__ = "Ryan Campbell"  # EDIT
__NetID__ = "317008605"  # EDIT
__GitHubID__ = "cafeclimber"  # EDIT
__SelfGrade__ = ""  # EDIT
__Answer1__ = "Gaussian"
__Answer2__ = "~0, ~1"
__Answer3__ = "Gaussian"
__Answer4__ = "~0, ~1"
__Challenge__ = "4"

TrialNumber = 10000
Uvariable = []
for trial in range(0, TrialNumber):
	Uvariable.append(random.random())

numBins = 50
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

def g(x):
        return -1.0 * math.log(1.0 - x)

Vvariable = []
#Make sure to define the function 'g'
for trial in range(0, len(Uvariable)):
	Vvariable.append(g(Uvariable[trial]))

numBins = 50
plt.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

def h(x):
        return np.sqrt(-2 * np.log(1 - x))

Wvariable = []
#Make sure to define the function 'h'
for trial in range(0, len(Uvariable)):
	Wvariable.append(h(Uvariable[trial]))

numBins = 50
plt.hist(Wvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()


Unknown1 = []
Unknown2 = []
for trial in range(0, TrialNumber):
    Uvariable1 = random.random()
    Uvariable2 = random.random()
    Unknown1.append(math.sqrt(-2.0 * math.log(Uvariable1)) * math.cos(2.0 * math.pi * Uvariable2))
    Unknown2.append(math.sqrt(-2.0 * math.log(Uvariable1)) * math.cos(2.0 * math.pi * Uvariable2))


numBins = 100
plt.hist(Unknown1, numBins, normed=1, facecolor='green', alpha=0.75)
plt.title("Unknown1")
print("Unknown1 mean: %f" % np.mean(Unknown1))
print("Unknown1 variance: %f" % np.var(Unknown1))
plt.show()

numBins = 100
plt.hist(Unknown2, numBins, normed=1, facecolor='green', alpha=0.75)
plt.title("Unknown2")
print("Unknown2 mean: %f" % np.mean(Unknown2))
print("Unknown2 variance: %f" % np.var(Unknown2))
plt.show()



'''
1. What is the type of random variable Unkown1?
2. What is its mean and variance?
3. What is the type of random variable Unkown2?
4. What is its mean and variance?
'''
