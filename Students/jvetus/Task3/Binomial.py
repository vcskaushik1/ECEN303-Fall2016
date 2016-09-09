import random

n = 6
p = 0.3
NumberTrials = 300000

nSequence = []

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    for k in range(0, n):
        sample = random.random()
        if sample < 1-p:
            nSequence.append(0)
        else:
            nSequence.append(1)
    TrialSequence.append(nSequence.count(1))
    del nSequence[:]

EmpiricalDistribution = []
for OutcomeIndex in range(0, n+1):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
