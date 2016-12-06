import random
import math
import numpy
# import pylab #  pylab not needed, commented out
import matplotlib.pyplot

__author__ = "Gregory A Jordan"
__NetID__ = "gjordan"
__GitHubID__ = "slab-bulkhead"
__SelfGrade__ = "5"
__Answer1__ = "Gaussian distribution"
__Answer2__ = "mean ~0, variance ~1"
__Answer3__ = "Gaussian distribution"
__Answer4__ = "mean ~0, variance ~1"
__Challenge__ = "4"

TrialNumber = 10000

# Uniform distribution
Uvariable = []
for trial in range(0, TrialNumber):
	Uvariable.append(random.random())

numBins = 100  #number of evenly sized bins for histogram
# numBins 100 from recitation advice
matplotlib.pyplot.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)
matplotlib.pyplot.show()

# Exponential distribution
Vvariable = []
def g(x):  #Make sure to define the function 'g'
    return -1.0*math.log(1.0 - x)
for trial in range(0, len(Uvariable)):
	Vvariable.append(g(Uvariable[trial]))

numBins = 100  #number of evenly sized bins for histogram
# numBins 100 from recitation advice
matplotlib.pyplot.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)
matplotlib.pyplot.show()

# Rayleigh distribution
def h(x):  #Make sure to define the function 'h'
    return math.sqrt(-2.0*math.log(1.0 - x))
for trial in range(0, len(Uvariable)):
	Vvariable.append(h(Uvariable[trial]))


numBins = 100  #number of evenly sized bins for histogram
# numBins 100 from recitation advice
matplotlib.pyplot.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)
matplotlib.pyplot.show()

# Gaussian distributions
# corrected numerous typos
Unknown1 = []
Unknown2 = []
for trial in range(0, TrialNumber):
    Uvariable1 = random.random()
    Uvariable2 = random.random()
    Unknown1.append(math.sqrt(-2.0*math.log(Uvariable1))*math.cos(2.0*math.pi*Uvariable2))
    Unknown2.append(math.sqrt(-2.0*math.log(Uvariable1))*math.sin(2.0*math.pi*Uvariable2))


numBins = 100  # number of evenly sized bins for histogram
# numBins 100 from recitation advice
matplotlib.pyplot.hist(Unknown1, numBins, normed=1, facecolor='green', alpha=0.75)
matplotlib.pyplot.show()
numBins = 100  # number of evenly sized bins for histogram
# numBins 100 from recitation advice
matplotlib.pyplot.hist(Unknown2, numBins, normed=1, facecolor='green', alpha=0.75)
matplotlib.pyplot.show()

print numpy.mean(Unknown1)
print numpy.var(Unknown1)
print numpy.mean(Unknown2)
print numpy.var(Unknown2)


'''
1. What is the type of random variable Unknown1?
2. What is its mean and variance?
3. What is the type of random variable Unknown2?
4. What is its mean and variance?
'''
