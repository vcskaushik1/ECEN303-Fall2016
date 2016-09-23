
"__author__ = Ross Bodeker"
"__NetID__ = rossbodeker"
"__GitHubID__ = rossbodker"
"__SelfGrade__ = 4"
"__Challenge__ = 1"
"__Answer1__ = 1"
"__Answer2__ = 6"

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
import matplotlib.pyplot


ParameterP = 0.5
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p=0.5):
    coinflip = random.random()  #assigns coinflip to be a vlue between 0.0 and 1.0, randomly
    if coinflip < p:        #allows you to decide which way a coin is biased towards, p being heads and 1-p being tails
        return 1    #heads
    else:
        return 0    #tails

for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    counter = 0     #starts a counter at zero
    for i in range(0, NumberFlips):
        counter = counter + biasedcoinflip(ParameterP)
    SumTrials.append(counter)   #adding adding the coin flips to the SumTrials

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print repr(Distribution)
# EDIT
# Print the sum of the elements in Distribution
Total = 0
for SumTotal in range(0, len(Distribution)):
    Total = Total + Distribution[SumTotal]
print "The sum of the coin flips is ", Total

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
    It changes the average number of ones to near what the value of ParameterP is.
What is the sum of the elements in Distribtion?
Place your answer in the __Answer1__ variable at the top of this file.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
Place your answer in the __Answer2__ variable at the top of this file.


"""
