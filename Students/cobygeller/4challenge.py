import random
import math
import numpy
import pylab

__author__ = "Jacob Geller"  # EDIT
__NetID__ = "coby.geller"  # EDIT
__GitHubID__ = "cobygeller"  # EDIT
__SelfGrade__ = ""  # 
__Answer1__ = "Gaussian"
__Answer2__ = "mean is 1 and var is 1"
__Answer3__ = "Gaussian as well"
__Answer4__ = "mean is 1 and var is 1"
__Challenge__ = "4"

TrialNumber = 10000
Uvariable = []
for trial in range(0, TrialNumber):
	Uvariable.append(random.random())

numBins = 50 #number of evenly sized bins for histogram
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)


#Make sure to define the function 'g'
def g(X):
	return -1*math.log(1-x)#-log(1-X)

for trial in range(0, len(Uvariable)):
	Vvariable.append(g(Uvariable[trial]))

numBins =50 #number of evenly sized bins for histogram
plt.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)

#Make sure to define the function 'h'
for trial in range(0, len(Uvariable)):
	Wvariable.append(h(Uvariable[trial]))


numBins =50 #number of evenly sized bins for histogram
plt.hist(Wvariable, numBins, normed=1, facecolor='green', alpha=0.75)


Uknown1 = []
Uknown2 = []
for trial in range(0, TrialNumber):
    Uvariable1 = random.random()
    Uvariable2 = random.random()
    Unkown1.append(math.sqrt(- 2 * math.ln(Uvariable1) * math.cos(2 * math.PI * Uvariable2)))
    Unkown2.append(math.sqrt(- 2 * math.ln(Uvariable1) * math.cos(2 * math.PI * Uvariable2)))


numBins =50 #number of evenly sized bins for histogram
plt.hist(Unkown1, numBins, normed=1, facecolor='green', alpha=0.75)
numBins = 50#number of evenly sized bins for histogram
plt.hist(Unkown2, numBins, normed=1, facecolor='green', alpha=0.75)


'''
1. What is the type of random variable Unkown1?
2. What is its mean and variance?
3. What is the type of random variable Unkown2?
4. What is its mean and variance?
'''