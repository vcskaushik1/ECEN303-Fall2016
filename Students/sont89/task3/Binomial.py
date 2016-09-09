import random

Cardinality = 2
NumberTrials = 10000
p = 0.50
n = 10

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
	cnt = 0
	for i in rang(n):	
		if random.random() < p:
			cnt+=1
		TrialSequence.append(1)

EmpiricalDistribution = []
for OutcomeIndex in range(0, n+1):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
