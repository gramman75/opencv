#-*- coding:utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

A = cv2.imread('images/apple.jpg')
B = cv2.imread('images/orange.jpg')

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in xrange(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    temp = cv2.resize(gpA[i-1], (GE.shape[:2][1], GE.shape[:2][0]))
    L = cv2.subtract(temp,GE)
    lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in xrange(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    temp = cv2.resize(gpB[i - 1], (GE.shape[:2][1], GE.shape[:2][0]))
    L = cv2.subtract(temp, GE)
    # L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols/2], lb[:,cols/2:]))
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in xrange(1,6):
    ls_ = cv2.pyrUp(ls_)
    temp = cv2.resize(LS[i],(ls_.shape[:2][1], ls_.shape[:2][0]))
    ls_ = cv2.add(ls_, temp)

# image with direct connecting each half
real = np.hstack((A[:,:cols/2],B[:,cols/2:]))

cv2.imshow('real', real)
cv2.imshow('blending', ls_)
cv2.waitKey(0)
cv2.destroyAllWindows()
