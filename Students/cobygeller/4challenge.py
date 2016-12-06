import random
import math
import numpy
import pylab
import matplotlib.pyplot as plt

__author__ = "Jacob Geller"  # EDIT
__NetID__ = "coby.geller"  # EDIT
__GitHubID__ = "cobygeller"  # EDIT
__SelfGrade__ = ""  # 
__Answer1__ = "Gaussian, slightly shifted from the center"
__Answer2__ = "Mean is -0.00072 and the Variance is 1.012 "
__Answer3__ = "Gaussian as well"
__Answer4__ = "mean is -0.024, Variance is 1.004 "
__Challenge__ = "4"

TrialNumber = 10000
Uvariable = []
for trial in range(0, TrialNumber):
	Uvariable.append(random.random())

numBins = 100 #number of evenly sized bins for histogram
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

#Make sure to define the function 'g'
def g(X):
	return (-1.0)*math.log(1.0-x)#-log(1-X)

for trial in range(0, len(Uvariable)):
	Vvariable.append(g(Uvariable[trial]))

numBins =100 #number of evenly sized bins for histogram
plt.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

#Make sure to define the function 'h'
def h(X)
	return math.sqrt(-2.0*(math.log(1.0-X)))
for trial in range(0, len(Uvariable)):
	Wvariable.append(h(Uvariable[trial]))


numBins =100 #number of evenly sized bins for histogram
plt.hist(Wvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

Uknown1 = []
Uknown2 = []
for trial in range(0, TrialNumber):
    Uvariable1 = random.random()
    Uvariable2 = random.random()
    Unkown1.append(math.sqrt(- 2 * math.log(Uvariable1)) * math.cos(2 * math.pi * Uvariable2)) 
    Unkown2.append(math.sqrt(- 2 * math.log(Uvariable1)) * math.sin(2 * math.pi * Uvariable2))


numBins =100 #number of evenly sized bins for histogram
plt.hist(Unkown1, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

numBins = 100#number of evenly sized bins for histogram
plt.hist(Unkown2, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

print numpy.mean(Unkown1)
print numpy.var(Unkown1)

print numpy.mean(Unkown2)
print numpy.var(Unkown2)

'''
1. What is the type of random variable Unkown1?
2. What is its mean and variance?
3. What is the type of random variable Unkown2?
4. What is its mean and variance?
'''