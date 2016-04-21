#-*-coding:utf-8-*-
import cv2
import numpy as np 
from matplotlib import pyplot as plt 
"""
# Contours
    . Object의 외형의 파악하고 인식하는데 사용됨.
    . 정확도를 위해서 Binary Image를 사용함. 적용전 threshold나 canny edge적용
    . findContours를 사용하면 원본이미지가 수정이됨.
    . Object는 White로 , 배경은 Black으로 표현됨.
    . findContours(image, retrieval mode, approximation method)
        . approximation method : 외곽선을 찾아 저장하는 방법

    . drawContours(image, contours,, index, color, thickness)
        . image: 원본이미지
        . contours : 외곽선 List
        . index : contours의 index(-1이면 외곽선을 그림)
"""

img = cv2.imread('images/imageHierarchy.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,127,255,0) #binary Image
image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
print len(contours)
cnt = contours[1]

# epsilon = 0.1*cv2.arcLength(cnt,True)
# approx = cv2.approxPolyDP(cnt,epsilon,True)
x,y,w,h = cv2.boundingRect(cnt)
straightRect = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4)

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img = cv2.drawContours(img,[box],0,(0,0,255),2)
dst = cv2.drawContours(img, contours,1,(0,255,0),3)

plt.subplot(121), plt.imshow(img),plt.xticks([]),plt.yticks([])
plt.show()

# cv2.imshow('img',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()