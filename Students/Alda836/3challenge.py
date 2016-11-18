__author__ = ""  # Malik Aldabbagh
__NetID__ = ""  # 323008160
__GitHubID__ = ""  # alda836
__SelfGrade__ = ""  # 5 out of 5
__Challenge__ = "3"



"""

Random Signals and Systems

Course: ECEN 303-502

Maximum Grade: 5

"""





import random
import math
import matplotlib.pyplot as plt



def biasedcoinflip(p=0.5):
    """
    This method returns a one with probability p and it returns a zero with
    probability (1 - p). The default parameter is p=0.5; this can be changed
    by passing an argument to the method.
    """
    return math.floor(random.random() + p)

def binomialflips(n=1, p=0.5):
    """
    This method returns a binomial random variable with parameters n and p.
    The default parameters are n=1 and p=0.5; this can be changed by passing
    arguments to the method.
    """
    numberones = 0
    for BinomialIndex in range(0,n):
        numberones += biasedcoinflip(p)
    return numberones



def poisson(parameterpoisson=10):
    """
    This is a function that calculate the sum or the total number of occurrence of an event for a given period of time. The probability of the average occurrence
     of an event is lambda. the total number of the event is k.
    """
    lambdaa = parameterpoisson # labda parameter which =10
    k = 0 # to incroment for the summation. this represent the total umber of events.
    sum = 0 # the value of the summation

    while (sum < random.random()):
        a = pow(lambdaa,k) # lambda^(k)
        b = math.exp(-1*lambdaa) # e^(-lambda)
        c = math.factorial(k) # k!
        sum += (a*b)/c # the summation
        k += 1
    return k - 1





def experiment(parameterpoisson=10, p=0.5):
    return binomialflips(poisson(parameterpoisson), p)
    # return poisson(binomialflips(parameterpoisson3, p))



ParameterPoisson = 10
NumberTrials = 100000
TrialSequence = []


for TrialIndex1 in range(0, NumberTrials):
    TrialSequence.append(experiment(ParameterPoisson))
print(sum(TrialSequence)/len(TrialSequence))



Distribution = []
for OutcomeIndex1 in range(0, 21):
    Distribution.append(TrialSequence.count(OutcomeIndex1) / (1.0 * NumberTrials))



OutcomeIndex2 = range(0, 21)
num_bins = len(OutcomeIndex2)
bar_width = 0.8
XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex2]
opacity = 0.4


plt.bar(OutcomeIndex2, Distribution, bar_width, alpha=opacity, color='b')
plt.xlabel("Value")
plt.ylabel("Probability")
plt.xticks(XticksIndex, OutcomeIndex2)
plt.show()



# Question 1: What is the mean of experiment()?

# Answer 1: 3.97971



# Question 2: What is the type of experiment()?

# Answer 2: poisson random variable


# Question 3: Do the two distributions match?

# Answer 3: yes.
