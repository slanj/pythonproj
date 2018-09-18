def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for
        the largest value in L then for the second largest, and so on to
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does
                not yield a set of multipliers such that the equation sums to 's'
    """
    multipliers = []
    ostatok = s
    for item in L:
        for m in range(s, 0, -1):
            if item * m <= ostatok:
                multipliers.append(m)
                ostatok -= item * m
                break
            if m == 1:
                multipliers.append(0)
    test = 0
    for i in range(len(L)):
            test += L[i]*multipliers[i]
    if test != s:
        return "no solution"

    return sum(multipliers)

L = [10, 5, 1]
s = 11
print(greedySum(L, s))