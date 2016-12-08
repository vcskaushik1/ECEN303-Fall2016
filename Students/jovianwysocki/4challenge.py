import random
import math
import numpy
import pylab
import matplotlib.pyplot as plt

__author__ = "Jovian Wysocki"  # EDIT
__NetID__ = "Joviancw"  # EDIT
__GitHubID__ = "jovianwysocki"  # EDIT
__SelfGrade__ = "5"  # EDIT
__Answer1__ = "Gaussian Distribution"
__Answer2__ = "Mean 0, variance 1"
__Answer3__ = "Gaussian Distribution"
__Answer4__ = "Mean 0, variance 1"
__Challenge__ = "4"

TrialNumber = 10000
Uvariable = []
for trial in range(0, TrialNumber):
	Uvariable.append(random.random())

numBins = 100 #number of evenly sized bins for histogram
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)

def g(x): return -1 + math.log(1-x)

Vvariable= []
#Make sure to define the function 'g'
for trial in range(0, len(Uvariable)):
	Vvariable.append(g(Uvariable[trial]))

numBins = 100 #number of evenly sized bins for histogram
plt.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)


Wvariable = []
#Make sure to define the function 'h'

def h(x): return math.sqrt(-2*(math.log(1-x)))


for trial in range(0, len(Uvariable)):
	Wvariable.append(h(Uvariable[trial]))


numBins = 100 #number of evenly sized bins for histogram
plt.hist(Wvariable, numBins, normed=1, facecolor='green', alpha=0.75)


Unknown1 = []
Unknown2 = []
for trial in range(0, TrialNumber):
    Uvariable1 = random.random()
    Uvariable2 = random.random()
    Unknown1.append(math.sqrt(- 2 * math.log(Uvariable1)) * math.cos(2 * math.pi * Uvariable2))
    Unknown2.append(math.sqrt(- 2 * math.log(Uvariable1)) * math.sin(2 * math.pi * Uvariable2))

numBins = 100 #number of evenly sized bins for histogram
plt.hist(Unknown1, numBins, normed=1, facecolor='green', alpha=0.75)
numBins = 100 #number of evenly sized bins for histogram
plt.hist(Unknown2, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()


print (numpy.mean(Unknown1))
print (numpy.var(Unknown1))
print (numpy.mean(Unknown2))
print (numpy.var(Unknown2))

'''
1. What is the type of random variable Unkown1?
2. What is its mean and variance?
3. What is the type of random variable Unkown2?
4. What is its mean and variance?
'''
