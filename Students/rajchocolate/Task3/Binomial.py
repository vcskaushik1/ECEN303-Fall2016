import random

Cardinality = 2
NumberTrials = 100
p = 0.5
n = 8
numSuccesses = int(Cardinality * p)

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))

BinomialDistribution = n
Success = []
Fail = []
for OutcomeIndex in range(0, numSuccesses):
   BinomialDistribution.append(TrialSequence.count(OutcomeIndex) / (NumberTrials))
print BinomialDistribution
