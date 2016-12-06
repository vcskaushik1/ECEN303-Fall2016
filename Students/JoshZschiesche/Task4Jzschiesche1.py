import random
import math
import numpy
import pylab
import matplotlib.pyplot as plt

__author__ = "Josh Zschiesche"  # EDIT
__NetID__ = "Jzschiesche1"  # EDIT
__GitHubID__ = "JoshZschiesche"  # EDIT
__SelfGrade__ = "5"  # EDIT
__Answer1__ = "Gaussian, e.g. Standard normal"
__Answer2__ = "Mean is -0.000717703, Variance is 1.01168"
__Answer3__ = "Gaussian, e.g. Standard normal"
__Answer4__ = "Mean is -0.02396541, Variance is 1.00424"
__Challenge__ = "4"

TrialNumber = 10000
Uvariable = []
for trial in range(0, TrialNumber):
        Uvariable.append(random.random())
plt.figure(1)
numBins = 100 #number of evenly sized bins for histogram
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)


def g(x):
    return math.log(1.0-x)*(-1.0) #Make sure to define the function 'g'

Vvariable = []
for trial in range(0, len(Uvariable)):
        Vvariable.append(g(Uvariable[trial]))

plt.figure(2)
numBins = 100 #number of evenly sized bins for histogram
plt.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)

def h(x):
    return math.sqrt(math.log(1.0-x)*(-2.0)) #Make sure to define the function 'h'

Wvariable = []
for trial in range(0, len(Uvariable)):
        Wvariable.append(h(Uvariable[trial]))

plt.figure(3)
numBins = 100 #number of evenly sized bins for histogram
plt.hist(Wvariable, numBins, normed=1, facecolor='green', alpha=0.75)

Unkown1 = []
Unkown2 = []
for trial in range(0, TrialNumber):
    Uvariable1 = random.uniform(0.0000000001, 0.9999999999999)
    Uvariable2 = random.uniform(0.0000000001, 0.9999999999999)
    Unkown1.append(math.sqrt(- 2 * math.log(Uvariable1)) * math.cos(2 * math.pi * Uvariable2)) 
    Unkown2.append(math.sqrt(- 2 * math.log(Uvariable1)) * math.sin(2 * math.pi * Uvariable2))

plt.figure(4)
numBins = 100 #number of evenly sized bins for histogram
plt.hist(Unkown1, numBins, normed=1, facecolor='green', alpha=0.75)

plt.figure(5)
numBins = 100 #number of evenly sized bins for histogram
plt.hist(Unkown2, numBins, normed=1, facecolor='green', alpha=0.75)

plt.show()

print "The Mean of Unknown1 is:"
print numpy.mean(Unkown1)
print "The Variance  of Unknown1 is:"
print numpy.var(Unkown1)

print "The Mean of Unknown2 is:"
print numpy.mean(Unkown2)
print "The Vriance of Unknown2 is:"
print numpy.var(Unkown2)
'''
1. What is the type of random variable Unkown1?
2. What is its mean and variance?
3. What is the type of random variable Unkown2?
4. What is its mean and variance?
'''
