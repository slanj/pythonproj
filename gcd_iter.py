def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a >= b:
        gcd = b
    else:
        gcd = a

    while a % gcd > 0 or b % gcd > 0:
        gcd -= 1

    print(gcd)
    return gcd


gcdIter(56, 182)