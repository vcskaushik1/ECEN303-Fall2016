__author__ = "Marlyn Rosales"
__NetID__ = "marlyn95"
__GitHubID__ = "marlyn95"
__SelfGrade__ = ""
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


ParameterP = 0.7
NumberFlips = 8
NumberTrials = 100000
Trials = []


# I would take a look at this. You want to define the function.
# The for loop is not part of the function, but you do want the
# for loop to call the function NumberTrials times.
def biasedcoinflip(p=0.5):
    # EDIT
    # Create method for biased coin flip
    # Return 1 for heads, with probability p
    # and 0 for tails
        if random.random()< p :
            Trials.append(1)
        else:
            Trials.append(0)

for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print 'The average number of ones is {0:.4f}.'.format(TrialAverage)

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    # EDIT
    # Add NumberFlips coin flips for each SumTrials outcome
    for TrialIndex3 in range(0, NumberFlips):
    SumTrials.append(biasedcoinflip(ParameterP)) 
    # You want to append SumTrials with a number
    # between 0 and NumberFlips. i.e. if you manage to flip 8 heads
    # in a row, you want to append the number "8" to SumTrials. 
    # Similarly, if you flip 4 heads in a row, you want to append
    # the number "4." I did a second for loop.

Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

# If you're not sure about Python 2 or 3, I would wrap all prints 
# in parenthesis. e.g.
# print(repr(Distribution))
print (repr(Distribution))
# EDIT
# Print the sum of the elements in Distribution
#
DistribuitionSum= sum(Distribution)
print('The sum of the elements in Distribution is {0:.4f}.'.format(DistribuitionSum))

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
