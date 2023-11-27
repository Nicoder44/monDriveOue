Clusters = [[1, 3, 2], [5, 7, 6, 8]]

means = []
E = 0
for Cluster in Clusters:
    mean_c = 0
    for c in Cluster:
        mean_c += c
    mean_c /= Cluster.__len__()
    means.append(mean_c)
idx = 0
for Cluster in Clusters:
    for c in Cluster:
        E += abs(means[idx] - c)
    idx += 1
print("Final E for the Clusters: " + str(E))

#With sklearn.cluster.KMeans
print("ex2-------------------------------------------------------------------")
################################################################################
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
#scaler = StandardScaler(copy=True, with_mean=True, with_std=True)

dots = np.array([[1, 7, 3, 6, 2, 5, 8]]).transpose()

#data = scaler.fit_transform(dots)

kmeans = KMeans(n_clusters=2, n_init=10)
kmeans.fit(dots)
#print("Identifiants: ", ids)
print("Data : ", dots)
print("Categories : ", kmeans.labels_)
print("ex3-------------------------------------------------------------------")





