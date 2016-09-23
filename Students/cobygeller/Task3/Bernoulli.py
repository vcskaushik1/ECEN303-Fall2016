import random
Cardinality = 2
NumberTrials = 100
#probability
p = 0.7
#make empty array
TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    #random floating number from 0 to 0.999...
    if random.random() < p:
        #add value one(1) into array TrialSequence if the random value is left of the given p.
        # if p is .7 about 70% of values sould be 1
        TrialSequence.append(1)
    else:
        #add value zero(0) to the array.  % should be about 100*(1-p)
        TrialSequence.append(0)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    #counts the number of faces and tails in trail and devieds by number of trails
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
x='left is the number of face/0 and right is the number of 1/tails'
print (x,EmpiricalDistribution)


