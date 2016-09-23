import random
#the number of trails to run
NumberTrials=1000
#prob(weighted coin with prob to one side)
p=0.7
#"weighted coin flips" in each trail
n=10
#empty array for trails
Trialarray=[]
for TrialIndex in range(0,NumberTrials):
    NumbersInRange=0
    for i in range(n):
            #counting the tosses (n tosses) in ach trail that fall within the given probability
         if random.random()<p:
                #counts the number of "good ones"
                NumbersInRange=1+NumbersInRange
    Trialarray.append(NumbersInRange)
Outcomearray=[]
#find the prob the coin fell with the right side up for all trails. 0 times to n times
for OutcomeIndex in range(0,n+1):
    Outcomearray.append(Trialarray.count(OutcomeIndex)/float(NumberTrials))
print(Outcomearray)

