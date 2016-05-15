#-*-coding:utf-8 -*-
import cv2

img = cv2.imread('images/lena.jpg')


lower_reso = cv2.pyrDown(img) # 원본 이미지의 1/4 사이즈
higher_reso = cv2.pyrUp(img) #원본 이미지의 4배 사이즈

cv2.imshow('img', img)
cv2.imshow('lower', lower_reso)
cv2.imshow('higher', higher_reso)

cv2.waitKey(0)

cv2.destroyAllWindows()