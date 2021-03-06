__author__ = "Jovian Wysocki"
__NetID__ = "Joviancw"
__GitHubID__ = "jovianwysocki"
__SelfGrade__ = "5"
__Challenge__ = "1"
__Answer1__ = "1.0"
__Answer2__ = "6"

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
import matplotlib.pyplot as plt


ParameterP = 0.7
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p):
    # EDIT
    # Create method for biased coin flip
    # Return 1 for heads, with probability p
    # and 0 for tails

    number = random.randrange(0,99)
    if (number < p*100):
        return 1
    else:
        return 0



for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print ('The average number of ones is {0:.4f}.'.format(TrialAverage))

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    # EDIT
    # Add NumberFlips (8) coin flips for each SumTrials outcome
    #
    Total=0
    for Trialsub in range(0, NumberFlips):
        Total = Total + biasedcoinflip(ParameterP)
    SumTrials.append(Total)


Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print (repr(Distribution))
# EDIT
# Print the sum of the elements in Distribution
#
print(sum(Distribution))

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
