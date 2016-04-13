#-*- coding:utf-8 -*-

"""
# Fourier Transform(푸리에 변환)
    . 시간 도메인(X축)에서 표현된 신호(일반적인 파형 도표)를 주파수 도메인으로 변환.
    . 시간축이 제거되어 대상의 전체적인 특징을 파악할 수 있음.
    . 이미지에 적용이 되어 중심이 저주파 영역, 주변이 고주파 영역을 나타냄.
    . 푸리에 변환을 하여 저주파 또는 고주파를 제거하고 다시 역으로 이미지로 변환 함으로써 
      이미지가공을 할 수 있음.
      (ex; 푸리에 변환 후 중심의 저주파를 제거하고 다시 Image로 전환 하면 이미지의 경계선만 남게 됨.
      	   푸리에 변환 후 주변의 고주파를 제거하면 모아레 패턴(휴대폰으로 모니터를 찍었을 때 나타나는 현상)
      	   을 제거할 수 있음.(모니터의 고주파를 제거함.) 
      )
"""

import cv2
import numpy as np 
from matplotlib import pyplot as plt 


img = cv2.imread('lena.jpg')
b,g,r = cv2.split(img)
img = cv2.merge([r,g,b])
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
"""
# Fourier Transform을 적용.
 적용을 하면 0,0, 즉 화면 좌측상단점이 중심이고, 거기에 저자파가 모여 있음.
 하지만 그양이 작아서 그래도 이미지를 보면 전체가 검은 색으로 보임.
 분석을 용이하게 하기 위해 0,0을 이미지의 중심으로 이동 시키고 Log Scaling을 하여 분석이 용이한 결과값으로 변환 
"""
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))


rows, cols = img.shape
crow, ccol = rows/2, cols/2

d = 10

fshift[crow-d:crow+d, ccol-d:ccol+d] = 1
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)


img_back = np.abs(img_back)
img_new = np.uint8(img_back); #img_new = np.array(img_back,dtype='uint8') #float64가 threshold가 적용되지 않아 uint8 or float32로 변환  

ret, thresh = cv2.threshold(img_new,30,255,cv2.THRESH_BINARY_INV)


plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(222),plt.imshow(img_back, cmap = 'gray')
plt.title('FT'), plt.xticks([]), plt.yticks([])

plt.subplot(223),plt.imshow(thresh, cmap = 'gray')
plt.title('Threshold With FT'), plt.xticks([]), plt.yticks([])
plt.show()