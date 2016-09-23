__author__ = "Estival Rivera"
__NetID__ = "322003761"
__GitHubID__ = "santiago2"
__SelfGrade__ = "5"
__Challenge__ = "1"
__Answer1__ = "1"
__Answer2__ = "8 and .3"

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


def biasedcoinflip(p=0.5): #biased coin flip
    Trial_sequence = []
    for Trialindex3 in range(0, NumberTrials):
        Count = 0
        if random.random() < p:
            Count += 1
            Trial_sequence.append(Count)
Empirical_Distribution = []
for OutcomeIndex3 in range(0,2):
    Empirical_Distribution.append(Trial_sequence.count(OutcomeIndex3)/ float( NumberTrials))
print Empirical_Distribution
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
	flipSum = 0
    for flipIndex in range(0,NumberFlips):
    	flipSum += biasedcoinflip(ParameterP)

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)# prints distribution
i = 0 
Count2 = 0 
for Distribution in range (i, Distribution.__sizeof__()):
    x = Distribution.__index__(i)
    count2 = Count2 + x
    i += 1 
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
Place your answer in the __Answer1__ variable at the top of this file.
What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
Place your answer in the __Answer2__ variable at the top of this file.
"""
