import random
import math
import numpy
import pylab
import matplotlib.pyplot as plt

__author__ = "Stefan J. Manoharan"  # EDIT
__NetID__ = "stefjabez"  # EDIT
__GitHubID__ = "stefjabez"  # EDIT
__SelfGrade__ = "5"  # EDIT
__Answer1__ = "Gausian"
__Answer2__ = "Mean = 0.00016100, Variance = 0.97070178"
__Answer3__ = "Gaussian"
__Answer4__ = "Mean = -0.01746622, Variance = 0.00179880"
__Challenge__ = "4"

TrialNumber = 10000
Uvariable = []
for trial in range(0, TrialNumber):
	Uvariable.append(random.random())

plt.figure(1)
numBins = 100 #number of evenly sized bins for histogram
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)


#Make sure to define the function 'g'
def g(x):
	return -1.0 * math.log(1.0 - x)
Vvariable = []
for trial in range(0, len(Uvariable)):
	Vvariable.append(g(Uvariable[trial]))

plt.figure(2)
numBins = 100 #number of evenly sized bins for histogram
plt.hist(Vvariable, numBins, normed=1, facecolor='red', alpha=0.75)

#Make sure to define the function 'h'
def h(x):
	return math.sqrt(-2.0 * math.log(1.0 - x))
Wvariable = []
for trial in range(0, len(Uvariable)):
	Wvariable.append(h(Uvariable[trial]))

plt.figure(3)
numBins = 100 #number of evenly sized bins for histogram
plt.hist(Wvariable, numBins, normed=1, facecolor='blue', alpha=0.75)


Unkown1 = []
Unkown2 = []
for trial in range(0, TrialNumber):
    Uvariable1 = random.uniform(0.000000000001,0.999999999999999)
    Uvariable2 = random.uniform(0.000000000001,0.999999999999999)
    Unkown1.append(math.sqrt(- 2 * math.log(Uvariable1)) * math.cos(2 * math.pi * Uvariable2))
    Unkown2.append(math.sqrt(- 2 * math.log(Uvariable1)) * math.sin(2 * math.pi * Uvariable2))

print numpy.mean(Unkown1)
print numpy.var(Unkown1)

print numpy.mean(Unkown2)
print numpy.var(Unkown2)

plt.figure(4)
numBins =100 #number of evenly sized bins for histogram
plt.hist(Unkown1, numBins, normed=1, facecolor='green', alpha=0.75)
plt.figure(5)
numBins =100 #number of evenly sized bins for histogram
plt.hist(Unkown2, numBins, normed=1, facecolor='green', alpha=0.75)

plt.show()
'''
1. What is the type of random variable Unkown1?
2. What is its mean and variance?
3. What is the type of random variable Unkown2?
4. What is its mean and variance?
'''
