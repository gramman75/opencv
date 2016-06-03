#-*- coding:utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/UK.jpg')
img1 = img.copy()

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,10,255,0)

image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[1]

img1 = cv2.drawContours(img1, contours, -1, (0,0,0), 3)
#
# # Straight Rectangle
# x, y, w, h = cv2.boundingRect(cnt)
# img1 = cv2.rectangle(img1,(x,y),(x+w, y+h),(0,255,0), 3) # green
#
# # Rotated Rectangle
# rect = cv2.minAreaRect(cnt)
# box = cv2.boxPoints(rect)
# box = np.int0(box)
# img1 = cv2.drawContours(img1, [box], 0, (0,0,255), 3) # blue
#
# # Minimum Enclosing Circle
# (x,y), radius = cv2.minEnclosingCircle(cnt)
# center = (int(x), int(y))
# radius = int(radius)
# img1 = cv2.circle(img1, center, radius,(255,255,0),3) # yellow
#
# # Fitting an Ellipse
# ellipse = cv2.fitEllipse(cnt)
# img1 = cv2.ellipse(img1, ellipse,(255,0,0),3) #red

titles = ['Original','Result']
images = [img, img1]

for i in xrange(2):
    plt.subplot(1,2,i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()