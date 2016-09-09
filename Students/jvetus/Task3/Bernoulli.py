import random

Cardinality = 2
p = 0.25
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    sample = random.random()
    if sample < 1-p:
        TrialSequence.append(0)
    else:
        TrialSequence.append(1)
EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
