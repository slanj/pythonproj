import random
def det():
    nums = [10, 12, 14, 16, 18, 20]
    i = 0
    while True:
        i+= 1
        yield nums[i%6]


def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 10

for n in range(10):
    print(deterministicNumber())
