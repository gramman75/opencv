# -*- coding: utf-8 -*-
"""
#K-Nearest Neighbours
    - Supervised Learning. training Data를 바탕으로 학습을 한 후, 새로운 input값을 구분하는 방법중
      가장 간단한 방법
    - 새로운 input에 가장 가까운 class를 찿아 새로운 input을 분류(Classification)
    - K각 1일면 가장 가까운 값. 얼마나 많은 주변 값을 고려할 것인지를 K값으로 결정.
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

trainData = np.random.randint(0,100,(25,2)).astype(np.float32)

response = np.random.randint(0,2,(25,1)).astype(np.float32)

red = trainData[response.ravel() == 0]
plt.scatter(red[:,0],red[:,1], 80,'r','^')

blue = trainData[response.ravel() == 1]
plt.scatter(blue[:,0], blue[:,1], 80, 'b', 's')

newcomer = np.random.randint(0,100,(10,2)).astype(np.float32)
plt.scatter(newcomer[:,0], newcomer[:,1],80,'g', 'o')

knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, response)
ret, results, neighbours, dist = knn.findNearest(newcomer, 3)

print "result : ", results
print "neighbours :", neighbours
print "distance: ", dist

plt.show()