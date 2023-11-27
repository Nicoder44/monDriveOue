# Mémo sur la Classification Non Supervisée avec les K-Means et le Gaussian Mixture Model

## 1. Classification Non Supervisée

La classification non supervisée vise à regrouper automatiquement des données similaires sans connaître leurs étiquettes. Deux techniques courantes sont les K-Means et le Gaussian Mixture Model (GMM).

## 2. K-Means

### Algorithme

L'algorithme K-Means cherche à minimiser l'inertie ou la variance intra-classe pour un nombre de classes \( k \) fixé. La formule de l'inertie \( E \) est donnée par :

\[ E = \sum_{i=1}^{K} \sum_{x_j \in C_i} d(x_j, \bar{x}_i) \]

- \( C_i \) : Cluster \( i \)
- \( \bar{x}_i \) : Centre du cluster \( i \)
- \( d(.,.) \) : Distance entre deux points (par exemple, distance euclidienne)

### Exemples de Questions

- Que vaut \( E \) pour différentes partitions \( C_1 = (A, C, E, F) \) et \( C_2 = (B, D, G) \) ?
- Quelle est la meilleure partition ? (Utilisation de [sklearn.cluster.KMeans])
- Quels sont les clusters pour un nombre donné \( k \) de catégories ?
- Faire le moyenne de chaque cluster, puis parcourir tous les points et faire la différence entre le point et la moyenne de son cluster. E vaut somme de abs(point - moy cluster)
- On cherche a minimiser E

### Application aux Images

- Regroupement d'images en catégories basé sur la similarité.

## 3. Gaussian Mixture Model (GMM)

Le GMM modélise chaque cluster par une densité de probabilité (loi normale) en supposant que les données peuvent être représentées comme une somme pondérée de K gaussiennes.

### Formule de Probabilité

\[ p(x) = \sum_{i=1}^{K} \pi_i \cdot p_{\mu_i, \sigma_i}(x) \]

- \( \pi_i \) : Proportion de la classe \( i \)
- \( p_{\mu_i, \sigma_i}(x) \) : Densité de probabilité gaussienne

### Exemples de Questions

- Quels sont les regroupements pour une hypothèse de 3 groupes ?
- Quelle est la proportion de chaque classe dans le mélange ?
- Quelles sont les propriétés (moyenne, matrice de variance-covariance) de la loi normale associée à un groupe spécifique ?

### Application aux Images

- Regroupement d'images en catégories basé sur le modèle de mélange gaussien.

---

**Remarque :** Ces techniques sont utilisées pour la classification non supervisée, où les données ne sont pas étiquetées, et permettent de découvrir des structures intrinsèques dans les ensembles de données.

```
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
```


