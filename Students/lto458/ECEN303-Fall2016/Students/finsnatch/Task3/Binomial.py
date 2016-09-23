import random

Cardinality = 2
NumberTrials = 100
p=0.85
n=10
EmpiricalDistribution = []

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    cnt=0
    for x in range(n):
        temp = random.random()
        if temp < p:
            cnt += 1
    TrialSequence.append(cnt)

for OutcomeIndex in range(0, NumberTrials):
    EmpiricalDistribution.append(TrialSequence[OutcomeIndex] / float(NumberTrials))
print EmpiricalDistribution