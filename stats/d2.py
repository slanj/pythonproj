import pylab as plt
import numpy as np

a = np.random.normal(10, 3, 1000)
b = np.random.normal(10, 5, 1000)
plt.figure('a')
plt.hist(a, 10)

plt.figure('b')
plt.hist(b, 10)
plt.show()