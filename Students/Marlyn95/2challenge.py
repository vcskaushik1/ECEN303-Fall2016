__author__ = "Marlyn Rosales"
__NetID__ = "marlyn95"
__GitHubID__ = "marlyn95"
__SelfGrade__ = "5/5"
__Challenge__ = "2"

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
#import matplotlib.pyplot as plt


ParameterP = 1.0/3.0    # Parameter of digital coin
ParameterA = 1.0/3.0    # Parameter of digital coin A
ParameterB = 1.0/2.0    # Parameter of digital coin B
NumberTrials = 100000


def biasedcoinflip(p=0.5):
        if random.random()< p :
            return 1
        else:
            return 0
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
# EDIT

print ("The empirical probability that the  number of flips is 4 is ", Trials.count(4)/NumberTrials, ".")

EvenTrials = 0
for TrialIndex2 in range(0, NumberTrials):
    variable= geometricflip(ParameterP)
    if(variable%2==0):
        EvenTrials+=1
    Trials.append(variable)

print ("The empirical probability that the number of flips is 4 conditional on number of flips being even is ", (Trials.count(4)/EvenTrials))



print ("\nPart 2\n")

Trials2=[]
Trials3=[]
def geometricflip2(p1=.5, p2=0.5):
    cnt=0
    cnt2=0
    FinalA = 0
    FinalB = 0
    while(cnt==cnt2):
        cnt= biasedcoinflip(p1)
        cnt2=biasedcoinflip(p2)
        FinalA+=1

    if(cnt==1):
        AH=1
    else:
        AH=3
    return  FinalA, AH

for TrialIndex2 in range(0, NumberTrials):
    Final, A1= geometricflip2(ParameterA, ParameterB)
    Trials2.append(Final)
    Trials3.append(A1)


print ("The empirical probability that the number of flips is 2 is " , (Trials2.count(2)/NumberTrials), ".")
print ("The empirical probability that coin A is showing 1 when the stopping condition is met is " , Trials3.count(1)/NumberTrials)
print ("The empirical probability that coin B is showing 1 when the stopping condition is met is " , Trials3.count(3)/NumberTrials)
