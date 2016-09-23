__author__ = "Michael Walker"
__NetID__ = "mgwalker95"
__GitHubID__ = "mgwalker95"
__SelfGrade__ = "4"
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
#not allowing me to run because i dont have matplotlib.pyplot


ParameterP = 0.3
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p=0.5):
    # EDIT
    #TrialSequence = []
    #for TrialIndex in range(0, NumberTrials):
    #    TrialSequence.append(random.randrange(Cardinality))
    coinflipoutcome=0
    if random.random() < p:
        coinflipoutcome =1
    else:
        coinflipoutcome=0


    # Create method for biased coin flip
    # Return 1 for heads, with probability p
    # and 0 for tails
    return coinflipoutcome


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print( 'The average number of ones is {0:.4f}.'.format(TrialAverage))

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    # EDIT
    count=0.0
    for trial in range(0,NumberTrials):
        count += biasedcoinflip(ParameterP)
        SumTrials.append(count)
    # Add NumberFlips coin flips for each SumTrials outcome
    #

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print(repr(Distribution))
# EDIT
print("The Sum of elements in Distribution is %f" % sum(i for i in Distribution))
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

What is the sum of the elements in Distribtion?
Place your answer in the __Answer1__ variable at the top of this file.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
Place your answer in the __Answer2__ variable at the top of this file.


"""
