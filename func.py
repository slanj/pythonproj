def hello(name = "Nikifor"):
    """
    Very useful function
    """
    greet = "Hello, " + str(name)
    print(greet)
    return greet

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = base
    if exp == 0:
        return 1
    else:
        for i in range(1, exp):
            result *= base
            print(result)
    return result

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here

    if exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        return  base*recurPower(base, exp-1)

hello()
hello("Peter")

iterPower(2, 4)