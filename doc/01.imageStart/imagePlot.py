#-*- coding:utf-8 -*-
import cv2
from matplotlib import pyplot as plt # as는 alias 적용시 사용

img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)

plt.imshow(img)
plt.xticks([]) # x축 눈금
plt.yticks([]) # y축 눈금
plt.show()
