import random

NumberTrials = 1000
p=0.5
n=9

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    cnt=0
    for i in range(n):
        if random.random()< p:
            cnt+=1
    TrialSequence.append(cnt)

EmpiricalDistribution = []
for OutcomeIndex in range(0, n+1):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print (EmpiricalDistribution)
