import random
import math
import numpy
import pylab
import matplotlib.pyplot as plt

__author__ = "Juan J. Lozoya"  # EDIT
__NetID__ = "jlozoya4"  # EDIT
__GitHubID__ = "jlozoya4"  # EDIT
__SelfGrade__ = "4"  # EDIT
__Answer1__ = "Gaussian"
__Answer2__ = "1 & 1"
__Answer3__ = "Gaussian"
__Answer4__ = "1 & 1"
__Challenge__ = "4"

TrialNumber = 10000
Uvariable = []
for trial in range(0, TrialNumber):
	Uvariable.append(random.random())

numBins = 100 #number of evenly sized bins for histogram
plt.hist(Uvariable, numBins, normed=1, facecolor='blue', alpha=0.75)
plt.show

#Make sure to define the function 'g'
def g(x):
	return -1.0 + math.log(1.0-x)

Vvariable = []
for trial in range(0, len(Uvariable)):
	Vvariable.append(g(Uvariable[trial]))



numBins = 100 #number of evenly sized bins for histogram
plt.hist(Vvariable, numBins, normed=1, facecolor='blue', alpha=0.75)

#Make sure to define the function 'h'
Wvariable = []
def h(x):
	return math.sqrt(-2.0*(math.log(1.0-x)))


for trial in range(0, len(Uvariable)):
	Wvariable.append(h(Uvariable[trial]))


numBins = 100 #number of evenly sized bins for histogram
plt.hist(Wvariable, numBins, normed=1, facecolor='blue', alpha=0.75)
plt.show()

Uknown1 = []
Uknown2 = []
for trial in range(0, TrialNumber):
	Uvariable1 = random.random()
	Uvariable2 = random.random()
 	Unkown1.append(math.sqrt(- 2 * math.log(Uvariable1) * math.cos(2 * math.pi * Uvariable2)))
    	Unkown2.append(math.sqrt(- 2 * math.log(Uvariable1) * math.cos(2 * math.pi * Uvariable2)))


numBins = 100 #number of evenly sized bins for histogram
plt.hist(Unkown1, numBins, normed=1, facecolor='blue', alpha=0.75)
plt.show()
numBins = 100 #number of evenly sized bins for histogram
plt.hist(Unkown2, numBins, normed=1, facecolor='blue', alpha=0.75)
plt.show()

'''
1. What is the type of random variable Unkown1?
2. What is its mean and variance?
3. What is the type of random variable Unkown2?
4. What is its mean and variance?
'''
