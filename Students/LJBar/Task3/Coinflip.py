import random

Cardinality = 2
NumberTrials = 100

TrialSequence = [] 
for TrialIndex in range(0, NumberTrials): 0 to 99
    TrialSequence.append(random.randrange(Cardinality))

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print (EmpiricalDistribution)

1st number is o 2nd number is 1