import random

p = 0.8
NumberTrials = 100

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    cnt =0
    if random.random() < p:
        cnt+= 1
    TrialSequence.append(cnt)

EmpiricalDistribution = []
for OutcomeIndex in range(0, 2):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution