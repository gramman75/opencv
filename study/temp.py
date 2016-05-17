#-*- coding:utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

dotImage = cv2.imread('images/dot_image.png')
holeImage = cv2.imread('images/hole_image.png')
orig = cv2.imread('images/morph_origin.png')


kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

erosion = cv2.erode(dotImage,kernel,iterations = 1)
dilation = cv2.dilate(holeImage,kernel,iterations = 1)

opening = cv2.morphologyEx(dotImage, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(holeImage, cv2.MORPH_CLOSE,kernel)
gradient = cv2.morphologyEx(orig, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(orig, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(orig, cv2.MORPH_BLACKHAT, kernel)

images =[dotImage, erosion, opening, holeImage, dilation, closing, gradient, tophat, blackhat]
titles =['Dot Image','Erosion','Opening','Hole Image', 'Dilation','Closing', 'Gradient', 'Tophat','Blackhot']

for i in xrange(9):
	plt.subplot(3,3,i+1),plt.imshow(images[i]),plt.title(titles[i])
	plt.xticks([]),plt.yticks([])

plt.show()