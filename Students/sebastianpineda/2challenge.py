__author__ = "Sergio Pineda"
__NetID__ = "123004451"
__GitHubID__ = "sebastianpineda"
__SelfGrade__ = "5"
__Challenge__ = "2"

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math


p = 1.0/3.0    			# Parameter of digital coin
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
        numberflips = numberflips + 1
    return numberflips


print "Part 1\n"

Trials = []
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(p))

emProb4 = Trials.count(4)/(1.0 * NumberTrials)
	
print "The empirical probability that the  number of flips is 4 is {0:.4f}" \
    .format(emProb4) + "."

EvenTrials = 0
for TrialIndex2 in range(0, NumberTrials):
    if  Trials[TrialIndex2] % 2 == 0:
		EvenTrials = EvenTrials + 1

emProbEven = Trials.count(4)/(1.0 * EvenTrials)

print "The empirical probability that the number of flips is 4 conditional on number of flips being even is {0:.4f}" \
    .format(emProbEven) + "."

print "\nPart 2\n"

Trials2 = []
stopOnA = 0
stopOnB = 0
for TrialIndex2 in range(0, NumberTrials):
	FinalA = 0
	FinalB = 0
	numberflips = 0
	
	while(FinalA == FinalB):
		FinalA = biasedcoinflip(ParameterA)
		FinalB = biasedcoinflip(ParameterB)
		numberflips = numberflips + 1
	
	Trials2.append(numberflips)
	
	if(FinalA == 1):
		stopOnA = stopOnA + 1
	else:
		stopOnB = stopOnB + 1
		
emProb2 = Trials2.count(2)/(1.0 * NumberTrials)
emProbA = stopOnA/(1.0 * NumberTrials)
emProbB = stopOnB/(1.0 * NumberTrials)

print "The empirical probability that the number of flips is 2 is {0:.4f}" \
	.format(emProb2) + "."
	
print "The empirical probability that coin A is showing 1 when the stopping condition is met is {0:.4f}" \
	.format(emProbA) + "."

print "The empirical probability that coin B is showing 1 when the stopping condition is met is {0:.4f}" \
	.format(emProbB) + "."