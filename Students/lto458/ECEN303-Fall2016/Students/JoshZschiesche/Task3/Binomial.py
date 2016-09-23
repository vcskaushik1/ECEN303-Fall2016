import random
import math

condition = True

while condition:
    print "Please Enter A Negative Number of Trials to exit the program\n"

    NumberTrials = int(raw_input("Please enter in the Number of Trials\n"))
    p = float(raw_input("Please enter on the probability p (must be between 0 and 1)\n"))
    n = int(raw_input("please enter in n (Must be an intiger)\n"))

    if NumberTrials < 0:
        condition = False
        break
    else:
        TrialSequence = []
        for TrialIndex in range(0, NumberTrials):
            i = 0
            for index in range(n):
                if random.random() < p:
                    i = i+1
            TrialSequence.append(i)
    EmpiricalDistribution = []
    for OutcomeIndex in range(0, n+1):
        EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
    print EmpiricalDistribution

print "Thanks for using this run again to continue the fun with statistics\n"
