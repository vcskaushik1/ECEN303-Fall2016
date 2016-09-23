import random
p=.5
Cardinality = 2
n = 100

TrialSequence = []
for TrialIndex in range(0, n):
    if random.random() < p:
        TrialSequence.append(1)
else:
        TrialSequence.append(0)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(n))
print (EmpiricalDistribution)
