#-*- coding:utf-8 -*-
import cv2
import numpy as np
import random
from matplotlib import pyplot as plt

img = cv2.imread('images/imageHierarchy.png')

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,125,255,0)

image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)


for i in xrange(len(contours)):
    #각 Contour Line을 구분하기 위해서 Color Random생성
    b = random.randrange(1,255)
    g = random.randrange(1,255)
    r = random.randrange(1,255)

    cnt = contours[i]
    img = cv2.drawContours(img, [cnt], -1,(b,g,r), 2)

titles = ['Result']
images = [img]

for i in xrange(1):
    plt.subplot(1,1,i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()