#-*-coding:utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/lena.jpg')

# pyplot를 사용하기 위해서 BGR을 RGB로 변환.
b,g,r = cv2.split(img)
img = cv2.merge([r,g,b])


# 일반 Blur
dst1 = cv2.blur(img,(7,7))

# GaussianBlur
dst2 = cv2.GaussianBlur(img,(5,5),0)

# Median Blur
dst3 = cv2.medianBlur(img,9)

# Bilateral Filtering
dst4 = cv2.bilateralFilter(img,9,75,75)

images = [img,dst1,dst2,dst3,dst4]
titles=['Original','Blur(7X7)','Gaussian Blur(5X5)','Median Blur','Bilateral']

for i in xrange(5):
	plt.subplot(3,2,i+1),plt.imshow(images[i]),plt.title(titles[i])
	plt.xticks([]),plt.yticks([])

plt.show()
