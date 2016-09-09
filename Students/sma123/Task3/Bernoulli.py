#Simmi Mani
#ECEN 303 502
#Name: Bernoulli.py

# p: chance getting head; 1-p: chance getting tails
import random

p = .5 #50% chance of getting heads

Cardinality = 2
NumberTrials = 100

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    if random.random() < p:
        TrialSequence.append(1)  #1 means heads
    else:
        TrialSequence.append(0)  #0 means tails

BernoulliRandomVariable = []
for OutcomeIndex in range(0, Cardinality):
    BernoulliRandomVariable.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print BernoulliRandomVariable

