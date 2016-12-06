import random
import math
import numpy
import pylab

__author__ = "Rebecca Sontheimer"  # EDIT
__NetID__ = "sont89"  # EDIT
__GitHubID__ = "sont89"  # EDIT
__SelfGrade__ = "4/5"  # EDIT
__Answer1__ = "Gaussian"
__Answer2__ = "1, 1"
__Answer3__ = "Gaussian"
__Answer4__ = "1, 1"
__Challenge__ = "4"

TrialNumber = 10000
Uvariable = []
for trial in range(0, TrialNumber):
	Uvariable.append(random.random())

numBins = 100
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)

def g(x):
	return -1.0*math.log(1.0-x)
	Variable = []	

#Make sure to define the function 'g'
for trial in range(0, len(Uvariable)):
	Vvariable.append(g(Uvariable[trial]))

numBins = 100
plt.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)

def h(x):
	return math.sqrt(-2.0*(math.log(1.0-x)))
		
#Make sure to define the function 'h'
for trial in range(0, len(Uvariable)):
	Wvariable.append(h(Uvariable[trial]))


numBins = 100
plt.hist(Wvariable, numBins, normed=1, facecolor='green', alpha=0.75)


Uknown1 = []
Uknown2 = []
for trial in range(0, TrialNumber):
    Uvariable1 = random.random()
    Uvariable2 = random.random()
    Unkown1.append(math.sqrt(- 2 * math.ln(Uvariable1) * math.cos(2 * math.PI * Uvariable2)))
    Unkown2.append(math.sqrt(- 2 * math.ln(Uvariable1) * math.sin(2 * math.PI * Uvariable2)))


numBins = 100
plt.hist(Unkown1, numBins, normed=1, facecolor='green', alpha=0.75)
numBins = 100
plt.hist(Unkown2, numBins, normed=1, facecolor='green', alpha=0.75)


'''
1. What is the type of random variable Unkown1? 
2. What is its mean and variance? 
3. What is the type of random variable Unkown2? 
4. What is its mean and variance?
'''
