#  biased coin flip
import random

Cardinality = 2
p = 0.85  #or anything
NumberTrials = 10000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    if random.random() < p:
        TrialSequence.append(1)
    else:
        TrialSequence.append(0)
    #  TrialSequence.append(random.randrange(Cardinality))  #random.random needed now

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
