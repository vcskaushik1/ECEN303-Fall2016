import random

NumberTrials = 100
p = .23
n=15

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    count = 0
	for 1 in range(n):
		if random.random()<p:
			count+=1
	TrialSequence.append(count)
		

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution