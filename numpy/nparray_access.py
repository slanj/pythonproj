import numpy as np
np.random.seed(0)

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3, 4))
x3 = np.random.randint(10, size=(3, 4, 5))

print(x1)
# [5 0 3 3 7 9]

print(x2)
# [[3 5 2 4]
#  [7 6 8 8]
#  [1 6 7 7]]

print("x3 ndim: ", x3.ndim)
print("x3 shape: ", x3.shape)
print("x3 size: ", x3.size)
# x3 ndim:  3
# x3 shape:  (3, 4, 5)
# x3 size:  60

print('dtype: ', x3.dtype)
print('itemsize: ', x3.itemsize, 'bytes')
print('nbytes: ', x3.nbytes, 'bytes')
# dtype:  int32
# itemsize:  4 bytes
# nbytes:  240 bytes

print(x2[2][3])
print(x2[2, 3])
# 7
# 7

print(x1[2:5])
# [3 3 7]

print(x1[::2]) # every second element
# [5 3 7]

print(x1[::-1]) # every elemant in reverse order
# [9 7 3 3 0 5]

print(x2[1:3, :3]) # two rows, three columns
# [[7 6 8]
#  [1 6 7]]

print(x2[:, 0]) # first column
# [3 7 1]

print(x2[0, :]) # first row
# [3 5 2 4]

x2_sub_copy = x2[:2, :2].copy() # make a copy of an array
print(x2_sub_copy)
# [[3 5]
#  [7 6]]

grid = np.arange(1, 10).reshape((3, 3)) # put numbers 1-9 in a table 3x3
print(grid)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

x = np.array([1, 2, 3]) # put numbers 1-9 in a table 3x1
print(x.reshape((3, 1)))
# [[1]
#  [2]
#  [3]]

print(x[:, np.newaxis])
# [[1]
#  [2]
#  [3]]

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
print(np.concatenate([x, y])) # unite two arrays
# [1 2 3 3 2 1]

grid = np.array([[1, 2, 3],
                 [4, 5, 6]])
print(np.concatenate([grid, grid], axis=1))
# [[1 2 3 1 2 3]
#  [4 5 6 4 5 6]]

print(np.vstack([x, grid])) # unite arrays vertically
# [[1 2 3]
#  [1 2 3]
#  [4 5 6]]

y = y.reshape((3, 1))[0:2]
print(np.hstack([grid, y])) # unite arrays horizontally
# [[1 2 3 3]
#  [4 5 6 2]]