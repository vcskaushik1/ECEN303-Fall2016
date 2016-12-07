import random
import math
import numpy
import pylab
import matplotlib.pyplot as plt

__author__ = "Phillip Cryer"  
__NetID__ = "Cryerp"  
__GitHubID__ = "Cryerp"  
__SelfGrade__ = "5"  
__Answer1__ = "Gaussian"
__Answer2__ = "mean = -.00617  var = 1.00805"
__Answer3__ = "Gaussian"
__Answer4__ = " mean = -.000129  var = 1.00529"
__Challenge__ = "4"

TrialNumber = 10000
Uvariable = []
plt.figure()
for trial in range(0, TrialNumber):
	Uvariable.append(random.random())

numBins = 1000 #number of evenly sized bins for histogram
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)


def g(x):
    return math.log(1-x)*-1

Vvariable=[]
for trial in range(0, len(Uvariable)):
	Vvariable.append(g(Uvariable[trial]))
plt.figure()
numBins = 1000 #number of evenly sized bins for histogram
plt.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)

def h(x):
    return math.sqrt(math.log(1-x)*-2)
Wvariable = []
for trial in range(0, len(Uvariable)):
	Wvariable.append(h(Uvariable[trial]))

plt.figure()
numBins = 1000 #number of evenly sized bins for histogram
plt.hist(Wvariable, numBins, normed=1, facecolor='green', alpha=0.75)


Unknown1 = []
Unknown2 = []
for trial in range(0, TrialNumber):
    Uvariable1 = random.random()
    Uvariable2 = random.random()
    Unknown1.append(math.sqrt(- 2 * math.log(Uvariable1)) * math.cos(2 * math.pi * Uvariable2))
    Unknown2.append(math.sqrt(- 2 * math.log(Uvariable1)) * math.sin(2 * math.pi * Uvariable2))
plt.figure()
numBins = 1000 #number of evenly sized bins for histogram
plt.hist(Unknown1, numBins, normed=1, facecolor='green', alpha=0.75)
plt.figure()
numBins = 1000 #number of evenly sized bins for histogram
plt.hist(Unknown2, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()
print(numpy.mean(Unknown1))
print(numpy.var(Unknown1))
print(numpy.mean(Unknown2))
print(numpy.var(Unknown2))


'''
1. What is the type of random variable Unkown1?
2. What is its mean and variance?
3. What is the type of random variable Unkown2?
4. What is its mean and variance?
'''
