import random
import math

ParameterP = 0.3
NumberFlips = 8
NumberTrials = 100000
Trials = []


def biasedcoinflip(p):
    x=random.random()
    if x < p:
        result=1
    else:
        result=0
    return result

print (biasedcoinflip(p=0.3))


for TrialIndex1 in range(0, NumberTrials):
    Trials.append(biasedcoinflip(ParameterP))

TrialAverage = sum(Trials) / (1.0 * len(Trials))
print ('The average number of ones is {0:.4f}.'.format(TrialAverage))

SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    cnt=0
    for x in range(0,NumberFlips):
        cnt=cnt + biasedcoinflip(ParameterP)
    SumTrials.append(cnt)
