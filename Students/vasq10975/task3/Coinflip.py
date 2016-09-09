import random

Cardinality = 2 #how many numbers
NumberTrials = 100

TrialSequence = [] #list (similar to java vector)
for TrialIndex in range(0, NumberTrials): #Trial Index is loop iterator, for loop from (0-99)
    TrialSequence.append(random.randrange(Cardinality)) #each time adds an element to the list either 0 or 1

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality): #loops thru all the outcomes
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials)) #count counts the numbers of 0's
print (EmpiricalDistribution)
