#-*-coding:utf-8-*-
import cv2
import numpy as np 
"""
# Moments
    . Image의 여러특성(중심점,영역 등)계산을 지
"""
img = cv2.imread('rectangle.tiff')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray,127,255,0)
image,contours,hierarchy = cv2.findContours(thresh,1,2)

cnt = contours[2]
M = cv2.moments(cnt)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print 'x : {0}, y : {1}'.format(cx,cy)