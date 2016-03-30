#-*- coding:utf-8 -*-
import cv2
import numpy as np 

img = cv2.imread('copy.png',0)
rows, cols = img.shape

# 평행 이동시 2차원 행렬
# [1,0,X],[0,1,Y] X축,Y축 이동 
M = np.float32([[1,0,5],[0,1,5]])

dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
