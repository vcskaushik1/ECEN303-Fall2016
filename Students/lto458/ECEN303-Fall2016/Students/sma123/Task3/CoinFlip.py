#Simmi Mani
#ECEN 303 502
#Name: CoinFlip.py

import random

Cardinality = 2
NumberTrials = 100

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials)) #count: how many elements in list = to outcome index
print EmpiricalDistribution
