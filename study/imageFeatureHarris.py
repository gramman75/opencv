#-*-coding:utf-8-*-
"""
# Feature
   . 물체를 식별할 수 있는 특징
   . 일반적으로 반복되는 부분인, 경계선은 Feature가 될수 없음.(그것만 가지고 형태 파악이 되지 않기 때문)
   . 경계점을 파악하면 물체의 전체적인 형태 파악이 가능함.
# Feature Detection
   . 물체의 경계점을 찾는 작업
# Feature Description
   . 물체가 무엇인지 설명하는 작업

# Harris Coner Detection
   . 코너의 특징은 이미지에서 작은 윈도우를 조금씩 움직였을 때 영상의 변화가 모든 방향으로 큼.
   . 이미지의 변화량이 작은면 flat한 영역(2개의 값이 결과로 나옴), 하나는 크고 하나는 작으면 경계선, 모두 크면 Corner
   . 영상의 평행이동, 회전변화에는 영향이 없고, affine변화, 조명변화에도 강정이 있으나 Scale변화에는 별도 작업이 필요.
   . cv2.cornerHarris(img, blockSize, ksize, k)
      . img : input image,grayscale, float32 type
      . blockSize : corner detection을 위해 고려해야 하는 주변값. 값이 커질 수록 많은 코너를 찾음(그만큼 실수도 많아짐)
      . ksize : Sobel 변환시 사용할 aperture size
      . k : Harris dector free parameter in the equstion.
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dave.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

img[dst>0.01*dst.max()] = [255,0,0]

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
