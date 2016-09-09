#!/bin/python
import random

NumberTrials = 1000
n = 10
p = 0.85

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    count = 0
    if random.random() < p:
        count += 1
        TrialSequence.append(count)

"""This need s to be fixed later"""
EmpiricalDistribution = []
for OutcomeIndex in range(0, n):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))

print(EmpiricalDistribution)
