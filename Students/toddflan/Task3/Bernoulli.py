import random

p = float(input('Enter a value for p (probability of success): '))

Cardinality = 2
NumberTrials = 100

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    if (random.random() < p):
        TrialSequence.append(0)
    else:
        TrialSequence.append(1)

BernoulliDist = []

for OutcomeIndex in range(0, Cardinality):
    BernoulliDist.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))

print("Format: [Success, Failure]")
print(BernoulliDist)
