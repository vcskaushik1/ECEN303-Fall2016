'''
Since it's a coin flip, the cardinality is still 2
The number of trials is 100 still
A binomial experiment has the following characteristics:
The experiment involves repeated trials. Each trial has only two possible outcomes
- a success or a failure. The probability that a particular outcome will occur on any given trial is constant.
'''
import random
p=.5 #constant probability throughout
n = 10 # repeated trials
NumberTrials = 100 #total number of trials

TrialSequence = [] #empty set

for index in range(0,NumberTrials): # index iterates through the range 0 to the # of trials
    amount = 0 #initialize to 0
    for index in range(n):
        if random.random() < p:
            amount+=1 #add 1 if condition is met
        TrialSequence.append(amount) #add to the end of the set

EmpiricalDistribution = [] #empty set
for OutcomeIndex in range(0, n+1):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print ("p = " + str(EmpiricalDistribution))
