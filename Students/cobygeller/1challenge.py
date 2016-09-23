__author__ = "Jacob Geller"
__NetID__ = "coby.geller"
__GitHubID__ = "cobygeller"
__SelfGrade__ = ""
__Challenge__ = "1"
__Answer1__ = "5.6"
__Answer2__ = ".7"

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""


import random
import math
#import matplotlib.pyplot as plt

ParameterP = 0.7
NumberFlips = 8
NumberTrials = 100000


# makes a function biasedcoinflip that flips a coin with a weighted biased based on the ParameterP
def biasedcoinflip(p=0.5):
    if random.random()<p:
        return 1
    else:
        return 0

Trials = []
#makes an array with 1 as heads and 0 as tails with length Numbertriles
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))
#makes and avrage of all trials ( 1s and 0s added, devided by the length of array Trials)
TrialAverage = sum(Trials) / (1.0 * len(Trials))
print ('The average number of ones is {0:.4f}.'.format(TrialAverage))

SumTrials = []
#run NumberFlips in each NUmberTrials and write these into array SumTrials(nested for loop)
for TrialIndex2 in range(0, NumberTrials):
    Numberinrange=0
    for TrialIndex3 in range (0,NumberFlips):
         if biasedcoinflip(ParameterP):
            Numberinrange=1+Numberinrange
            SumTrials.append(Numberinrange)
Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))


x=sum(Distribution)
print('Sum of values contained in list Distribution',x)

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
""""
Describe what happens to the figure as you vary ParameterP from zero to one.

What is the sum of the elements in Distribtion?
Place your answer in the __Answer1__ variable at the top of this file.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
Place your answer in the __Answer2__ variable at the top of this file.


"""
