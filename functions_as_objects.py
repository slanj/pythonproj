# Apply given function to each element of a list
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L

L = [1, -4, 8, -9]

applyToEach(L, abs)
print(L)

applyToEach(L, int)
print(L)

# Lists of functions
def applyFuns(L, x):
    for f in L:
        print (f(x))

applyFuns([abs, int], 4.5)

# Python provides Higher Order Procedure (HOP) - map
for elt in map(abs, [1, -2, 3, -4]):
    print(elt)

L1 = [1, 28, 36]
L2 = [2, 57, 9]

for elt in map(min, L1, L2):
    print(elt)


def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

print(applyEachTo([inc, square, halve, abs], -3))
print(applyEachTo([inc, square, halve, abs], 3.0))