__author__ = "Samuel Todd Flanagan"
__NetID__ = "toddflanagan95"
__GitHubID__ = "toddflan"
__SelfGrade__ = "5"
__Challenge__ = "1"
__Answer1__ = "1"
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

# EDIT****************************************************
def biasedcoinflip(p=0.5):
    RandNum = random.random()       # generate random number [0.0, 1.0)

    if (RandNum < p):               # makes the "coin" biased
        return 1                    # heads
    else:
        return 0                    # tails
# ********************************************************

for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print('The average number of ones is {0:.4f}.'.format(TrialAverage))

SumTrials = []

# EDIT********************************************************
for TrialIndex2 in range(0, NumberTrials):
    SumNumFlips = 0

    for Flip in range(0, NumberFlips):
        SumNumFlips = SumNumFlips + biasedcoinflip(ParameterP)
                                    # add NumberFlips coin flips for each SumTrials outcome
    SumTrials.append(SumNumFlips)
# ************************************************************

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print(repr(Distribution))

# EDIT*************************************************************************
SumDist = 0                             # set sum of distribution to 0

for DistElements in Distribution:       # loop through each element of Distribution
    SumDist = SumDist + DistElements    # add each element

print('Sum of the elements in Distribution = {0:.2f}.'.format(SumDist))      # prints the sum of Distribution
# *****************************************************************************


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
    - The maximum of the figure shifts from left to right.*************************************

What is the sum of the elements in Distribtion?
Place your answer in the __Answer1__ variable at the top of this file.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
Place your answer in the __Answer2__ variable at the top of this file.


"""
