def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')

    lens = [len(x) for x in L]
    mean = sum(lens)/float(len(lens))
    tot = 0.0
    for x in lens:
        tot += (x - mean)**2
    std = (tot/len(lens))**0.5
    return std

def coefOfVar(X):
    '''
    The coefficient of variation is the standard deviation divided by the mean. Loosely, it's a measure of how variable the population is in relation to the mean.
    '''
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return std/mean

L = ['apples', 'oranges', 'kiwis', 'pineapples']
print(stdDevOfLengths(L))
print(coefOfVar([10, 4, 12, 15, 20, 5]))