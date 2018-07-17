def genFib():
    fib_1 = 1
    fib_2 = 0
    while True:
        next = fib_1 + fib_2
        yield next
        fib_2 = fib_1
        fib_1 = next

def genPrime():
    x = 2
    primes = [2]
    while True:
        yield x
        #A candidate number x is prime if (x % p) != 0 for all earlier primes p
        isPrime = False
        while isPrime == False:
            x += 1
            isPrime = True
            for p in primes:
                if (x % p) == 0:
                    isPrime = False
        primes.append(x)


fib = genFib()
prim = genPrime()

print('Fibonacci:')
for i in range(0, 5):
    print(fib.__next__())

print('\n')
print('Primes:')

for i in range(0, 5):
    print(prim.__next__())
