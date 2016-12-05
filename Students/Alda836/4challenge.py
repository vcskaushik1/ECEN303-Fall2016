import random
import math
import numpy
import pylab
import matplotlib.pyplot as plt  # i had problems with ploting the graphs before i used this library

# __author__ = "Malik Aldabbagh"
# __NetID__ = "323008160"
# __GitHubID__ = "Alda836"
# __SelfGrade__ = "5 out of 5"
# __Answer1__ = "gaussaian"
# __Answer2__ = " 1, 1"
# __Answer3__ = "gaussian"
# __Answer4__ = "1, 1"
# __Challenge__ = "4"




TrialNumber = 10000

Uvariable = []

for trial in range(0, TrialNumber):
    Uvariable.append(random.random())

numBins = 10  # number of evenly sized bins for histogram

plt.hist(Uvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()


# define the function 'g'
def g(u):
    G = -1.0 * math.log(1.0 - u)
    return G


Vvariable = []  # to stor the values from the function g(u)
for trial in range(0, len(Uvariable)):
    Vvariable.append(g(Uvariable[trial]))

numBins = 10  # number of evenly sized bins for histogram
plt.hist(Vvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()


# Make sure to define the function 'h'
def h(u):
    H = math.sqrt(-2.0 * (math.log(1.0 - u)))
    return (H)


Wvariable = []  # trore values coming from h(u)
for trial in range(0, len(Uvariable)):
    Wvariable.append(h(Uvariable[trial]))

numBins = 10  # number of evenly sized bins for histogram
plt.hist(Wvariable, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

Uknown1 = []
Uknown2 = []
for trial in range(0, TrialNumber):
    Uvariable1 = random.random()
    Uvariable2 = random.random()
    Unkown1.append(math.sqrt(- 2 * math.ln(Uvariable1) * math.cos(2 * math.PI * Uvariable2)))
    Unkown2.append(math.sqrt(- 2 * math.ln(Uvariable1) * math.cos(2 * math.PI * Uvariable2)))

numBins = 10  # number of evenly sized bins for histogram
plt.hist(Unkown1, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()

numBins = 10  # number of evenly sized bins for histogram
plt.hist(Unkown2, numBins, normed=1, facecolor='green', alpha=0.75)
plt.show()







'''
1. What is the type of random variable Unkown1?
2. What is its mean and variance?
3. What is the type of random variable Unkown2?
4. What is its mean and variance?
'''
