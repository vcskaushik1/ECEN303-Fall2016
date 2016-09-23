import random
Cardinality = 2
NumberTrials = 1000
p=0.85
n=10
TrialSequence = []
for TrialIndex in range(0, NumberTrials):
        Cnt = 0
        for i in range (n):
				if random.random()<p:
					Cnt+=1
        if random.random() <p:
            TrialSequence.append(1)
        else:
            TrialSequence.append(0)

empiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    empiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print empiricalDistribution

print Cnt
