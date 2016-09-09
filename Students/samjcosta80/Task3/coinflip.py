import random

Cardinality = 2
NumberTrials = 100

TrialSequence = [] #contains a list
for TrialIndex in range(0, NumberTrials): #trialindes is loop indicator, goes from 0-99
    TrialSequence.append(random.randrange(Cardinality))#adds to the list

EmpiricalDistribution = []#another list
for OutcomeIndex in range(0, Cardinality):#loops through all possible outcomes
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print (EmpiricalDistribution)
