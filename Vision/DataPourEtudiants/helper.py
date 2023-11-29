import numpy as np
import cv2

def keypoints2numpyarray(kp):
    nb_points_ref=len(kp)
    points_ref=np.zeros((nb_points_ref,2),dtype=np.float)
    for i in range(0,nb_points_ref):
        points_ref[i,:]=kp[i].pt
    return points_ref

def create_K(dX, dY, N, M, dx, dy, Z):
    # Calcul des focales en pixels
    fx = (Z * dX / dx)
    fy = (Z * dY / dy)

    # Calcul du centre de l'image dans le repère de l'image
    x0 = N / 2
    y0 = M / 2

    # Création de la matrice intrinsèque K
    K = np.array([[fx, 0, x0],
                  [0, fy, y0],
                  [0, 0, 1]])

    return K

K = create_K(243, 170, 960, 540, 155, 105, 500)

print(K)