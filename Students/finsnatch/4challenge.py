import random
import math
import numpy 
import pylab
import matplotlib.pyplot as plt
#import statistics

__author__ = "Alan Ngo"  # EDIT
__NetID__ = "alntamu7"  # EDIT
__GitHubID__ = "finsnatch"  # EDIT
__SelfGrade__ = "5"  # EDIT
__Answer1__ = "It is a gaussian random variable, made with cos"
__Answer2__ = "Mean is 0, variance is 1"
__Answer3__ = "It is a gaussian random variable, made with sin"
__Answer4__ = "Mean is 0, variance is 1"
__Challenge__ = "4"

TrialNumber = 10000
Uvariable = []
for trial in range(0, TrialNumber):
        Uvariable.append(random.random())

plt.figure(1)
numBins = 100 #number of evenly sized bins for histogram
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.title("Uvariable")
#plt.show()


#Make sure to define the function 'g'
def g(x):
    return -1.0 * math.log(1.0 - x)
Vvariable = []
for trial in range(0, len(Uvariable)):
	Vvariable.append(g(Uvariable[trial]))

plt.figure(2)
numBins = 100 #number of evenly sized bins for histogram
plt.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.title("Vvariable")
#plt.show()

#Make sure to define the function 'h'
def h(x):
    return math.sqrt(-2.0 * math.log(1.0 - x))
Wvariable = []
for trial in range(0, len(Uvariable)):
	Wvariable.append(h(Uvariable[trial]))

plt.figure(3)
numBins = 100 #number of evenly sized bins for histogram
plt.hist(Wvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.title("Wvariable")
#plt.show()

Unknown1 = []
Unknown2 = []
for trial in range(0, TrialNumber):
    Uvariable1 = random.uniform(0.000000001,0.999999999)
    #print Uvariable1
    Uvariable2 = random.uniform(0.000000001,0.999999999) 
    #print Uvariable2
    #print math.cos(2 * math.pi * Uvariable2)
    Unknown1.append(math.sqrt(- 2 * math.log(Uvariable1)) * math.cos(2 * math.pi * Uvariable2))
    Unknown2.append(math.sqrt(- 2 * math.log(Uvariable1)) * math.sin(2 * math.pi * Uvariable2))

print 'Unknown1::'
#statistics.mean(Unknown1)
#statistics.variance(Unknown1)
mean1 = 0
for x in Unknown1:
    mean1 = mean1 + x
mean1 = mean1 / len(Unknown1)
print mean1
print numpy.var(Unknown1)

print 'Unknown2::'
#statistics.mean(Unknown2)
#statistics.variance(Unknown2)
mean2 = 0
for x in Unknown2:
    mean2 = mean2 + x
mean2 = mean2 / len(Unknown2)
print mean2
print numpy.var(Unknown2)

plt.figure(4)
numBins = 100 #number of evenly sized bins for histogram
plt.hist(Unknown1, numBins, normed=1, facecolor='green', alpha=0.75)
plt.title("Unknown1")
#plt.show()
plt.figure(5)
numBins = 100 #number of evenly sized bins for histogram
plt.hist(Unknown2, numBins, normed=1, facecolor='green', alpha=0.75)
plt.title("Unknown2")
plt.show()


'''
1. What is the type of random variable Unkown1? 
2. What is its mean and variance?
3. What is the type of random variable Unkown2?
4. What is its mean and variance?
'''