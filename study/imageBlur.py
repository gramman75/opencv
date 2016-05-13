#-*-coding:utf-8 -*-
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('images/lena.jpg')

# pyplot를 사용하기 위해서 BGR을 RGB로 변환.
b,g,r = cv2.split(img)
img = cv2.merge([r,g,b])

"""
# 일반 Blur
"""
dst1 = cv2.blur(img,(7,7))

"""
# GaussianBlur
 kernel은 양수에 홀수로 지정해야함.
 가우스 함수를 적용한 Blur기법
 가우스 함수란 자기자신과 같거나 작은 정수
 그래서 소수점들은 모두 버려지기 때문에 image가 부드러워짐.
"""
dst2 = cv2.GaussianBlur(img,(5,5),0)
"""
# salt-and-pepper noise제거에 효과적임.
"""
dst3 = cv2.medianBlur(img,9)
"""
# Bilateral Filtering
GaussianBlur의 기능과 edge까지 파악을 하여 Blur처리함.
GaussianBlur와는 다르게 경계선은 유지가 됨.
cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]])
   src : 8-bit, 1 or 3 channel image
   d : filtering시 고려할 주변 pixcel 지름 
   sigmaColor: Color를 고려할 공간. 숫자가 크면 멀리있는 색깔까지도 고려함.
   sigmaSpace : 숫자가 크면 멀리 있는 pixcel도 고려대상이 됨.
"""
dst4 = cv2.bilateralFilter(img,9,75,75)

images = [img,dst1,dst2,dst3,dst4]
titles=['Original','Blur','Gaussian Blur','Median Blur','Bilateral']

for i in xrange(5):
	plt.subplot(3,2,i+1),plt.imshow(images[i]),plt.title(titles[i])
	plt.xticks([]),plt.yticks([])

plt.show()	
