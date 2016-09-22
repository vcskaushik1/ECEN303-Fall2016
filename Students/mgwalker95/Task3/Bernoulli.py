import random

NumberTrials = 10000
Probability = 0.60

TrialSequence = []
for TrialIndex in range(0,NumberTrials):
    count = 0
    if random.random() < Probability:
        count =count + 1
    TrialSequence.append(count)

EmpiricalDistribution = []
for OutcomeIndex in range(0, 2):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print (EmpiricalDistribution)

