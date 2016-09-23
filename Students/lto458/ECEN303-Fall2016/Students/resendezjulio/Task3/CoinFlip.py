'''
A regular coin flip has a cardinality of 2, 2 outcomes(heads,tails)
Number of trials will be 100
'''
import random #import random library to use functions

Cardinality = 2
NumberTrials = 100

TrialSequence = [] #creates an empty set
for TrialIndex in range(0, NumberTrials): #the for loop iterates through a range of 0 to the specified number of trials(100)
    TrialSequence.append(random.randrange(Cardinality)) #append adds to the set randrange 0 to 2

EmpiricalDistribution = [] #creates an empty set
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print ("p = " + str(EmpiricalDistribution)) # converts float point to a str so that it may be displayed along with a string
