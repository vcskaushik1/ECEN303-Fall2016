import random

Cardinality = 2
NumberTrials = 100
n=10
p=0.3
cnt=0

TrialSequence = [] # delaring list (vector)
for TrialIndex in range(0, NumberTrials): #defining a loop
	for i in range(n)
		if random.random() < p:
			cnt=+1
			TrialSequence.append(cnt)
    

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print (EmpiricalDistribution)
