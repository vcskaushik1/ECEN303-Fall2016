import random
import math
import numpy
import matplotlib.pyplot as plt

__author__ = "Dillon Johnson"  # EDIT
__NetID__ = "324007726"  # EDIT
__GitHubID__ = "dillonjohnson48"  # EDIT
__SelfGrade__ = "5"  # 
__Answer1__ = "Gaussian"
__Answer2__ = "1 for both"
__Answer3__ = "Gaussian"
__Answer4__ = "1 for both"
__Challenge__ = "4"

TrialNumber = 10000
Uvariable = []
for trial in range(0, TrialNumber):
	Uvariable.append(random.random())

numBins = 100 #number of evenly sized bins for histogram
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

#Make sure to define the function 'g'
def g(x):
        return -1.0*math.log(1.0-x)
Vvariable = []

for trial in range(0, len(Uvariable)):
	Vvariable.append(g(Uvariable[trial]))

numBins = 100 #number of evenly sized bins for histogram
plt.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()
Wvariable = []

#Make sure to define the function 'h'
def h(x):
        return math.sqrt( -2.0*(math.log(1.0-x)) )


for trial in range(0, len(Uvariable)):
	Wvariable.append(h(Uvariable[trial]))


numBins = 100 #number of evenly sized bins for histogram
plt.hist(Wvariable, numBins, normed=1, facecolor='green', alpha=0.75)


Unknown1 = []
Unknown2 = []
for trial in range(0, TrialNumber):
    Uvariable1 = random.random()
    Uvariable2 = random.random()
    Unknown1.append(math.sqrt(- 2.0 * math.ln(Uvariable1) * math.cos(2.0 * math.PI * Uvariable2)))
    Unknown2.append(math.sqrt(- 2.0 * math.ln(Uvariable1) * math.sin(2.0 * math.PI * Uvariable2)))


numBins = 100 #number of evenly sized bins for histogram
plt.hist(Unknown1, numBins, normed=1, facecolor='green', alpha=0.75)
numBins = 100 #number of evenly sized bins for histogram
plt.hist(Unknown2, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

'''
1. What is the type of random variable Unknown1?
2. What is its mean and variance?
3. What is the type of random variable Unknown2?
4. What is its mean and variance?
'''
