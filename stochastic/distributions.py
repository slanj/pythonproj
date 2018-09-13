import random

def dist4():
    return random.randrange(0, 10)

def dist3():
    return int(random.random() * 10)

for i in range(10):
    print(random.random())

for i in range(10):
    print(dist3())