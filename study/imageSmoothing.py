#-*- coding:utf-8 -*-
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('copy.png')

# 1행렬을 만들어서 행렬 원소로 갯수 나눈 Kernel matrix을 
# filter2D를 이용하여 적용
# 모든 pixel에 동일한 효과 적

kernel = np.ones((5,5),np.float32)/25

dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]),plt.yticks([])

plt.show()
