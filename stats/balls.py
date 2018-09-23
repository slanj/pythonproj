import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    balls = [1, 0, 1, 0, 1, 0]
    same_color = 0
    for trial in range(numTrials):
        choice = sum(random.sample(balls, 3))
        if choice == 3 or choice == 0:
            same_color += 1
    return same_color/numTrials

print(noReplacementSimulation(11142))

