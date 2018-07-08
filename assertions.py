def avg(grades):
    '''
    Returns an average of a list.
    Raises an AssertionError if it is given an empty list for grades
    '''
    assert not len(grades) == 0, 'no grades data'
    return sum(grades) / len(grades)

print(avg([5, 6, 7]))
print(avg([]))