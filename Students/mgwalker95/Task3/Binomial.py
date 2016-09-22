import random

NumberTrials = 10000
Probability = 0.450
n=9

TrialSequence = []
for TrialIndex in range(0,NumberTrials):
    count = 0
    for i in range(n):
        if random.random() < Probability:
            count =count + 1
    TrialSequence.append(count)

EmpiricalDistribution = []
for OutcomeIndex in range(0, n+1):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print (EmpiricalDistribution)


