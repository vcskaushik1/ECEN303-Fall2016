__author__ = "Gregory A Jordan"
__NetID__ = "gjordan"
__GitHubID__ = "slab-bulkhead"
__SelfGrade__ = "5"  # out of 5
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

ParameterP = 0.7  # vary from 0 to 1 to observe shifting bias
NumberFlips = 8
NumberTrials = 100000
Trials = []


# Create method for biased coin flip
def biasedcoinflip(p=0.5):
    if random.random() < p:
        # Return 1 for heads, with probability p
        return 1
    else:
        # and 0 for tails
        return 0


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    count = 0  # initialize a counter
    # Add NumberFlips coin flips for each SumTrials outcome
    for i in range(0, NumberFlips):
        count += biasedcoinflip(ParameterP)
    SumTrials.append(count)

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
#  Print the sum of the elements in Distribution
ElementSum = 0
for i in range(0, len(Distribution)):  # len function gets length of array
    ElementSum += Distribution[i]  # increment through array and add
print "The sum of the elements in Distribution is ", ElementSum

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

The probability of getting a head on that trial shifts from trial 1 to trial 8

What is the sum of the elements in Distribtion?
Place your answer in the __Answer1__ variable at the top of this file.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
Place your answer in the __Answer2__ variable at the top of this file.


"""
