__author__ = "Crystal Fisher"
__NetID__ = "crystal_fisher"
__GitHubID__ = "crystalmfisher"
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
import matplotlib.pyplot as plt # makes plots


ParameterP = 0.3
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p=0.5):
    # EDIT
    # Create method for biased coin flip
    # Return 1 for heads, with probability p
    # and 0 for tails
	if biasedcoinflip == p:
		return 1
	else:
		return 0
	# Is this right? ^^^ Maybe it's not supposed to be biasedcoinflip?


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print ('The average number of ones is {0:.4f}.'.format(TrialAverage))

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    # EDIT
    # Add NumberFlips coin flips for each SumTrials outcome
    # Similar to Binomial.py (fill this out with Binomial code)
    count = 0
    for i in range(NumberFlips):
            if random.random() < ParameterP:
                count += 1
    SumTrials.append(count)

	
Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print (repr(Distribution))
# EDIT
# Print the sum of the elements in Distribution
#
sumDist = sum(Distribution)
print ('Here is your sum:.f'.format(sumDist)) # Is this right?

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
