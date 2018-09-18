from itertools import chain, combinations

'''
def max_contig_sum2(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a subsequence in L """
    variants = list(chain.from_iterable(combinations(list(L), r) for r in range(len(L)+1)))
    sums = max([sum(item) for item in variants])
    return sums
'''

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    variants = []
    temp = []
    for start in range(len(L)):
        temp.append(L[start])
        variants.append(temp[:])
        second = start + 1
        for j in range(second, len(L)):
            temp.append(L[j])
            variants.append(temp[:])
        temp = []
    sums = max([sum(item) for item in variants])

    return sums

results = max_contig_sum([3, 4, -1, 5, -4])
print(results)