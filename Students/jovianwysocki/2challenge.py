__author__ = "Jovian Wysocki"
__NetID__ = "Joviancw"
__GitHubID__ = "Jovianwysocki"
__SelfGrade__ = "5"
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


print ("Part 1\n")

Trials = []
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))
#
# EDIT
#
TrialAverage4 = Trials.count(4) / (1.0 * len(Trials))

print ("The empirical probability that the  number of flips is 4 is " \
    # EDIT: + repr(Solution1)) \
    + "{0:.4f}.".format(TrialAverage4))

EvenTrials = 0
for TrialIndex2 in range(0, NumberTrials):
    if (Trials[TrialIndex2]%2 ==0): EvenTrials +=1

    #
    # EDIT
    #
TrialAverageEven = Trials.count(4) / (1.0 * EvenTrials)

print ("The empirical probability that the number of flips is 4 conditional on number of flips being even is " \
    # EDIT: + repr(Solution2)) \
    + "{0:.4f}.".format(TrialAverageEven))


print ("\nPart 2\n")

Trials2 = []
FinalA = 0
FinalB = 0
for TrialIndex2 in range(0, NumberTrials):
    TempA =0
    TempB =0
    Trials2.append(0)
    while (TempA==TempB):
        TempA= biasedcoinflip(ParameterA)
        TempB= biasedcoinflip(ParameterB)
        Trials2[TrialIndex2]+=1
    FinalA+=TempA
    FinalB+=TempB
    #
    # EDIT
    #
TrialAverage2 = Trials2.count(2) / (1.0 * len(Trials2))
print ("The empirical probability that the number of flips is 2 is " \
    # EDIT: + repr(Solution3)) \
    + "{0:.4f}.".format(TrialAverage2))
print ("The empirical probability that coin A is showing 1 when the stopping condition is met is " \
    # EDIT: + repr(Solution4)) \
    + "{0:.4f}.".format(FinalA/(len(Trials2))))
print ("The empirical probability that coin B is showing 1 when the stopping condition is met is " \
    # EDIT: + repr(Solution5)) \
    + "{0:.4f}.".format(FinalB/(len(Trials2))))
