# flipping, and counting times getting desired result, adding these results

import random

#  Cardinality = 2
NumberTrials = 10000
p = 0.3  # modify probability
n = 10

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    cnt = 0
    for i in range(n):
        if random.random() < p:
            cnt += 1
    TrialSequence.append(cnt)
    #  uncomment following line to see results of individual flips
    #  print TrialSequence

EmpiricalDistribution = []
for OutcomeIndex in range(0, n + 1):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution # generate "table" of generated numbers
