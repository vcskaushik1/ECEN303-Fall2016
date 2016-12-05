import random
import math
import matplotlib.pyplot as plt
import numpy
import statistics
import pylab

__author__ = "John Osborn"
__NetID__ = "josbo757"
__GitHubID__ = "josbo757"
__SelfGrade__ = "5"
__Answer1__ = "Gaussian"
__Answer2__ = "1 & 1"
__Answer3__ = "Gaussian"
__Answer4__ = "1 & 1"
__Challenge__ = "4"

TrialNumber = 10000
Uvariable = []
for trial in range(0, TrialNumber):
	Uvariable.append(random.random())

numBins = 100
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show ()

#Make sure to define the function 'g'
def g(x):
    return -1*math.log(1-x)

Vvariable = []
for trial in range(0, len(Uvariable)):
	Vvariable.append(g(Uvariable[trial]))

numBins = 100
plt.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

#Make sure to define the function 'h'
def h(x):
    return math.sqrt(-2*math.log(1-x))

Wvariable = []
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
    Unknown1.append(math.sqrt(abs(- 2 * math.log(Uvariable1) * math.cos(2 * math.pi * Uvariable2))))
    Unknown2.append(math.sqrt(abs(- 2 * math.log(Uvariable1) * math.sin(2 * math.pi * Uvariable2))))


numBins = 100
plt.hist(Unknown1, numBins, normed=1, facecolor='green', alpha=0.75)
p = statistics.mean (Unknown1)
pp = statistics.variance(Unknown1)
print ("Unknown 1 Mean:", p)
print ("Unknown 1 Variance:", pp)
plt.show()

numBins = 100
plt.hist(Unknown2, numBins, normed=1, facecolor='green', alpha=0.75)
p = statistics.mean (Unknown2)
pp = statistics.variance(Unknown2)
print ("Unknown 2 Mean:", p)
print ("Unknown 2 Variance:", pp)

plt.show()


'''
1. What is the type of random variable Unknown1?
2. What is its mean and variance?
3. What is the type of random variable Unknown2?
4. What is its mean and variance?
'''
