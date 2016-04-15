#-*-coding:utf-8-*-
"""
# Shi-Tomasi Corner Detector
    . Harris Corner Detector를 수정한 방식
    . 계산된 2개의 결과값이 threshold보다 크면 corner로 고려.
    . 2개의 값중 작은 값이 threshold보타 크면 corner.
    . 추적에 용이한 corner찾기방식임.
    . cv2.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance[, corners[, mask[, blockSize[, useHarrisDetector[, k]]]]]) → corners
        - image : Input 8-bit or floating-point 32-bit, single-channel image.
        - maxCorner : corner을 내림차순 정렬한 후 가장 큰 값부터 return할 갯수
        - qulityLevel : quality측정 기준. 0 ~ 1사이
        - minDistance : corner들 사이의 최소 거리
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('chessboard.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,10,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),10,255,-1)

plt.imshow(img),plt.show()