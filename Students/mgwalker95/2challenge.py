"""
Michael Walker
Username: mgwalker95
Date: 9/30/16
ECEN 303


"""



import random
import math

Numofloops=100000

def biasedcoinflip(p=0.5):
    return math.floor(random.random() + p)

TrialSequence = []
TrialSequence1 = []

def geometricflip(p=0.5):
    numberflips =1
    coinflip = biasedcoinflip(p)
    while (coinflip == 0):
        numberflips +=1
        coinflip = biasedcoinflip(p)
    return numberflips


for OutcomeIndex in range(0, Numofloops):
    TrialSequence.append(geometricflip(p=1.0/3.0))


for OutcomeIndex in range(0, Numofloops):
    resultofflip = geometricflip(p=1.0/3.0)
    Count = resultofflip
    while Count >= 1:
        Count =Count-2

    if Count == 0:
        TrialSequence1.append(resultofflip)

    if Count < 0:
        OutcomeIndex = OutcomeIndex -1

print('the emperical probability of getting a heads on the 4th roll is ')
print((TrialSequence.count(4)/float(Numofloops)))
print('the conditional probability of getting a heads on the 4th roll of only even rolls is')
print((TrialSequence1.count(4)/float(Numofloops)))
