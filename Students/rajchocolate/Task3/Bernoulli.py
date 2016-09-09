import random

Cardinality = 2
NumberTrials = 100
p = 0.5
numSuccesses = int(Cardinality * p)

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))

BernoulliDistribution = []
for OutcomeIndex in range(0, numSuccesses):
    BernoulliDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print BernoulliDistribution
