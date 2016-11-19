# -*-coding:utf-8-*-
"""
    . harris corner로 찾은 결과를 이용함.
# cv2.cornerSubPix
    . 가장 정확한 코너를 찾을 때 사용.
    . cv2.cornerSubPix(image, corners, winSize, zeroZone, criteria)
        . image : Input image
        . corners:  정제가 필요한 Corner data. harris corner의 결과 이용
        . winSize : 정제 작업시 사용할 window size
        . zeroZone : 일치정도를 파악하는 matrix에서 특이한 점을 피하기 위함.(-1,-1)은 무시?
        . criteria : 정확한 Data를 찾기위해 반복해야 하는 회수(maxCount나 특정 지점을 벗어나면 멈춤)
            - type of termination criteria : It has 3 flags as below:
            - cv2.TERM_CRITERIA_EPS - stop the algorithm iteration if specified accuracy, epsilon, is reached.
            - cv2.TERM_CRITERIA_MAX_ITER - stop the algorithm after the specified number of iterations, max_iter.
            - cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER - stop the iteration when any of the above condition is met.
            3.b - max_iter - An integer specifying maximum number of iterations.
            3.c - epsilon - Required accuracy
"""

import cv2
import numpy as np

img = cv2.imread('images\chessboard.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 9, 3, 0.04)
# dst = cv2.dilate(dst, None)
ret, dst = cv2.threshold(dst, 0.02 * dst.max(), 255, 0)
dst = np.uint8(dst)

ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)

res = np.hstack((centroids, corners))
res = np.int0(res)

for i in res:
    img = cv2.circle(img, (i[0], i[1]), 3, (0, 0, 255), 3)
    img = cv2.circle(img, (i[2], i[3]), 3, (0, 255, 0), 3)
# img[res[:, 1], res[:, 0]] = [0, 0, 255]
# img[res[:, 3], res[:, 2]] = [0, 255, 0]

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
