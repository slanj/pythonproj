'''
Rules of Broadcasting

Broadcasting in NumPy follows a strict set of rules to determine the interaction between the two arrays:

    Rule 1: If the two arrays differ in their number of dimensions, the shape of the one with fewer dimensions is padded with ones on its leading (left) side.
    Rule 2: If the shape of the two arrays does not match in any dimension, the array with shape equal to 1 in that dimension is stretched to match the other shape.
    Rule 3: If in any dimension the sizes disagree and neither is equal to 1, an error is raised.
'''

import numpy as np

a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
print(a + b)
# [5 6 7]

M = np.ones((3, 3))
# [[ 1.,  1.,  1.],
# [ 1.,  1.,  1.],
# [ 1.,  1.,  1.]]

M + a
# [[ 1.,  2.,  3.],
# [ 1.,  2.,  3.],
# [ 1.,  2.,  3.]]

a = np.arange(3)
b = np.arange(3)[:, np.newaxis]

print(a)
print(b)
# [0 1 2]
# [[0]
#  [1]
#  [2]]

print(a + b)
# [[0, 1, 2],
# [1, 2, 3],
# [2, 3, 4]]

M = np.ones((2, 3))
a = np.arange(3)
print(M + a)
# [[1. 2. 3.]
#  [1. 2. 3.]]

a = np.arange(3).reshape((3, 1))
b = np.arange(3)

'''
Let's consider an operation on these two arrays. The shape of the arrays are

    a.shape = (3, 1)
    b.shape = (3,)

Rule 1 says we must pad the shape of b with ones:

    a.shape -> (3, 1)
    b.shape -> (1, 3)

And rule 2 tells us that we upgrade each of these ones to match the corresponding size of the other array:

    a.shape -> (3, 3)
    b.shape -> (3, 3)

Because the result matches, these shapes are compatible. We can see this here:

'''
print(a + b)
# [[0 1 2]
#  [1 2 3]
#  [2 3 4]]

np.random.seed(0)

X = np.random.random((10, 3))
# [[0.5488135 , 0.71518937, 0.60276338],
# [0.54488318, 0.4236548 , 0.64589411],
# [0.43758721, 0.891773  , 0.96366276],
# [0.38344152, 0.79172504, 0.52889492],
# [0.56804456, 0.92559664, 0.07103606],
# [0.0871293 , 0.0202184 , 0.83261985],
# [0.77815675, 0.87001215, 0.97861834],
# [0.79915856, 0.46147936, 0.78052918],
# [0.11827443, 0.63992102, 0.14335329],
# [0.94466892, 0.52184832, 0.41466194]]

Xmean = X.mean(0)
print(Xmean)
# [0.52101579, 0.62614181, 0.59620338]

X_centered = X - Xmean
# [[ 0.02779771,  0.08904756,  0.00655999],
# [ 0.02386739, -0.20248701,  0.04969073],
# [-0.08342858,  0.26563119,  0.36745938],
# [-0.13757427,  0.16558323, -0.06730846],
# [ 0.04702877,  0.29945483, -0.52516732],
# [-0.43388649, -0.60592341,  0.23641646],
# [ 0.25714096,  0.24387034,  0.38241496],
# [ 0.27814277, -0.16466245,  0.18432579],
# [-0.40274137,  0.01377921, -0.45285009],
# [ 0.42365312, -0.10429349, -0.18154144]]

# To double-check that we've done this correctly, we can check that the centered array has near zero mean:

print(X_centered.mean(0))
# [1.11022302e-17 1.22124533e-16 3.33066907e-17]

# To within machine precision, the mean is now zero.