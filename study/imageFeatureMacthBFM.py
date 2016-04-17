#-*- coding: utf-8 -*-
"""
# Brute-Forece Matcher(BFMatcher)
    . 첫번째 Set의 Feature의 Descriptor를 이용하여 두번째 Set에서 Distance calculation을 이용하여
      Match되는 Feature를 Return.
    . cv2.BFMatcher(normType, crossCheck)
        . normType : 거리측정시 사용되는 option.cv2.NORM_L2
        . crossCheck : true면 Set A와 Set B에서 서로 match가되는 (i,j)를 retur함
        . cv2.BFMacher.match()
            . best match를 return
        . cv2.BFMacher.knnMatch()
            . 사용자가 k값을 지정하여 결과를 조정할 수 있음
        . cv2.drawMatches()
        . cv2.drawMatchesKnn()
    . opencv 3.x버전의 버그
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('images/box.png',0)
img2 = cv2.imread('images/box_in_scene.png',0)
img3 = img1.copy()

orb = cv2.ORB_create()

kp1 = orb.detect(img1, None)
kp1, des1 = orb.compute(img1, kp1)

kp2 = orb.detect(img2, None)
kp2, des2 = orb.compute(img2, kp2)
# kp1, des1 = orb.detectAndCompute(img1, None)
# kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

matches = sorted(matches, key = lambda x:x.distance)

cv2.drawMatches(img1,kp1,img2,kp2, matches[:10],outImg=img3, flags=2)

plt.imshow(img3),plt.show()


