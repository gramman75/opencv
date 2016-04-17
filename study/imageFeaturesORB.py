#-*- coding:utf-8-*-
"""
# Oriented FAST and Rotated BRIEF)
    . 특허권이 있는 SIFT와 SURF를 대체할 수 있도록 Open CV Lab에서 개발
    . FAST + BRIEF를 조합한 형태
    . Point에는 FAST algorithm, descrptor를 위해서는 수정된 BRIEF Descriptor적용 .
    . 작업순서
        . Key Point를 찾기 위해 FAST적용
        . 찾은 Key Point에서 최상위 N개 추출을 위해 Harris 검출 방법 적용
        . Multi-Scales 처리를 위한 Image Pyramid 사용
        . BRIEF Descritpor적용
    . cv2.ORB_create(nfeatures, scaleFator, nlevels, edgeThreshold, firstLevel, WTA_K, scoreType, patchSize)
        . nfeatures :
"""
import cv2
import numpy as np

img = cv2.imread('chessboard.jpg')

orb = cv2.ORB_create()
kp = orb.detect(img)

# kp, des = orb.detectAndCompute(img, None)

cv2.drawKeypoints(img, kp, img, color=(255,0,5))
cv2.imshow('ORB', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

