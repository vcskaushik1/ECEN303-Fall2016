__author__ = "Dillon Johnson"
__NetID__ = "dillonjohnson48"
__GitHubID__ = "dillonjohnson48"
__SelfGrade__ = ""
__Challenge__ = "1"
__Answer1__ = ""
__Answer2__ = ""

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
import matplotlib.pyplot as plt


ParameterP = 0.3
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p=0.5):
    Num = random.random()
    if (Num < p):   #p bias
        return 1    #1 is heads
    else:
        return 0    #0 is tails


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    Sum = 0                                     #reset value to 0

    for Sample in range(0, NumberFlips):        #0 to NumberFlips value in header
        Sum = Sum + biasedcoinflip(ParameterP)  #Sum is the accumulative sum of past value and current biased flip

    SumTrials.append(Sum)                       #adds sum to the end of the list


Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print (repr(Distribution))

SumDistribution = 0
for i in Distribution:
    SumDistribution = SumDistribution + i
print('Sum of Distribution elements is {0:.2f}.'.format(SumDistribution))


OutcomeIndex2 = range(0, NumberFlips + 1)
num_bins = len(OutcomeIndex2)
bar_width = 0.8
XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex2]
opacity = 0.4

plt.bar(OutcomeIndex2, Distribution, bar_width, alpha=opacity, color='b')
plt.xlabel("Value")
plt.ylabel("Probability")
plt.xticks(XticksIndex, OutcomeIndex2)
plt.show()

"""
Describe what happens to the figure as you vary ParameterP from zero to one.
<<<<<<< HEAD
What is the sum of the elements in Distribtion?
Place your answer in the __Answer1__ variable at the top of this file.
What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
Place your answer in the __Answer2__ variable at the top of this file.
=======

What is the sum of the elements in Distribtion?
Place your answer in the __Answer1__ variable at the top of this file.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
Place your answer in the __Answer2__ variable at the top of this file.


>>>>>>> c4f74ea0b0cbf4103691c0f735b9b090503cd740
"""
