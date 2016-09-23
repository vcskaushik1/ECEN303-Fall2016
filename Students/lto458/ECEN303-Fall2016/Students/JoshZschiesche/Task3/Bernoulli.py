import random

p = float(raw_input("Please enter in the paramater (Must be between 0 and 1)\n"))
NumberTrials = 100
Cardinality = 2
num_successes = 0

ArraySuccesses = []
TrialSequence = []

for TrialIndex in range(0, NumberTrials):
    if random.random() < p:
        TrialSequence.append(1)
    else:
        TrialSequence.append(0)

for element in TrialSequence:
    if element < p:
        ArraySuccesses.append(1)
    else:
        ArraySuccesses.append(0)

for element in ArraySuccesses:
    num_successes += element

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))

print "The Emperical Distribution:"
print EmpiricalDistribution
print "\n"
print "The Number of Successes:"
print num_successes
print "\n"
