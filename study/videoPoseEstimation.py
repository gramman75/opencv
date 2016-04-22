#-*- coding: utf-8 -*-
"""
# 이미지에 3D효과
   . 2차원 이미지에서 3차원을 표현.
   . 2차원 이미지에 X축 Y축 Z축 의 좌표계를 그리고, 이미지가 움지이면  해당 좌표계에 있는 객체도
     동일한 Pose(위치와 방향)움직임
   . Camera Calibration의 값은 왜곡된 이미지를 보정하기도 하지만 3D Pose Estimation에 중요한 자료로 사용됨
   .
"""
import cv2
import numpy as np
import glob

with np.load('calibration.npz') as X:
    ret, mtx, dist, _, _ = [X[i] for i in ('ret','mtx','dist','rvecs','tvecs')]

# def draw(img, corners, imgpts):
#     corner = tuple(corners[0].ravel())
#     img = cv2.line(img, corner, tuple(imgpts[0].ravel()),(255, 0, 0), 5)
#     img = cv2.line(img, corner, tuple(imgpts[1].ravel()),(0, 255, 0), 5)
#     img = cv2.line(img, corner, tuple(imgpts[2].ravel()),(0, 0, 255), 5)
#     return img

def draw(img, corners, imgpts):
    imgpts = np.int32(imgpts).reshape(-1,2)
    # draw ground floor in green
    img = cv2.drawContours(img, [imgpts[:4]],-1,(0,255,0),-3)
    # draw pillars in blue color
    for i,j in zip(range(4),range(4,8)):
        img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(255),3)
        # draw top layer in red color
    img = cv2.drawContours(img, [imgpts[4:]],-1,(0,0,255),3)
    return img
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

c, r = 9, 6

objp = np.zeros((c*r,3), np.float32)
objp[:,:2] = np.mgrid[0:r,0:c].T.reshape(-1,2)

# axis = np.float32([[2,0,0], [0,2,0], [0,0,-2]]).reshape(-1,3)
axis = np.float32([[0,0,0], [0,3,0], [3,3,0], [3,0,0],[0,0,-3],[0,3,-3],[3,3,-3],[3,0,-3] ])

for fname in glob.glob('images/chessboard/frame*.jpg'):
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, (r,c), None)

    if ret == True:
        corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)

        ret, rvecs, tvecs  = cv2.solvePnP(objp, corners2, mtx, dist)
        imgpts, jax = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)

        img = draw(img, corners2, imgpts)
        cv2.imshow('img', img)

        k = cv2.waitKey(0) & 0xFF

        if k == 27:
            break

cv2.destroyAllWindows()





