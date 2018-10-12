import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    numbered = {}
    for i in range(len(choices)):
        numbered[i] = [choices[i], 0]
    choices = sorted(choices)
    temp = 0
    taken = []
    for i in range(len(choices)-1, -1, -1):
        if temp + choices[i] <= total:
            temp += choices[i]
            taken.append(choices[i])
    positions = []
    for t in taken:
        for n in numbered.keys():
            if numbered[n][0] == t and numbered[n][1] == 0:
                positions.append(n)
                numbered[n][1] = 1
                break
    result = []
    for i in range(len(choices)):
        if i in positions:
            result.append(1)
        else:
            result.append(0)

    return np.array(result)

results = find_combination([10, 10, 11, 11, 11], 20)
print(results)