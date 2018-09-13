import random
'''
random - returns time in milliseconds since January 1, 1968.
That is called seed generating
Given a seed you always get the same sequence
'''
random.seed(0) # use zero as seed

def rollDie():
    '''
    Returns a randomly chosen int beween 1 and 6
    '''
    return random.choice([1, 2, 3, 4, 5, 6])

def testRoll(n = 10):
    result = ''
    for i in range(n):
        result += str(rollDie())
    print(result)

def runSim(goal, numTrials):
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    print("Actual probability=",
            round(1/(6**len(goal)), 8))
    estProbability = round(total/numTrials, 8)
    print('Estimated Probability =',
            round(estProbability, 8))

runSim('66', 1000)