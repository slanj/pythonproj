def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    interselect = {}
    difference = {}

    for key1, value1 in d1.items():
        for key2, value2 in d2.items():
             if key1 == key2:
                 interselect[key1] = f(value1, value2)

    for key1, value1 in d1.items():
        uniq = True
        for key2, value2 in d2.items():
             if key1 == key2:
                 uniq = False
        if uniq:
            difference[key1] = value1

    for key2, value2 in d2.items():
        uniq = True
        for key1, value1 in d1.items():
             if key1 == key2:
                 uniq = False
        if uniq:
            difference[key2] = value2

    return interselect, difference


def f(a, b):
    return a + b

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

print(dict_interdiff(d1, d2))