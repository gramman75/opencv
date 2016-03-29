# -*- coding:utf-8 -*-
import cv2 
import numpy as np 

img = np.zeros((512,512,3), np.uint8)

img = cv2.line(img,(0,0),(511,511),(2550,0,0), 5)

img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# 1: 대상 이미지 
# 2: 중심점
# 3: 중심점에서 가로 
# 4: 중심점에서 세로 
# 5: 시작점 
# 6: 종점 ???
# 7: 회전 각 
# 8: 선두께(-1이면 채우기)
img = cv2.ellipse(img,(256,256),(180,180),50,10,200,100,30)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img,'Open CV',(10,500),font,4,(255,255,255),2,cv2.LINE_AA)


cv2.imshow('image', img)
cv2.waitKey(0)
