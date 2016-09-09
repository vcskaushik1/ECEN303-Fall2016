#!/usr/bin/python3
import random

NumberTrials = 1000
n = 10
p = 0.85

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    count = 0
    for x in range(n):
        if random.random() < p:
            count += 1
            TrialSequence.append(count)

EmpiricalDistribution = []
for OutcomeIndex in range(0, NumberTrials):
    EmpiricalDistribution.append(TrialSequence[OutcomeIndex] / float(NumberTrials))

print(EmpiricalDistribution)
