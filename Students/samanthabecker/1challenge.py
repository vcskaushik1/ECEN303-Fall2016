"""

Random Signals and Systems

Course: ECEN 303-502

Maximum Grade: 5pt

"""
__author__ = "Samantha Becker"
__NetID__ = "224001853"
__GitHubID__ = "samanthabecker"
__SelfGrade__ = "4.5"
__Challenge__ = "1"
__Answer1__ = "As ParamterP is varied from 0 to 1, the center of the distribution shifts from 0 to 8. The sum of the elements in the distribution is always 1."
__Answer2__ = "The most likely outcome when ParamterP = 0.7 and NumberFlips = 8 is that a 1 (heads) will be flipped"

import random
import math
import matplotlib.pyplot as plt


ParameterP = 0.3
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p=0.5):

    if random.random() < p:

            return 1


    else :
            return 0


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))



TrialAverage = sum(Trials) / (1.0 * len(Trials))
print('he average number of ones is {0:.4f}.'.format(TrialAverage))



SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    cnt = 0
    for i in range(0,NumberFlips):
        cnt += biasedcoinflip(ParameterP)
    SumTrials.append(cnt)


Distribution = []
for OutcomeIndex1 in range(0, NumberFlips + 1):
    Distribution.append(SumTrials.count(OutcomeIndex1) / (1.0 * NumberTrials))

print (repr(Distribution))


counter=0   # for loop counter
Sum =0.0    # sum for the summation
for i in range (0, len(Distribution)):
    Sum += Distribution[i]

print(Sum)


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
