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

roi = cv2.imread('rose_red.png')
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

"""
# 2. 전체 이미지를 HSV로 변환. 
"""

target = cv2.imread('rose_cat.jpg')
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

"""
# 6. dst의 결과가 각져보이기 때문에 원 모양을 적용하여 경계를 부드럽게함. 
   filter2D
     argu1: Source
     argu2: depth, -1이면 source와 동일 
     argu3: kernel. 적용 대상 
     argu4: output
"""

disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(1,1))
cv2.filter2D(dst,-1,disc,dst)

"""
# 7. 찾은 대상영역을 Binary Image로 변환함. Morpholoogy를 통해서 노이즈 제거
"""

ret,thresh = cv2.threshold(dst,50,255,cv2.THRESH_BINARY_INV)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(6,6))
thresh = cv2.dilate(thresh,kernel,iterations = 3)
# thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,kernel)
# thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

"""
#8. bitwhise연상은 동일한 demension을 가져야 하기 때문에 thresh를 대상 이미지와 같은 3차원으로 변환 
"""

thresh = cv2.merge((thresh,thresh,thresh))

"""
#9. biwise연상을 통해서 대상 이미지에 threshold적용 
"""

res = cv2.bitwise_and(target,thresh)

"""
#10. 원본,적용 Mask, 결과를 하나의 이미지로 붙임.
"""

res = np.vstack((target,thresh,res))

cv2.imwrite('rose_cat.png', res)

cv2.imshow('dst',res)
cv2.waitKey(0)
cv2.destroyAllWindows()