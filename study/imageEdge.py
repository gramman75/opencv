#-*- coding:utf-8 -*-

"""
# Sobel Filter
    . x축과 y축의 미분하여 경계값을 계산
    . x축 미분은 수평선, y축 미분은 수직선을 미분함
    . 미분하는 축의 선이 사라지는 효과
    . 미분시 소실되는 표본의 정보가 많을 수 있어, aperture_size로 조절
# Scharr filter
    . Sobel Filter에 적용되는 aperture_Size 값
    . 이 필터값을 사용하면 Sobel에서 손실된 정보를 보정하는 효과가 있음.
# Laplacian 함수
    . 이미지의 가로와 세로에 대한 Gradient를 2차 미분한 값
    . Sobel 필드에 미분의 정도가 더해진 것과 비슷
    . blob(주위 픽셀과 확연한 픽셀차이를 나타내는 덩어리)검출에 많이 사용
# Canny Edge Detection
    . 가장 유명한 Edge Detction방법
    . 여러단계의 Algorithm을 통하여 Edge Detection
    . 1. Noise Reduction
        . 5X5의 Kenel을 이용한 Gaussian Filter적용
    . 2. Edge Gradient Detection
        . Gradient의 방향과 강도를  확인.
        . 경계에서는 미분값이 급속히 변함.
    . 3. Non-maximum Suppression
        . Image Pixel을 Full Scan하여 Edge가 아닌 Pixel은 제거
    . 4. Hysteresis Threshoding
        . 지금까지 Edge로 판단된 Pixel이 진짜 Edge인지 판별하는 작업
        . maxVal와 minVal(임계값)을 설정하여 maxVal 이상은 강한 Edge 
          minVal과 maxVal사이는 약한 Edge로 설정함.
        . 이제 약한 Edge가 진짜 Edge인지 확인하기 위해서 강한 Edge와 연결이 되어 
          있으면 Edge로 판단하고, 그러지 않으면 제거함.

"""
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('images/lena.jpg')
canny = cv2.Canny(img,30,70)
gaussian = cv2.GaussianBlur(img,(5,5),0)
gray = cv2.cvtColor(gaussian,cv2.COLOR_BGR2GRAY)
# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

laplacian = cv2.Laplacian(gray,cv2.CV_64F)
sobelx = cv2.Sobel(gaussian,cv2.CV_8U,1,0,ksize=3)
sobely = cv2.Sobel(gaussian,cv2.CV_8U,0,1,ksize=3)

images = [gaussian,laplacian, sobelx, sobely, canny]
titles = ['Origianl', 'Laplacian', 'Sobel X', 'Sobel Y','Canny']

for i in xrange(5):
	plt.subplot(2,3,i+1),plt.imshow(images[i]),plt.title([titles[i]])
	plt.xticks([]),plt.yticks([])

plt.show()