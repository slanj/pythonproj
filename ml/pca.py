# PCA is a dimensionality reduction technique;
# it lets you distill multi-dimensional data down to fewer dimensions,
# selecting new dimensions that preserve variance in the data as best it can.

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pylab as pl
from itertools import cycle

iris = load_iris()

numSamples, numFeatures = iris.data.shape
print(numSamples)
print(numFeatures)
print(list(iris.target_names))

# So, this tells us our data set has 150 samples (individual flowers) in it.
# It has 4 dimensions - called features here,
# and three distinct Iris species that each flower is classified into.

# While we can visualize 2 or even 3 dimensions of data pretty easily,
# visualizing 4D data isn't something our brains can do. So let's distill
# this down to 2 dimensions, and see how well it works:

X = iris.data
pca = PCA(n_components=2, whiten=True).fit(X)
X_pca = pca.transform(X)

# What we have done is distill our 4D data set down to 2D,
# by projecting it down to two orthogonal 4D vectors
# that make up the basis of our new 2D projection.
# We can see what those 4D vectors are,
# although it's not something you can really wrap your head around:

print(pca.components_)

# Let's see how much information we've managed to preserve:
print(pca.explained_variance_ratio_)
print(sum(pca.explained_variance_ratio_))

from pylab import *

colors = cycle('rgb')
target_ids = range(len(iris.target_names))
pl.figure()
for i, c, label in zip(target_ids, colors, iris.target_names):
    pl.scatter(X_pca[iris.target == i, 0], X_pca[iris.target == i, 1],
        c=c, label=label)
pl.legend()
pl.show()