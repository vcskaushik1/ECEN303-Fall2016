import random

p = input('Enter a value for p: ')
p = float(p)

#p = 0.7

Cardinality = 10
NumberTrials = 100
suc_range = int(p * Cardinality)
tempSum = 0

#print(p)
#print(Cardinality)
#print(suc_range)

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))




#print(TrialSequence)

#EmpiricalDistribution = []
#for OutcomeIndex in range(0, Cardinality):
#    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex))

BernoulliDist = []

for OutcomeIndex in range(0, suc_range):
    tempSum = tempSum + TrialSequence.count(OutcomeIndex)

BernoulliDist.append(tempSum/NumberTrials)
tempSum = 0

for OutcomeIndex in range(suc_range, Cardinality):
    tempSum = tempSum + TrialSequence.count(OutcomeIndex)

BernoulliDist.append(tempSum/NumberTrials)

#print(EmpiricalDistribution)
print(BernoulliDist)



#print(EmpiricalDistribution)
#print(BernoulliDist)
