import random
import math
import numpy
import pylab

__author__ = "Julio Resendez"  
__NetID__ = "resendezjulio"
__GitHubID__ = "resendezjulio"  
__SelfGrade__ = "4.0/5.0" #I believe I got most of this to compile # seperately
__Answer1__ = "Gaussian"
__Answer2__ = "Mean = 1.0, Variance =1"
__Answer3__ = "Gaussian again"
__Answer4__ = "Mean = 1.0, Variance = 1"
__Challenge__ = "4"
 
	
TrialNumber = 10000
Uvariable = []
for trial in range(0, TrialNumber):
	Uvariable.append(random.random())

numBins = 100 # size of bins 
plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)

plt.show()


def g(x):
return 1.0*math.log(1.0-x)
uvariable =[]

#Make sure to define the function 'g'
for trial in range(0, len(Uvariable)):
	Vvariable.append(g(Uvariable[trial]))
	

	

for trial in range(0, len(Uvariable)):
	Vvariable.append(g(Uvariable[trial]))

numBins = 100
plt.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)

#Make sure to define the function 'h'
for trial in range(0, len(Uvariable)):
	Wvariable.append(h(Uvariable[trial]))


numBins = #100
plt.hist(Wvariable, numBins, normed=1, facecolor='green', alpha=0.75)

plt.show()


Uknown1 = []
Uknown2 = []
for trial in range(0, TrialNumber):
    Uvariable1 = random.random()
    Uvariable2 = random.random()
    Unkown1.append(math.sqrt(- 2 * math.ln(Uvariable1) * math.cos(2 * math.PI * Uvariable2)))
    Unkown2.append(math.sqrt(- 2 * math.ln(Uvariable1) * math.cos(2 * math.PI * Uvariable2)))


numBins = 100
plt.hist(Unkown1, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()
plt.clf()
numBins = 1000
plt.hist(Unkown2, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()



