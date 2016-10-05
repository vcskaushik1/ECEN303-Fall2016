
__author__ = ""
__NetID__ = ""
__GitHubID__ = ""
__SelfGrade__ = ""
__Challenge__ = "2"

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
import matplotlib.pyplot as plt


ParameterP = 1.0/3.0    # Parameter of digital coin
ParameterA = 1.0/3.0    # Parameter of digital coin A
ParameterB = 1.0/2.0    # Parameter of digital coin B
NumberTrials = 100000


def biasedcoinflip(p=0.5):
    """
    This method returns a one with probability p and it returns a zero with
    probability (1 - p). The default parameter is p=0.5; this can be changed
    by passing an argument to the method.
    """
    return math.floor(random.random() + p)


def geometricflip(p=0.5):
    """
    This method returns a natural number that denotes the number of digital
    coin flips needed to obtain a one. It relies on method biasedcoinflip().
    """
    numberflips = 1
    while biasedcoinflip(p) != 1:
        numberflips += 1
    return numberflips


print "Part 1\n"

Trials = []
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))
#
# EDIT
#

print "The empirical probability that the  number of flips is 4 is " \
    # EDIT: + repr(Solution1)) \
    + "."

EvenTrials = 0
for TrialIndex2 in range(0, NumberTrials):
    #
    # EDIT
    #

print "The empirical probability that the number of flips is 4 conditional on number of flips being even is " \
    # EDIT: + repr(Solution2)) \
    + "."


print "\nPart 2\n"

Trials2 = []
FinalA = 0
FinalB = 0
for TrialIndex2 in range(0, NumberTrials):
    #
    # EDIT
    #

print "The empirical probability that the number of flips is 2 is " \
    # EDIT: + repr(Solution3)) \
    + "."
print "The empirical probability that coin A is showing 1 when the stopping condition is met is " \
    # EDIT: + repr(Solution4)) \
    + "."
print "The empirical probability that coin B is showing 1 when the stopping condition is met is " \
    # EDIT: + repr(Solution5)) \
    + "."

=======
"""
Michael Walker
Username: mgwalker95
Date: 9/30/16
ECEN 303
Self Grade:5/5

"""



import random
import math

Numofloops=100000

def biasedcoinflip(p=0.5):
    return math.floor(random.random() + p)

TrialSequence = []
TrialSequence1 = []

def geometricflip(p=0.5):
    numberflips =1
    coinflip = biasedcoinflip(p)
    while (coinflip == 0):
        numberflips +=1
        coinflip = biasedcoinflip(p)
    return numberflips


for OutcomeIndex in range(0, Numofloops):
    TrialSequence.append(geometricflip(p=1.0/3.0))


for OutcomeIndex in range(0, Numofloops):
    resultofflip = geometricflip(p=1.0/3.0)
    Count = resultofflip
    while Count >= 1:
        Count =Count-2

    if Count == 0:
        TrialSequence1.append(resultofflip)

    if Count < 0:
        OutcomeIndex = OutcomeIndex -1

print('the emperical probability of getting a heads on the 4th roll is ')
print((TrialSequence.count(4)/float(Numofloops)))
print('the conditional probability of getting a heads on the 4th roll of only even rolls is')
print((TrialSequence1.count(4)/float(Numofloops)))
