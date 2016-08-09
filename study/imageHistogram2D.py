#-*- coding:utf-8-*-
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

"""
# 2D Histogram
    . 이미지를 2가지 측면에서 분석 
    . 이미지를 HSV Format으로 변경하여 분석
    . 이미지의 내용을 수치화 할 수 있고, 이를 이용해서 유사한 이미지를 찾는데 사용됨.=> Object Detection    
    . calcHist([image],[channel],mask,[bins],[range])
        . image : HSV로 변환된 이미지
        . channel: 0-> Hue, 1->Saturation 
        . bins:[180,256] 첫번째는 Hue, 두번째는 Saturation
        . range:[0,180,0,256] : Hue(0~180), Saturation(0,256)
"""

img = cv2.imread('images/home.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])

plt.imshow(hist) #, interpolation='nearest')
plt.show()

