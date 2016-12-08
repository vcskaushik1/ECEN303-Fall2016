import random
import math
import numpy
import pylab

__author__ = "Joshua Thompson"  # EDIT
__NetID__ = "jct6395"  # EDIT
__GitHubID__ = "josht6"  # EDIT
__SelfGrade__ = "4"  # EDIT
__Answer1__ = "Gaussian"
__Answer2__ = "Mean= -0.00568420238493; Variance= 1.00040511958"
__Answer3__ = "Gaussian"
__Answer4__ = "Mean= -0.00872952381758; Variance= 1.00144505802"
__Challenge__ = "4"

TrialNumber = 10000
Uvariable = []
for trial in range(0, TrialNumber):
	Uvariable.append(random.random())

numBins = 100 #number of evenly sized bins for histogram
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)

def g(x):
    return -1.0*math.log(1.0-x)
Vvariable=[]

for trial in range(0, len(Uvariable)):
	Vvariable.append(g(Uvariable[trial]))

numBins = 100 #number of evenly sized bins for histogram

plt.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)


def h(x):
    return math.sqrt(-2.0*(math.log(1.0-x)))
Wvariable=[]
	
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

print ("Mean 1:")
print (numpy.mean(Unknown1))
print ("Variance 1: ")
print (numpy.var(Unknown1))

print ("Mean 2:")
print (numpy.mean(Unknown2))
print ("Variance 2: ")
print (numpy.var(Unknown2))
'''
1. What is the type of random variable Unkown1?
2. What is its mean and variance?
3. What is the type of random variable Unkown2?
4. What is its mean and variance?
'''
