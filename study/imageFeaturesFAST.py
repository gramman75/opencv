#-*-coding:utf-8-*-
"""
# Features from Accelerated Segment Test(FAST)
    . Edward Rosten and Tom Drummond in their paper “Machine learning for high-speed corner detection” in 2006
    . 속도도 빠르면서 기존 Algorithm보다 더 정확한 결과 추출
    . 작업 방식
        . 특정 Pixel(p)을 중심으로 반지름이 3인원상의 16개의 pixel값을 가지고 판단
        . P보다 일정값 이상 밝은 픽셀이 n개이상 연속되어 있거나 또는 일정값 이상 어두운 픽셀이 n개 이상
          연속되어 있으면 P를 코너점으로 판단
        . n의 개수에 따라서 FAST-9(저자들이 가장 빠르다고 함), FAST-10, FAST-11... FAST-16
        . 코너점파악을 위해서 decision tree방식을 사용하여 빠르게 판단함
        . 문제점은 p가 코너로 인식이 되면 주변 점들도 코너로 인식이 되는 문제가 있음
           . 이를 위해 Non-maximal suppression 후처리를 함.
           . 인접접들이 코너로 인시이 되면 max점만을 남기고 제거하는 방식
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('chessboard.jpg')

fast = cv2.FastFeatureDetector_create(threshold=13,nonmaxSuppression=True, type=cv2.FAST_FEATURE_DETECTOR_TYPE_9_16)

kp = fast.detect(img,None)
cv2.drawKeypoints(img, kp, img, color=(255, 0, 0))


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()