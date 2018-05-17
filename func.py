def hello(name = "Nikifor"):
    """
    Very useful function
    """
    greet = "Hello, " + str(name)
    print(greet)
    return greet

hello()
hello("Peter")