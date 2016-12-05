import random
import cmath
import math
import numpy
import pylab
import matplotlib.pyplot as plt

__author__ = "Sergio Pineda"
__NetID__ = "123004451"
__GitHubID__ = "sebastianpineda"
__SelfGrade__ = "4.5?"  # Parts of this template shouldn't normally compile, and some parts output complex values that can't be plotted.
__Answer1__ = "Gaussian"
__Answer2__ = "1 and 1"
__Answer3__ = "Gaussian"
__Answer4__ = "1 and 1"
__Challenge__ = "4"

TrialNumber = 10000
Uvariable = []
for trial in range(0, TrialNumber):
	Uvariable.append(random.random())

numBins = 100 #number of evenly sized bins for histogram
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

def g(x):
	return -1.0*math.log(1.0-x)

Vvariable = []
#Make sure to define the function 'g'
for trial in range(0, len(Uvariable)):
	Vvariable.append(g(Uvariable[trial]))

numBins = 100 #number of evenly sized bins for histogram
plt.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

Wvariable = []
def h(x):
	return math.sqrt(-2.0*(math.log(1.0-x)))
#Make sure to define the function 'h'
for trial in range(0, len(Uvariable)):
	Wvariable.append(h(Uvariable[trial]))


numBins = 100 #number of evenly sized bins for histogram
plt.hist(Wvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

Unknown1 = []
Unknown2 = []
for trial in range(0, TrialNumber):
    Uvariable1 = random.random()
    Uvariable2 = random.random()
    Unknown1.append(math.sqrt(abs(- 2 * math.log(Uvariable1) * math.cos(2 * math.pi * Uvariable2))))
    Unknown2.append(math.sqrt(abs(- 2 * math.log(Uvariable1) * math.cos(2 * math.pi * Uvariable2))))


numBins = 100 #number of evenly sized bins for histogram
plt.hist(Unknown1, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()
numBins = 100 #number of evenly sized bins for histogram
plt.hist(Unknown2, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()


'''
1. What is the type of random variable Unknown1? Gaussian
2. What is its mean and variance? 1 and 1
3. What is the type of random variable Unknown2? Gaussian. Both functions are identical?
4. What is its mean and variance? 1 and 1
'''
