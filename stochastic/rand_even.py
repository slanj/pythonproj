import random

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    while True:
      i = random.randint(0, 99)
      if i % 2 == 0:
          return i

def genEvenChoice():
    return random.choice(range(0, 50))*2

for n in range(10):
    print(genEven())

for n in range(10):
    print(genEvenChoice())