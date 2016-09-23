#Juan J. Lozoya
#September 9, 2016
#ECEN 303-502
#Binomial.py

import random

Cardinality = 2 #either heads or tails. written in 0 and 1
NumberTrials = 100 #Number of times it's flipped.
p = 0.50 #Bias. 50%
n = 10 

TrialSequence = [] #Results of coin flips stored here
for TrialIndex in range(0, NumberTrials): #TrialIndex is gonna change. #Goes from 0-99
    count = 0
    for i in range(n):
    	if random.random() < p: #if random number is less than p add a number into count
    		count+=1
    	TrialSequence.append(count)


EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
    
print EmpiricalDistribution