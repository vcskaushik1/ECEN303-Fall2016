import random
#this is the number of random samples
Cardinality = 2
NumberTrials = 100
#empty aray to be filled by loop
TrialSequence = []
#iterate from 0m to numberTrials
for TrialIndex in range(0, NumberTrials):
    #.appent adds elamnts to trialSequence (Integer from 0 to 1 bc of random.randrange(2))
    TrialSequence.append(random.randrange(Cardinality))

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    #count counts the numbers
    EmpiricalDistribution.append(TrialSequence.count(0) / float(NumberTrials))

x='left is p of 0/face, and right is 1/tail side p'
#prints the randome outcome of the trails
print (x,EmpiricalDistribution)
