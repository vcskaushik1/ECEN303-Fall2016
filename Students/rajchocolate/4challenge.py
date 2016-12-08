import random
import math
import numpy
import pylab
import matplotlib.pyplot as plt

__author__ = "Rajiv Chockalingam"  # EDIT
__NetID__ = "rcwiz1296"  # EDIT
__GitHubID__ = "Rajchocolate"  # EDIT
__SelfGrade__ = "5"  # EDIT
__Answer1__ = "Gaussian Random Variable"
__Answer2__ = "Mean = 1, Variance = 1"
__Answer3__ = "Gaussian Random Variable"
__Answer4__ = "Mean = 1, Variance = 1"
__Challenge__ = "4"

TrialNumber = 10000
Uvariable = []
for trial in range(0, TrialNumber):
Uvariable.append(random.random())

numBins = 100
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

Vvariable = []
def g(x):
return -1 * math.log(1-x)

for trial in range(0, len(Uvariable)):
Vvariable.append(g(Uvariable[trial]))

numBins = 100
plt.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

Wvariable=[]
def h(x):
return math.sqrt(-2.0 *(math.log(1.0-x)))

for trial in range(0, len(Uvariable)):
Wvariable.append(h(Uvariable[trial]))

numBins = 100 
plt.hist(Wvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

Unknown1 = []
Unknown2 = []
for trial in range(0, TrialNumber):
    Uvariable1 = random.random()
    Uvariable2 = random.random()
    Unknown1.append(math.sqrt(- 2 * math.ln(Uvariable1) * math.cos(2 * math.PI * Uvariable2)))
    Unknown2.append(math.sqrt(- 2 * math.ln(Uvariable1) * math.sin(2 * math.PI * Uvariable2)))


numBins = 100
plt.hist(Unknown1, numBins, normed=1, facecolor='green', alpha=0.75)
numBins = 100
plt.hist(Unknown2, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

'''
1. What is the type of random variable Unkown1?
2. What is its mean and variance?
3. What is the type of random variable Unkown2?
4. What is its mean and variance?
'''
