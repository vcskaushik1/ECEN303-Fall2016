__author__ = "John Osborn"
__NetID__ = "josbo757"
__GitHubID__ = "josbo757"
__SelfGrade__ = ""
__Challenge__ = "1"
__Answer1__ = "1"
__Answer2__ = ""

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random


ParameterP = 0.3
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p=0.5):
    # EDIT
    # Create method for biased coin flip
    # Return 1 for heads, with probability p
    # and 0 for tails

    if random.random() < p:
        return 1
    else:
        return 0




for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print( 'The average number of ones is {0:.4f}.'.format(TrialAverage))

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    count = 0
    for i in range(NumberFlips):
        if biasedcoinflip(ParameterP) == 1:
            count += 1
    SumTrials.append(count)




Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print (repr(Distribution))
print ((sum)Distribution)


OutcomeIndex2 = range(0, NumberFlips + 1)
num_bins = len(OutcomeIndex2)
bar_width = 0.8
XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex2]
opacity = 0.4


"""
Describe what happens to the figure as you vary ParameterP from zero to one.
What is the sum of the elements in Distribtion?
Place your answer in the __Answer1__ variable at the top of this file.
What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
Place your answer in the __Answer2__ variable at the top of this file.
"""

#friday 2-3pm web326a
#3-4pm chamberlain
