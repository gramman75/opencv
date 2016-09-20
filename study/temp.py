<<<<<<< HEAD
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('images/noise.png',0)

# global thresholding
ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(img,(5,5),0)

ret3, th3 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# plot all the images and their histograms
images = [img, 0, th1, img, 0, th2, blur, 0, th3]

titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)', 'Original Noisy Image','Histogram',"Otsu's Thresholding", 'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in xrange(3):
	plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
	plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
	plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
	plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
	plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
	plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])

plt.show()
=======
#-*- coding:utf-8-*-
"""
#Histogram Backprojection
    . 찾고자하는 Object의 Pixcel값을 가지고, 현재 이미지에서 그 Pixel이 얼마나 분포되어 있는지 수치화 하는 과정.
    . 즉, 대상(추적대상)의 Histogram을 분석하고, 전체 이미지에 그 분석값이 얼마나 있는지 확인하여 대상을 찾을 수 있음.
    . 동영상의 대상 추적에 사용이 가능함. 
"""

import cv2
import numpy as np 

"""
# 1. roi를 선택하여 hsv로 변환. 찿고자하는 대상이 됨. 
"""

roi = cv2.imread('images/rose.jpg')
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

"""
# 2. 전체 이미지를 HSV로 변환. 
"""

target = cv2.imread('images/rose_cat.jpg')
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

"""
# 3. roi의 2D Histogram을 분석 
"""
roihist = cv2.calcHist([roi],[0,1],None,[180,256],[0,180,0,256])

"""
# 4. 정확한 값을 찿기 위해서 roi histogram에 대해서 Normalize수행. 
   argu1 : Source
   argu2 : Output
   argu3 : alpha. 정규화의 min값.
   argu4 : beta. 정규화의 max값.
   argu5 : normType. NORM_MINMAX,NORM_INF, NORM_L1,NORM_L2
"""

cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)

"""
# 5. 전체 이미지에 ROI를 적용하여 대상을 찾음.
"""

dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)
cv2.imshow('dst',dst);
cv2.waitKey()
cv2.destroyAllWindows()
>>>>>>> 22f27dd8e77f2cc0b7d0543eefc81fa4836ca007
