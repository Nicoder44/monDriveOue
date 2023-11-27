import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn import datasets

def plot_boundary(clf, X, y):
    h = 0.001
    x_min, x_max = X[:, 0].min() - .1, X[:, 0].max() + .1
    y_min, y_max = X[:, 1].min() - .1, X[:, 1].max() + .1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),np.arange(y_min, y_max, h))
    
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
        
    plt.figure()
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
    
    plt.scatter(X[:, 0], X[:, 1], c=y, s = 100)
    plt.title('score : ' + str(clf.score(X,y)))
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.show()

iris = datasets.load_iris()

X = iris["data"][:,(2,3)]
y = (iris["target"] == 2).astype(np.float64)
    
clf_iris = SVC(kernel='rbf', gamma=2, C=3)
clf_iris.fit(X,y)

print("score d'entrainement:",clf_iris.score(X,y))
    
plot_boundary(clf_iris,X,y)
