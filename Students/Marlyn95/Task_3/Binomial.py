import random

Cardinality = 2
NumberTrials = 100
p=.50
n= 10
cnt=0

TrialSequence = []
for i in range(n):
    if random.random()< p :
        cnt +=1
        TrialSequence.append(cnt)

EmpiricalDistribution = []
for OutcomeIndex in range(0, n+1):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print (EmpiricalDistribution)
