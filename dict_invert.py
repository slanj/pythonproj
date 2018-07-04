def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
    inverted = {}
    for key, value in d.items():
        if value not in inverted:
            inverted[value] = []
            for inkey, invalue in d.items():
                if invalue == value:
                    inverted[value].append(inkey)
            inverted[value].sort()

    return inverted

d = {4:True, 2:True, 0:True}
print(dict_invert(d))