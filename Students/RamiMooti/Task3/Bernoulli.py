#burniolli 
import random

Cardinality = 2
NumberTrials = 100
p=.9
TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    if random.random() < p:
            TrialSequence.append(0)
    else: TrialSequence.append(1)
    #TrialSequence.append(random.random(Cardinality))
#print TrialSequence
EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print "90% bias towards first variable [1, 2]"
print "p = " + str(EmpiricalDistribution)
