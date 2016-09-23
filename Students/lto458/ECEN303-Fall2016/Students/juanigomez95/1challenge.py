__author__ = "Juan Gomez"
__NetID__ = "juanigomez"
__GitHubID__ = "juanigomez95"
__SelfGrade__ = "5"
__Challenge__ = "1"
__Answer1__ = "1.0"
__Answer2__ = "6"

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import math
import random
import matplotlib.pyplot as plt



ParameterP = 0.3
NumberFlips = 8
NumberTrials = 100000
Trials = []

def biasedcoinflip(p):
    x = random.random()
    "p is the probability of getting heads so if p"
    "x is a random number between 0 and 1"
    "if x is smaller than p, it will be heads and vice versa"
    if x < p:
        outcome=1
    else:
        outcome=0
    return outcome

for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    i = 0
    for x in range(0,NumberFlips):
        i = i + biasedcoinflip(ParameterP)
    SumTrials.append(i)

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)

Sum= 0
for y in range(0,NumberFlips):
    Sum = Sum + Distribution[y]
    print Sum

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
What is the sum of the elements in Distribtion?

The the distribution will shift from left to right as heads become more prominent.
The sum of the distriution will eventually reach the number of coin flips.

Place your answer in the __Answer1__ variable at the top of this file.
What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
Place your answer in the __Answer2__ variable at the top of this file.
"""
