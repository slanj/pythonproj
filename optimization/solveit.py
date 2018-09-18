def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True
        In case of ties, return any one of them.
    """
    x = 100000

    while True:
        try:
            podhodit = test(x)
            if podhodit:
                return x
            x -= 1
        except:
            x -= 1

#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f2(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f2))

def f3(x):
    return 20 / x == 4
print(solveit(f3))

def f4(x):
    return x**2 + x + 0 == 0
print(solveit(f4))