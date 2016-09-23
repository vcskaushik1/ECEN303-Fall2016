#Simmi Mani
#ECEN 303 502
#Name: Binomial.py

import random

n = 10 #n is the number of flips within a trial
p = .4 #p is 40% chance of getting heads
NumberTrials = 10000  # number of trials

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    cnt = 0
    for i in range(n): #sees how many times the coin get heads within 1 trial (1 trial is 10 flips)
        if random.random() < p: # if random.random is less than .4, than count increases by 1
            cnt += 1
    TrialSequence.append(cnt)

BinomialRandomVariable = []
for OutcomeIndex in range(0, n+1): #range function goes from 0 to n-1, so need to include 10th flip -> n+1
    BinomialRandomVariable.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print BinomialRandomVariable

