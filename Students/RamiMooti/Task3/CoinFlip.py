import random

Cardinality = 2
NumberTrials = 100

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))
#print TrialSequence
EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print "probability of [heads,tails] when a coin is flipped 100 times (no bias)"
print "p = " + str(EmpiricalDistribution)

