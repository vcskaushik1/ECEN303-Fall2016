__author__ = "Josh Zschiesche"
__NetID__ = "Jzschiesche1"
__GitHubID__ = "JoshZschiesche"
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


def biasedcoinflip(p=0.5):
    if random.random() <= p:
        return 1
    else:
        return 0

for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    flipsTrials = []
    summFlips = 0

    for TrialIndex3 in range(0, NumberFlips):
        flipsTrials.append(biasedcoinflip(ParameterP))
    
    summFlips = sum(flipsTrials)
    SumTrials.append(summFlips)

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

strwq = "The summation of the distributions is: "
str23 = strwq.replace("\n", "")

print str23
print sum(Distribution)
print repr(Distribution)
# Print the sum of the elements in Distribution
#

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

As you change ParameterP, your sample distribution will move to other places, for example if ParameterP is 0.7, you should see the highest normal bar centered at 0.7, however if made to something like 0.3, the highest normal is centered on 0.3

What is the sum of the elements in Distribtion?
Place your answer in the __Answer1__ variable at the top of this file.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
Place your answer in the __Answer2__ variable at the top of this file.


"""

