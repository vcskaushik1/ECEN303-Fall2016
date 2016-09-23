import random
numbertrials = 1000
p = .5
n = 10
Trialsequence = []
for Trialindex in range(0,numbertrials):
    cnt = 0
    for i in range(n):
        if random.random() < p:
            cnt += 1
    Trialsequence.append(cnt)
EmpiricalDistribution = []
for OutcomeIndex in range(0, n+1):
    EmpiricalDistribution.append(Trialsequence.count(OutcomeIndex) / float(numbertrials))
print(EmpiricalDistribution)
