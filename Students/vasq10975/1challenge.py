__author__ = "Jacob Vasquez"
__NetID__ = "vasq10975"
__GitHubID__ = "vasq10975"
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


ParameterP = 0.1
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p=0.5): #p=0.5 is the defaut case for biasedcoinflip()
    flip = random.random() #generates a random number between 0 & 1
    if flip < p: #if random number is less than p
        return 1 #1 signifies heads
    else:
        return 0 #0 signifies tails

for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP)) #puts ParameterP into function

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print ('The average number of ones is {0:.4f}.'.format(TrialAverage))

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    Sum = 0                                 #define a variable for sum and set it equal to zero

    for sumcalc in range(0, NumberFlips):   #define a for loop that will start at zero and iterate through the number of flips
        Sum = Sum + biasedcoinflip(ParameterP)  #sum is initially zero; populate with the number of heads flipped

    SumTrials.append(Sum)


Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print (repr(Distribution))
print ('The sum of the elements in distribution is {0:.4f}.'.format(sum(Distribution))) #print the sum of elements in distribution

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

As Parameter P is increased, the most likely outcome shifts from 0-8

What is the sum of the elements in Distribtion?
Place your answer in the __Answer1__ variable at the top of this file.

What is the most likely outcome for ParameterP = 0.7 and NumberFlips = 8?
Place your answer in the __Answer2__ variable at the top of this file.


"""
