import random

Cardinality = 2
NumberTrials = 100
kount = 0
p = .25

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))
if TrialSequence.count(1)/float(NumberTrials) < p:
    while (TrialSequence.count(1)/float(NumberTrials)) < p:
        TrialSequence[kount] = 1
        kount += 1
else:
    while (TrialSequence.count(1)/float(NumberTrials)) > p:
        TrialSequence[kount] = 0
        kount += 1

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print(EmpiricalDistribution)

