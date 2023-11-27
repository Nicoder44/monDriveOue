import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import LinearSVC
import pandas as pd

data = pd.read_csv("ex2data.csv")
# AFFICHAGE DE QUELQUES LIGNES
print("Données brutes:\n",data.head(5))

# Informations sur les colonnes
print(data.info())

# Statistiques elementaires sur les colonnes
print(data.describe())

plt.scatter(data["x"], data["y"], c = data["label"])

clf = LinearSVC(C=2800)
clf.fit(data[["x","y"]],data["label"])

#on récupère le coefficient directeur de la droite
w = clf.coef_[0]
print(w)
a = -w[0] / w[1]

#trace l'hyperplan
xx = np.linspace(0,4)
yy = a * xx - clf.intercept_[0] / w[1]
h0 = plt.plot(xx, yy, 'k-', label="Hyperplan")
plt.legend()




plt.show()

