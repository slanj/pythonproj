import numpy as np

x = [1, 2, 3, 55, 66, 3, 2, 1]
x1, x2, x3 = np.split(x,[3, 5])
print(x1, x2, x3)
# [1 2 3] [55 66] [3 2 1]

grid = np.arange(16).reshape((4, 4))
print(grid)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

upper, lower = np.vsplit(grid, [2])
print(upper)
# [[0 1 2 3]
#  [4 5 6 7]]
print(lower)
# [[ 8  9 10 11]
#  [12 13 14 15]]

left, right = np.hsplit(grid, [2])
print(left)
# [[ 0  1]
#  [ 4  5]
#  [ 8  9]
#  [12 13]]
print(right)
# [[ 2  3]
#  [ 6  7]
#  [10 11]
#  [14 15]]