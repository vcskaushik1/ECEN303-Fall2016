__author__ = 'Crystal'
import random
# Bernoulli: Like a biased coin flip
Cardinality = 2 # Cardinality: Number of elements in a set
NumberTrials = 100 # 100 trials
p = 0.85 

TrialSequence = [] # Initialization of blank list TrialSequence
for TrialIndex in range(0, NumberTrials): # For loop for 100 trials
    TrialSequence.append(random.randrange(Cardinality))
if random.random() < p: # So if random < 0.25...
    TrialSequence.append(1) # We make it 1
else
    TrialSequence.append(0) # otherwise, it's 0

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution

#Bernoulli random variables with parameter p
# Modify this code
# Bernoulli on page 49 of notes
