import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs

np.random.seed(0)

# Next we will be making random clusters of points by using the make_blobs class.
#  The make_blobs class can take in many inputs,
# but we will be using these specific ones.

# Input

#     n_samples: The total number of points equally divided among clusters.
#         Value will be: 5000
#     centers: The number of centers to generate, or the fixed center locations.
#         Value will be: [[4, 4], [-2, -1], [2, -3],[1,1]]
#     cluster_std: The standard deviation of the clusters.
#         Value will be: 0.9

# Output

#     X: Array of shape [n_samples, n_features]. (Feature Matrix)
#         The generated samples.
#     y: Array of shape [n_samples]. (Response Vector)
#         The integer labels for cluster membership of each sample.


X, y = make_blobs(n_samples=5000, centers=[[4,4], [-2, -1], [2, -3], [1, 1]], cluster_std=0.9)

# Display the scatter plot of the randomly generated data.
plt.scatter(X[:, 0], X[:, 1], marker='.')
plt.show()

# Now that we have our random data, let's set up our K-Means Clustering.

# The KMeans class has many parameters that can be used,
# but we will be using these three:

#     init: Initialization method of the centroids.
#         Value will be: "k-means++"
#         k-means++: Selects initial cluster centers for k-mean clustering
#         in a smart way to speed up convergence.
#     n_clusters: The number of clusters to form as well
#     as the number of centroids to generate.
#         Value will be: 4 (since we have 4 centers)
#     n_init: Number of time the k-means algorithm will be run
#     with different centroid seeds. The final results will be
#     the best output of n_init consecutive runs in terms of inertia.
#         Value will be: 12

# Initialize KMeans with these parameters,
# where the output parameter is called k_means.

k_means = KMeans(init = "k-means++", n_clusters = 4, n_init = 12)
k_means.fit(X)
k_means_labels = k_means.labels_
k_means_cluster_centers = k_means.cluster_centers_

# So now that we have the random data generated and the KMeans model initialized,
# let's plot them and see what it looks like!

# Initialize the plot with the specified dimensions.
fig = plt.figure(figsize=(6, 4))

# Colors uses a color map, which will produce an array of colors based on
# the number of labels there are. We use set(k_means_labels) to get the
# unique labels.
colors = plt.cm.Spectral(np.linspace(0, 1, len(set(k_means_labels))))

# Create a plot
ax = fig.add_subplot(1, 1, 1)

# For loop that plots the data points and centroids.
# k will range from 0-3, which will match the possible clusters that each
# data point is in.
for k, col in zip(range(len([[4,4], [-2, -1], [2, -3], [1, 1]])), colors):

    # Create a list of all data points, where the data poitns that are
    # in the cluster (ex. cluster 0) are labeled as true, else they are
    # labeled as false.
    my_members = (k_means_labels == k)

    # Define the centroid, or cluster center.
    cluster_center = k_means_cluster_centers[k]

    # Plots the datapoints with color col.
    ax.plot(X[my_members, 0], X[my_members, 1], 'w', markerfacecolor=col, marker='.')

    # Plots the centroids with specified color, but with a darker outline
    ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,  markeredgecolor='k', markersize=6)

# Title of the plot
ax.set_title('KMeans')

# Remove x-axis ticks
ax.set_xticks(())

# Remove y-axis ticks
ax.set_yticks(())

# Show the plot
plt.show()