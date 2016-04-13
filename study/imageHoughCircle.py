#-*-coding:utf-8-*-

import cv2
import numpy as np

img = cv2.imread('copy.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

"""
 HoughCircles
     - param1 : Image
     - Param2 : Method
     - param3: inverse ratio of resolution
     - param4 : min_dist. 중심과의 최소 거리
     - param5 : Canny 적용시 Threshold
     - param6 : 중심점 찾기 threshold

"""

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,param1=50,param2=25,minRadius=0, maxRadius=0)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('img', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()