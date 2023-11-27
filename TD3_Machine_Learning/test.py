from sklearn.model_selection import train_test_split
from ucimlrepo import fetch_ucirepo
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
import sklearn
data = pd.read_csv('winequality-red.csv', sep=';')
print(data.head(20))
# creer la matrice de donnees
X = data.drop('quality',axis=1).copy()
# creer le vecteur d'etiquettes
y = data['quality'].values
y = y.flatten()
print(y)
# transformer en un probleme de classification binaire
y_class = np.where(y<6, 0, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

scaler = StandardScaler()
print(scaler.fit(data))
#sklearn.model_selection.train_test_split()
