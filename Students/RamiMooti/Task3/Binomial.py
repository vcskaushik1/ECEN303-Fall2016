#binomial - is n coinflips with a biased coin, parameter p
import random
p=.75
n = 5
#Cardinality = 2
NumberTrials = 10000

TrialSequence = []

for i in range(0,NumberTrials):
    cnt = 0
    for i in range(n):
        if random.random() < p:
            cnt+=1
        TrialSequence.append(cnt)

EmpiricalDistribution = []
for OutcomeIndex in range(0, n+1):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print "n = 5"
print "p = .75"
print "Yield = " + str(EmpiricalDistribution)

