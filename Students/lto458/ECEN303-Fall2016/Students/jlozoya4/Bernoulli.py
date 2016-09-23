#Juan J. Lozoya
#September 9, 2016
#ECEN 303-502
#Bernoulli.py

import random

Cardinality = 2 #either heads or tails. written in 0 and 1
NumberTrials = 100 #Number of times it's flipped.
p = 0.85 #Bias is 85%

TrialSequence = [] #Results of coin flips stored here
for TrialIndex in range(0, NumberTrials): #TrialIndex is gonna change. #Goes from 0-99
    if random.random() < p:
    		TrialSequence.append(1)
    else:
    		TrialSequence.append(0)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
    
print EmpiricalDistribution