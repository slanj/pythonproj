import random, pylab
import numpy as np

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    if title != None:
        pylab.title(title)

    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.hist(values, numBins)
    pylab.show()


# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    values = []
    longest = []
    for trial in range(numTrials):
        for roll in range(numRolls):
            values.append(die.roll())
        temp = values[0]
        count = 1
        maxCount = 1
        for i in range(len(values)-1):
            if temp == values[i+1]:
                count += 1
            else:
                temp = values[i+1]
                count = 1

            if count > maxCount:
                maxCount = count
        longest.append(maxCount)
        values = []

    makeHistogram(longest, 10, "Mean of runs", "Longest runs")

    return round(getMeanAndStd(longest)[0], 3)




# a = np.random.normal(10, 5, 100)
# makeHistogram(a, 10, "X", "Y", "Graphik")


# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))