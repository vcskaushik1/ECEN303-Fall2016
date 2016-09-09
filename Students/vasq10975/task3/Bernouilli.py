import random

Cardinality = 2
NumberTrials = 100
p = 0.85

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    if random.random() < p:
        TrialSequence.append(1)
    else:
        TrialSequence.append(0)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality): #loops thru all the outcomes
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials)) #count counts the numbers of 0's
print (EmpiricalDistribution)
