import random

p = float(input('Enter a value for p (probability of success): '))
n = int(input('Enter a value for n (number of trials): '))

Cardinality = 2
NumberTrials = 1000

TrialSequence = []

for TrialIndex in range(0, NumberTrials):
    cnt = 0

    for index in range(0, n):
        if (random.random() < p):
            cnt = cnt + 1

    TrialSequence.append(cnt)

BinomialDist = []

for OutcomeIndex in range(0, n+1):
    BinomialDist.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))

print("Format: [All Tails, ... , All Heads]")
print(BinomialDist)
