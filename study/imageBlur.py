#-*-coding:utf-8 -*-
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('copy.png')

# filter2D에 (5,5) kernel적용과 동일로 추정.
dst = cv2.blur(img,(5,5))

# kernel은 양수에 홀수로 지정해야함.
# 가우스 함수를 적용한 Blur기법
# 가우스 함수란 자기자신과 같거나 작은 정수
# 그래서 소수점들은 모두 버려지기 때문에 image가 부드러워짐.
dst2 = cv2.GaussianBlur(img,(21,21),0)

# salt-and-pepper noise제거에 효과적임.
dst3 = cv2.medianBlur(img,5)

# plt.subplot(121),plt.title('Original'),plt.imshow(img)
# plt.xticks([]),plt.yticks([])

plt.subplot(121),plt.title('Blur'),plt.imshow(dst)
plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.title('GaussianBlur'),plt.imshow(dst2)
plt.xticks([]),plt.yticks([])

plt.show()