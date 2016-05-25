#-*- coding:utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('images/rectangle.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,127,255,0)

image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# 첫번째 contours의 moment 특징 추출
cnt = contours[0]
M = cv2.moments(cnt)

print M.items()

