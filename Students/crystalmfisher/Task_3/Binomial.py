__author__ = 'Crystal'
import random
# Binomial: Biased coin flip done n times
Cardinality = 2 # Cardinality: Number of elements in a set
NumberTrials = 100 # 100 trials
p = 0.5 
n = 10

TrialSequence = []
for TrialIndex in range(0, NumberTrials): 
    count = 0
    for i in range(n): # There are n 'coin flips'
            if random.random < p:
                count += 1
    TrialSequence.append(count) # Append TrialSequence with count

EmpiricalDistribution = []
for OutcomeIndex in range(0, n+1):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution

#Binomial code
# Modify this code
# Binomial on page 50 of notes
