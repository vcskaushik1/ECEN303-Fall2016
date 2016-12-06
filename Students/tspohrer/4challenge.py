import random
import math
import matplotlib.pyplot as plt
import numpy
import statistics
import pylab

__author__ = "Trevor Spohrer"
__NetID__ = "tspohrer"
__GitHubID__ = "tspohrer"
__SelfGrade__ = "5/5"
__Answer1__ = "Gaussian"
__Answer2__ = "Mean=1 & Variance=0.365"
__Answer3__ = "Gaussian"
__Answer4__ = "Mean=1 & Variance=0.35"
__Challenge__ = "4"

TrialNumber = 10000
Uvariable = []
for trial in range(0, TrialNumber):
	Uvariable.append(random.random())

numBins = 100
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

def g(x):
    return -1*math.log(-x+1)

Vvariable = []
for trial in range(0, len(Uvariable)):
	Vvariable.append(g(Uvariable[trial]))

numBins =100
plt.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show ()

def h(x):
    return math.sqrt(-2*math.log(-x+1))

Wvariable = []
for trial in range(0, len(Uvariable)):
	Wvariable.append(h(Uvariable[trial]))


numBins = 100
plt.hist(Wvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show ()

"I believe these should be unknown not uknown"
Unknown1 = []
Unknown2 = []
for trial in range(0, TrialNumber):
    Uvariable1 = random.random()
    Uvariable2 = random.random()
    Unknown1.append(math.sqrt(- 2 * math.ln(Uvariable1) * math.cos(2 * math.PI * Uvariable2)))

    "I think this one was supposed to be sin also Unknown not Unkown"
    Unknown2.append(math.sqrt(- 2 * math.ln(Uvariable1) * math.sin(2 * math.PI * Uvariable2)))


numBins = 100
plt.hist(Unkown1, numBins, normed=1, facecolor='green', alpha=0.75)
p=statistics.mean (Unknown1)
pp= statistics.variance(Unknown1)
print ("Unknown 1 Mean:", P)
print ("Unknown 1 Variance:", pp)
plt.show()

numBins = 100
plt.hist(Unkown2, numBins, normed=1, facecolor='green', alpha=0.75)
p=statistics.mean (Unknown2)
pp= statistics.variance(Unknown2)
print ("Unknown 2 Mean:", P)
print ("Unknown 2 Variance:", pp)
plt.show()

