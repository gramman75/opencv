#-*- coding: utf-8 - *-
"""
====================================
 :mod:`mod2` 모듈2
====================================
.. moduleauthor:: 홍길동 <gdhong@foo.org>
.. note:: Future's NDA License

"""
import cv2      # OpenCV Import
from matplotlib import pyplot as plt #plot Import

fname = 'lena.jpg'  # 이미지 파일경로

color1 = cv2.imread(fname, cv2.IMREAD_COLOR) # 원본 이미지
gray = cv2.imread(fname, cv2.IMREAD_GRAYSCALE) # Grayscale 이미지
alpha = cv2.imread(fname, cv2.IMREAD_UNCHANGED) # alpha Chanell포함 이미지

# 각 이미지별 Show
cv2.imshow('Original',color1)
cv2.imshow('Gray',gray)
cv2.imshow('alpha', alpha)


b, g, r = cv2.split(color1)
color2 = cv2.merge((r,g,b))

titles = ['Origianl', 'RGB']
images = [color1, color2]

for i in xrange(2):
    plt.subplot(1,2,i+1),plt.title(titles[i]),plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

