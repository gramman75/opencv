# -*- coding:utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gradient.jpg')
res1 = cv2.resize(img, None,fx=2, fy=2, interpolation = cv2.INTER_LINEAR)
height, width = img.shape[:2]

res2 = cv2.resize(img,(2*width,2*height),interpolation = cv2.INTER_CUBIC)

cv2.imshow('img',img)
cv2.imshow('res1',res1)
cv2.imshow('res2',res2)

cv2.waitKey(0)
cv2.destroyAllWindows()


#py plot를 사용하면 Scaling결과를 확인할 수 없음.
# images = [img, res1, res2]
# titles = ['a','b','c']

# for i in xrange(3):
# 	plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
# 	plt.title(titles[i])
# 	plt.xticks([])
# 	plt.yticks([])
# plt.show()


