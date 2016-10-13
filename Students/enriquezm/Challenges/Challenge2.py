
__author__ = "Melanie Enriquez"
__NetID__ = "enriquezm"
__GitHubID__ = "smilingmelanie"
__SelfGrade__ = "4"
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


print "\nPart 1\n"

Trials = []
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))
    
Answer1 = Trials.count(4)/float(len(Trials))
print("The empirical probability that the  number of flips is 4 is " + repr(Answer1) + ".")


EvenTrials = 0
for TrialIndex2 in range(0, NumberTrials):
   if Trials[TrialIndex2]%2 == 0: 
        EvenTrials += 1
        
Answer2 = Trials.count(4)/ float(EvenTrials)
print("The empirical probability that the number of flips is 4 conditional on number of flips being even is " + repr(Answer2) + ".")
    
print "\nPart 2\n"

def GeometricFlip(p = 0.5,q = 0.5):
    set = 0
    countA = 0
    countB = 0
    count = 0
while set == 0:
        SpotA = biasedcoinflip(p)
        SpotB = biasedcoinflip(q)

if SpotA == SpotB:
            count +=1
    elif (SpotA == 1 - SpotB):
            count += 1
            countA += SpotA
            countB += SpotB
            set = 1
return(count,countA,countB)
Trials2 = []
FinalA = 0
FinalB = 0
for TrialIndex3 in range(0, NumberTrials):
    Result = geometricFlip(ParameterA,ParameterB)
    Trials2.append(Result[0])
    FinalA += Result[1]
    FinalB += Result[2]

Answer3 = Trials2.count(2)/ float(NumberTrials)   #Problem 1
Answer4 = A/ float(NumberTrials)             #Problem 2
Answer5 = B/ float(NumberTrials)             #Problem 3

print ("The empirical probability that the number of flips is 2 is " + repr(Answer3) + ".")

print ("The empirical probability that coin A is showing 1 when the stopping condition is met is " + repr(Answer4)+ ".")

print ("The empirical probability that coin B is showing 1 when the stopping condition is met is " + repr(Answer5)+ ".")
