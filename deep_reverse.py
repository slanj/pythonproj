def deep_reverse2(L):
    """ assumes L is a list of lists whose elements are ints
    Not mutates L.
    """
    # Your code here
    AL = []
    for i in range(len(L)-1, -1, -1):
        temp = []
        for j in range(len(L[i])-1, -1, -1):
            temp.append(L[i][j])
        AL.append(temp)
    return(L)

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    # Your code here
    L.reverse()
    for item in L:
        item.reverse()
    return(L)


L = [[1, 2], [3, 4], [5, 6, 7]]

deep_reverse(L)
print(L)