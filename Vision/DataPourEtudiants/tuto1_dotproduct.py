import numpy as np

Z=500
K=np.array([  [1,2],
              [-1,3] ])
Kinv=np.linalg.inv(K)
print(Kinv)
point_pixels=np.array([1,2])

C=500*np.dot(Kinv,point_pixels)
print(C)

