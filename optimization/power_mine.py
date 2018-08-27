from itertools import chain, combinations

def powerset(iterable):
    return chain.from_iterable(combinations(list(iterable), r) for r in range(len(iterable)+1))

results = list(powerset([1, 2, 3]))
print(results)