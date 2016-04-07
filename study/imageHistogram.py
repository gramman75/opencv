#-*-coding:utf-8-*-
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

"""
# Histogram
    . 이미지의 강도에 대한 분포
    . 강도는 빛의세기, Channel의 분포 등이 될수 있음.
    . 챠트를 보면서 이미지의 대략적인 특징을 파악할 수 있음.

    calcHist(images, channels, mask, histSize, ranges)
        . images : 분석 대상 이미지의 Array형태
        . channels : 분석 Channels(X축의 대상) 0: grayscale, 1:blue, 2:green, 3: red ex;[0], [0,1]
        . mask : 이미지의 분석 영역 , None이면 전체, 
        . histSize: BIN count, x축의 간격 
        . ranges: x축의 from ~ to
"""

img = cv2.imread('lena.png')

# color = ('b','g','r')
# for i, col in enumerate(color):
# 	hist = cv2.calcHist([img],[i],None,[256],[0,256])
# 	plt.plot(hist, color = col)
# 	plt.xlim([0,256])

"""
Histogram에 Mask적용 
"""


mask = np.zeros(img.shape[:2],np.uint8)
mask[100:300,100:400] = 255
masked_img = cv2.bitwise_and(img,img,mask=mask)

hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221),plt.imshow(img,'gray')
plt.subplot(222),plt.imshow(mask,'gray')
plt.subplot(223),plt.imshow(masked_img,'gray')
plt.subplot(224),plt.plot(hist_full,color='r'),plt.plot(hist_mask,color='b')
plt.xlim([0,256])


plt.show()