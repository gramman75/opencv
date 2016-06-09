#-*- coding:utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/UK.jpg')
img1 = img.copy()

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,125,255,0)

image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[14] # 14번째가 지도의 contour line

# 끝점 좌표 찾기
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

# 좌표 표시하기
cv2.circle(img1,leftmost,20,(0,0,255),-1)
cv2.circle(img1,rightmost,20,(0,0,255),-1)
cv2.circle(img1,topmost,20,(0,0,255),-1)
cv2.circle(img1,bottommost,20,(0,0,255),-1)

img1 = cv2.drawContours(img1, cnt, -1, (255,0,0), 5)

titles = ['Original','Result']
images = [img, img1]

for i in xrange(2):
    plt.subplot(1,2,i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()