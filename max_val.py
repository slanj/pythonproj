def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    # Your code here
    flat = flatten(t)
    return max(flat)


def flatten(L):
    '''
    Returns a flattened version of nested list L
    '''
    # base case: list with one element
    if len(L) == 1:
        if type(L[0]) == list or type(L[0]) == tuple:
            result = flatten(L[0])
        else:
            result = L
    elif type(L[0]) == list or type(L[0]) == tuple:
        result = flatten(list(L[0])) + flatten(list(L[1:]))
    else:
        result = [L[0]] + flatten(list(L[1:]))
    return result

print(flatten((5, (1,2), [[1],[9]])))
t = (5, (1,2), [[1],[9]])
print(max_val(t))