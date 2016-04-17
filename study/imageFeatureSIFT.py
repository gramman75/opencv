#-*-coding:utf-8-*-
"""
# Scale-Invariant Feature Transform
    . Harris 방법이 Scale변환에 민감한 문제를 해결하기 위한 algorith
    . 작업순서
        . Scale을 계속 변경한 집합생성(Image Pyramid)
        . 해당 집합에서 코너점을 찾고, 각 이미지 마다의 동일한 코너점이 발견이 되면,
          그 코너점이 스케일이 불변이 코너점이 됨.
        . 각 이미지에서 코너점을 찾기 위해서 Harris방법이 아닌 Laplacian of Gaussian(LoG)를 사용하는데,
          속도문제로 인하여 Difference of Gaussian(DoG)방법을 사용함.
          DoG는 Scale을 변화시키는 것이 아니고 blurring을 하여 LoG와 거의 동일한 결과를 추출해 냄.
"""
import cv2
import numpy as np
img = cv2.imread('chessboard.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift =cv2.FastFeatureDetector_create()

kp = sift.detect(gray,None)

img = cv2.drawKeypoints(gray,kp)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()