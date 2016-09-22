Cardinality = 2
NumberTrials = 100
p=.3
TrialSequence = [] #creates an empty set
for TrialIndex in range(0, NumberTrials): #iterates through a range between 0 and the # of trials
    if random.random() < p: # if the randomly generated number is less than p, append 1, else, 0
            TrialSequence.append(1)
    else:
        TrialSequence.append(0)

EmpiricalDistribution = []  #creates an empty set
for OutcomeIndex in range(0, Cardinality): #iterates through a range between 0 and the # of outcomes
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials)) 
print ("p = " + str(EmpiricalDistribution))
