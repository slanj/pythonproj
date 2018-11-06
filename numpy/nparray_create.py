import numpy as np

"""
Working with NumPy Arrays
"""

# Create an array

a = np.array([1, 2, 5])
print(a)
# [1 2 5]

b = np.array([5, 7.7, 4])
print(b)
# [5.  7.7 4. ]

c = np.array([8, 9, 1], dtype='float32')
print(c)
# [8. 9. 1.]

tens = np.zeros(10, dtype=int)
print(tens)
# [0 0 0 0 0 0 0 0 0 0]

ones = np.ones((3, 7))
print(ones)
# [[1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1.]]

pi = np.full((3, 3), 3.14)
print(pi)
# [[3.14 3.14 3.14]
#  [3.14 3.14 3.14]
#  [3.14 3.14 3.14]]

rang = np.arange(0, 20, 2)
print(rang)
# [ 0  2  4  6  8 10 12 14 16 18]

quart = np.linspace(0, 1, 5)
print(quart)
# [0.   0.25 0.5  0.75 1.  ]

r = np.random.random((3, 3))
print(r)
# [[0.67652966 0.32369373 0.4233812 ]
#  [0.6953303  0.83887377 0.02019276]
#  [0.00561717 0.68126844 0.58347282]]

normal = np.random.normal(0, 2, 10)
print(normal)
# [-4.28190653 -0.91278821  0.31164536  1.48733714 -1.31763542 -1.16436339
#  -2.27240085 -0.60607322  1.62205948 -2.73993085]

r2 = np.random.randint(0, 10, 5)
print(r2)
# [5 6 5 1 9]