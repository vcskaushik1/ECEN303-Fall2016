__author__ = "Alan Ngo"
__NetID__ = "alntamu7"
__GitHubID__ = "finsnatch"
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


print "Part 1\n"

Trials = []
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))
#
# EDIT
#
#print(Trials)
Solution1 = Trials.count(4)/float(len(Trials))
print "The empirical probability that the  number of flips is 4 is " + repr(Solution1) + "."

EvenTrials = 0
evenT = []
for TrialIndex2 in range(0, NumberTrials):
    #
    # EDIT
    #
    temp = geometricflip(ParameterP)
    if temp % 2 == 0:
        EvenTrials+=1
        evenT.append(temp)
    
Solution2 = evenT.count(4)/float(EvenTrials)

print "The empirical probability that the number of flips is 4 conditional on number of flips being even is " + repr(Solution2) + "."


print "\nPart 2\n"

Trials2 = []
FinalA = 0
FinalB = 0
for TrialIndex2 in range(0, NumberTrials):
    #
    # EDIT
    #
    tempA = biasedcoinflip(ParameterA)
    tempB = biasedcoinflip(ParameterB)
    cnt = 1
    while tempA == 0 and tempB == 0 or tempA ==1  and tempB == 1:
        cnt+=1
        tempA = biasedcoinflip(ParameterA)
        tempB = biasedcoinflip(ParameterB)
        if tempA == 1 and tempB == 0:
            FinalA+=1
        elif tempA == 0 and tempB ==1:
            FinalB+=1
    Trials2.append(cnt)

#print(Trials2)
Solution3 = Trials2.count(2)/float(len(Trials2))
Solution4 = FinalA/float(len(Trials2))
Solution5 = FinalB/float(len(Trials2))

print "The empirical probability that the number of flips is 2 is " + repr(Solution3) + "."
print "The empirical probability that coin A is showing 1 when the stopping condition is met is " + repr(Solution4) + "."
print "The empirical probability that coin B is showing 1 when the stopping condition is met is " + repr(Solution5) + "."

