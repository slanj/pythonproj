import numpy as np

m = np.array([[17, 24, 1],
              [23, 5, 7],
              [4, 6, 13],
              [10, 12, 19],
              [11, 18, 25]])
print(m.T)

v = np.array([0, 0, 0, 1, 0])

print(np.dot(v, m))
print(v[:, np.newaxis])