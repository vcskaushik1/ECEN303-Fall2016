__author__ = "Trevor Spohrer"
__NetID__ = "tspohrer"
__GitHubID__ = "tspohrer"
__SelfGrade__ = "5"
__Challenge__ = "2"

"""
 Random Signals and Systems
 Course: ECEN 303-502
 Maximum Grade: 5pt
 """

 import random
 import math
 import matplotlib.pyplot as plt


 ParameterP = 1.0/3.0
 ParameterA = 1.0/3.0
 ParameterB = 1.0/2.0   
 NumberTrials = 100000


 def biasedcoinflip(p=0.5):
     return math.floor(random.random() + p)


 def geometricflip(p=0.5):
	 #offlips = 1
     while biasedcoinflip(p) != 1:
         numberflips += 1
     return #offlips


 print "Part 1\n"

 Trials = []
 for TrialIndex1 in range(0, NumberTrials):
     Trials.append(geometricflip(ParameterP))

 Answer1 = Trials.count(4)/float(len(Trials))
 print("The empirical probability that the  number of flips is 4 is " + repr(solution1) + ".")


 EvenTrials = 0
 for TrialIndex2 in range(0, NumberTrials):
    if Trials[TrialIndex2]%2 == 0:
         EvenTrials += 1

 Answer2 = Trials.count(4)/ float(EvenTrials)
 print("The empirical probability that the number of flips is 4 conditional on number of flips being even is " + repr(solution2) + ".")

 print "Part 2\n"

 def GeometricFlip(p = 0.5,q = 0.5):
     set = 0
     countA = 0
     countB = 0
     count = 0
 while set == 0:
        SpotA = biasedcoinflip(p)
          SpotB = biasedcoinflip(q)

 if SpaceA == SpaceB:
             count +=1
     elseif (SpaceA == 1 - SpaceB):
             count += 1
             countA += SpotA
             countB += SpotB
             set = 1
 return(count,countA,countB)
 Trials2 = []
 FinalA = 0
 FinalB = 0
 for TrialIndex3 in range(0, NumberTrials):
     Result = geometricFlip(ParameterA,ParameterB)
     Trials2.append(Result[0])
     FinalA += Result[1]
     FinalB += Result[2]

 Answer3 = Trials2.count(2)/ float(NumberTrials)
 Answer4 = A/ float(NumberTrials)
 Answer5 = B/ float(NumberTrials)

 print ("The empirical probability that 2 is the number of flips" + repr(solution3) + ".")

 print ("The empirical probability that 1 is showing on coin A when the stopping condition is met is " + repr(solution4)+ ".")

 print ("The empirical probability that 1 is showing for coin B when the stopping condition is met is " + repr(solution5)+ ".")
