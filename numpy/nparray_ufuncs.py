import numpy as np

print(np.arange(1, 6) / 5)
# [0.2 0.4 0.6 0.8 1. ]

print(np.arange(5) / np.arange(1, 6))
# [0.         0.5        0.66666667 0.75       0.8       ]

x = np.arange(9).reshape((3, 3))
print(2**x)
# [[  1   2   4]
#  [  8  16  32]
#  [ 64 128 256]]

x = np.arange(4)
print("x     =", x)
print("x + 5 =", x + 5)    # np.add(x, 5)
print("x - 5 =", x - 5)    # np.substract(x, 5)
print("x * 2 =", x * 2)    # np.multiply(x, 2)
print("x / 2 =", x / 2)    # np.divide(x, 2)
print("x // 2 =", x // 2)  # np.floor_divide(x, 2)
# x     = [0 1 2 3]
# x + 5 = [5 6 7 8]
# x - 5 = [-5 -4 -3 -2]
# x * 2 = [0 2 4 6]
# x / 2 = [0.  0.5 1.  1.5]
# x // 2 = [0 0 1 1]

print("-x     =", -x)      # np.negative(x)
print("x ** 2 =", x ** 2)  # np.power(x, 2)
print("x % 2  =", x % 2)   # np.mod(x, 2)
# -x     = [ 0 -1 -2 -3]
# x ** 2 = [0 1 4 9]
# x % 2  = [0 1 0 1]

print(-(0.5*x + 1) ** 2)
# [-1.   -2.25 -4.   -6.25]

# get absolute values of array elements
a = np.arange(-5, 5)
print(a)
# [-5 -4 -3 -2 -1  0  1  2  3  4]
print(abs(a))
# [5 4 3 2 1 0 1 2 3 4]

theta = np.linspace(0, np.pi, 3)

print("theta      =", theta)
print("sin(theta) =", np.sin(theta))
print("cos(theta) =", np.cos(theta))
print("tan(theta) =", np.tan(theta))
# theta      = [0.         1.57079633 3.14159265]
# sin(theta) = [0.0000000e+00 1.0000000e+00 1.2246468e-16]
# cos(theta) = [ 1.000000e+00  6.123234e-17 -1.000000e+00]
# tan(theta) = [ 0.00000000e+00  1.63312394e+16 -1.22464680e-16]

x = [1, 2, 3]
print("x   =", x)
print("e^x =", np.exp(x))
print("2^x =", np.exp2(x))
print("3^x =", np.power(3, x))
# x   = [1, 2, 3]
# e^x = [ 2.71828183  7.3890561  20.08553692]
# 2^x = [2. 4. 8.]
# 3^x = [ 3  9 27]

x = [1, 2, 4, 10]
print("x        =", x)
print("ln(x)    =", np.log(x))
print("log2(x)  =", np.log2(x))
print("log10(x) =", np.log10(x))
# x        = [1, 2, 4, 10]
# ln(x)    = [0.         0.69314718 1.38629436 2.30258509]
# log2(x)  = [0.         1.         2.         3.32192809]
# log10(x) = [0.         0.30103    0.60205999 1.        ]

x = [0, 0.001, 0.01, 0.1]
print("exp(x) - 1 =", np.expm1(x))
print("log(1 + x) =", np.log1p(x))
# exp(x) - 1 = [0.         0.0010005  0.01005017 0.10517092]
# log(1 + x) = [0.         0.0009995  0.00995033 0.09531018]


# Assign an array to save result

x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out=y)
print(y)
#[ 0. 10. 20. 30. 40.]

y = np.zeros(10)
np.power(2, x, out=y[::2])
print(y)
# [ 1.  0.  2.  0.  4.  0.  8.  0. 16.  0.]


# Aggregation

x = np.arange(1, 6)
print(np.add.reduce(x))
# 15

print(np.multiply.reduce(x))
# 120

print(np.add.accumulate(x))
# [ 1  3  6 10 15]

print(np.multiply.accumulate(x))
# [  1   2   6  24 120]

# apply operation for every pair of elements
x = np.arange(1, 6)
print(np.multiply.outer(x, x))
# [[ 1  2  3  4  5]
#  [ 2  4  6  8 10]
#  [ 3  6  9 12 15]
#  [ 4  8 12 16 20]
#  [ 5 10 15 20 25]]

L = np.random.random(100)
print(L.sum()) # same np.sum(L)
# 54.45444326420844

print(np.min(L)) # same L.min()
# 0.017590748494069164

print(np.max(L)) # same L.max()
# 0.9882734041911772

M = np.random.rand(3, 4)
print(M)
# [[0.86400934 0.87054826 0.07571589 0.38570058]
#  [0.08197708 0.69073776 0.84698773 0.23421596]
#  [0.7055006  0.67504555 0.1356861  0.33119635]]

print(M.sum(axis=0)) # sum for every column
# [0.17906058 2.13618776 1.38091689 1.74123551]

print(M.sum(axis=1)) # sum for every row
# [1.91574394 1.81144783 1.71020896]

print(M.std(axis = 0)) # standard deviation for every row
# [0.16958465 0.09470688 0.15676532 0.31622955]

print(M.argmax()) # index of maximum element
# 11

print(np.percentile(M, q=4)) # compute 4th percentile of data
# 0.05424430029564519