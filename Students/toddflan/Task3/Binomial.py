import random
import math

p = float(input('Enter a value for p: '))
n = int(input('Enter a value for n: '))

Cardinality = 10
NumberTrials = 100
suc_range = int(p * Cardinality)

Binomialpmf = [1.0] * n
Success = []
Failure = []


#print(Binomialpmf)

for num in range(0, n):

    TrialSequence = []
    for TrialIndex in range(0, NumberTrials):
        TrialSequence.append(random.randrange(Cardinality))

    tempSum = 0

    for OutcomeIndex in range(0, suc_range):
        tempSum = tempSum + TrialSequence.count(OutcomeIndex)

    Success.append(tempSum/NumberTrials)

    tempSum = 0

    for OutcomeIndex in range(suc_range, Cardinality):
        tempSum = tempSum + TrialSequence.count(OutcomeIndex)

    Failure.append(tempSum/NumberTrials)

for value in range(0, n):
    k = n - value

    Binomialpmf[value] = Binomialpmf[value] * ( math.factorial(n)/( math.factorial(k) * math.factorial(n-k) ) )

    for index in range(0, value):
        Binomialpmf[value] = Binomialpmf[value] * Success[index]
    for i in range(0, k):
        Binomialpmf[value] = Binomialpmf[value] * Failure[i]

#print(Success)
#print(Failure)

print(Binomialpmf)
