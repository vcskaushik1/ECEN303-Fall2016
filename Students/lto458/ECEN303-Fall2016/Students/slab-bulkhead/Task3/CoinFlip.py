import random

Cardinality = 2
NumberTrials = 10000  # larger trial count means closer to 50/50

TrialSequence = []  # list of trials, similar to vector, no need for datatype
for TrialIndex in range(0, NumberTrials):  # loop begins, TrialIndex is iterator "i"
    TrialSequence.append(random.randrange(Cardinality))

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
    # trialsequence0, trialsequence1, trialsequence2...
print EmpiricalDistribution
