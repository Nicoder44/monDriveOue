import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
    
data = pd.DataFrame(np.array([[0, 0, 1],[0, 1, 0],[1, 0, 0],[1, 1, 1]]), columns=["x", "y", "label"])
print(data)

plt.scatter(data["x"], data["y"], c=data["label"])

#on appelle le classifieur SVM
clf_xor = LinearSVC()
clf_xor.fit(data[["x", "y"]], data["label"])

#on affiche le score d'entrainement



#on récupère le coefficient directeur de la droite
w = clf_xor.coef_[0]
print(w)
a = -w[0] / w[1]
#trace l'hyperplan
xx = np.linspace(0,1)
yy = a * xx - clf_xor.intercept_[0] / w[1]
h0 = plt.plot(xx, yy, 'k-', label="Hyperplan")
plt.legend()
plt.show()

