#-*- coding:utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('images/logo.png')

rows, cols = img.shape[:2]

cv2.getRo

# 변환 행렬, X축으로 10, Y축으로 20 이동
M = np.float32([[1,0,10],[0,1,20]])

dst = cv2.warpAffine(img, M,(cols, rows))
cv2.imshow('Original', img)
cv2.imshow('Translation', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

