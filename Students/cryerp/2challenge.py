
__author__ = ""
__NetID__ = ""
__GitHubID__ = ""
__SelfGrade__ = ""
__Challenge__ = "2"

__author__ = "Phillip Cryer"
__NetID__ = "Cryerp"
__GitHubID__ = "Cryerp"
__SelfGrade__ = "5"
__Challenge__ = "2"
__Answer1__ = "There is a .1001 Probabilty that it takes 4 flips to get a one"
__Answer2__ = "Given the flips are even, there is a .2492 Probability it takes 4 flips"
__Answer3__ = "With two coins the probability is .2474"
__Answer4__ = "Probability of Coin A being 1 is .3285"
__Answer5__ = "Probability of Coin B being 1 is .6715"
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
import random
import math
ParameterA = 1/3
ParameterB = 1/2
ParameterP = 1/3
Numtrials = 10000

def biased_coinflip(p=.5):
    if random.random() < p:
        return 1
    else:
        return 0


def geometricflip(p=.5):
    i = 0
    cnt = 0
    while i != 1:
        j = biased_coinflip(p)
        if j == 1:
            i = 1
            cnt += 1
        else:
            cnt += 1
    return cnt
def even_geometricflip(p=.5):
    i=0
    cnt =0
    while i != 1:
        j=biased_coinflip(p)
        if j == 1:
            cnt += 1

            if cnt %2 == 0:
                i = 1
                d = cnt
            else:
                cnt = 0
        else:
            cnt += 1
    return d


def twocoinflip(pa=.5,pb=.5):
    i =0
    cnt = 0
    while i != 1:
        ac=biased_coinflip(pa)
        bc=biased_coinflip(pb)
        cnt += 1
        if ac == 1 and bc == 0 or ac == 0 and bc == 1:
            i = 1
    return cnt

def twocoinflip_mod(pa=.5,pb=.5):
    i = 0
    cnt = 0
    while i != 1:
        ac = biased_coinflip(pa)
        bc = biased_coinflip(pb)
        if ac == 1 and bc == 0:
            cnt = 0
            i = 1
        if ac == 0 and bc == 1:
            cnt = 1
            i = 1
    return cnt

Whichcoin = []
Trials = []
EvenTrials = []
FlipTrials = []
FlipProbability = []
Distribution = []
CondDistribution = []
Whichcoinprob = []
for n in range(0,Numtrials):
    Trials.append(geometricflip(ParameterP))
    EvenTrials.append(even_geometricflip(ParameterP))
    FlipTrials.append(twocoinflip(ParameterA,ParameterB))
    Whichcoin.append(twocoinflip_mod(ParameterA,ParameterB))
for OutcomeIndex1 in range(0, max(Trials)+1):
    Distribution.append(Trials.count(OutcomeIndex1) / (1.0 * Numtrials))
for OutcomeIndex2 in range(0, max(EvenTrials)+1):
    CondDistribution.append(EvenTrials.count(OutcomeIndex2)/(1.0 * Numtrials))
for OutcomeIndex3 in range (0, max(FlipTrials)+1):
      FlipProbability.append(FlipTrials.count(OutcomeIndex3)/(1.0*Numtrials))
for OutcomeIndex4 in range (0,2):
    Whichcoinprob.append(Whichcoin.count(OutcomeIndex4)/(1.0*Numtrials))


print(repr(Distribution))
print(repr(CondDistribution))
print(repr(FlipProbability))
print(repr(Whichcoinprob))
>>>>>>> 76c3a976705c0941953b6966d819b112c27dc6cd
