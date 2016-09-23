import random

NumTrials = 100000

# Parameters
p = 0.25
n = 8

Outcomes = [0 for j in range(0,n)]

for x in range(0,  NumTrials):
	TrialSequence = [0 for j in range(n)]
	for i in range(0, n):
		for k in range(0, n):
			r = random.random()
			if r <= p:
				TrialSequence[i] = TrialSequence[i] + 1
		if TrialSequence[i] == i:
			Outcomes[i] = Outcomes[i] + 1
		
for x in range(0,n):
	Outcomes[x] = Outcomes[x]/float(NumTrials)
print Outcomes
