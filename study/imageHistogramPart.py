#-*- coding: utf-8-*-
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('hist_norm.jpg')
b,g,r = cv2.split(img)
img = cv2.merge([r,g,b])

mask_top = np.zeros(img.shape[:2],np.uint8)
mask_top[0:100,0:258] = 255 #[시작X:끝X, 시작Y, 끝Y]

mask_middle = np.zeros(img.shape[:2],np.uint8)
mask_middle[100:310, 0:258] = 255

mask_bottom = np.zeros(img.shape[:2],np.uint8)
mask_bottom[310:344,0:258] = 255

masked_top = cv2.bitwise_and(img,img,mask=mask_top)
masked_middle= cv2.bitwise_and(img,img,mask=mask_middle)
masked_bottom= cv2.bitwise_and(img,img,mask=mask_bottom)

masked_top_hist = cv2.calcHist([img],[0],mask_top,[256],[0,256])
masked_middle_hist = cv2.calcHist([img],[0],mask_middle,[256],[0,256])
masked_bottom_hist = cv2.calcHist([img],[0],mask_bottom,[256],[0,256])


images = [img,mask_top,masked_top, masked_top_hist, img,mask_middle, masked_middle, masked_middle_hist,img,mask_bottom, masked_bottom, masked_bottom_hist]
titles = ['Origian', 'Top Mask', 'Top Masked', 'Top Histogram','Origian', 'Middle Mask', 'Middle Masked', 'Middle Histogram','Origian', 'Bottom Mask', 'Bottom Masked', 'Bottom Histogram']

for i in xrange(12):
	plt.subplot(3,4,i+1),plt.title(titles[i])
	if ((i+1)%4) == 0:
		plt.plot(images[i])
	else:
	plt.imshow(images[i])


plt.show()
