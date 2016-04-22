# -*- coding: utf-8 -*-
"""
# Camera Calibration
      . 3D 공간좌표를 2D 영상 좌표로 변환하는 관계를 찾는 과정
      . 즉, 각 카메라마다 3D 현실을 2D 영상으로 표현하면서 생기는 왜곡을 보정하는 방법
      . 왜곡의 종류
         . radial distortion : 직선이 곡선으로 왜곡.
         . tangential distortion : 렌즈가 포착한 이미지가 카메라의 이미지 센서와 평행하지 못해서 발생하는 왜곡.
      . 왜곡 보정을 위해서는 영향을 주는 파라미터가 파악이 되어야 함.
      . 내부 파라미터
          . 초점거리, 주점, 비대칭 계수가 있음. 카메라 고유의 내부 파라미터
      . 외부 파라미터
          . 영상촬영시의 위치나 방향에 따라 달라짐.
          . 내부 파라미터를 구한 후, Sample영상을 이용하여 변환행렬을 구함.
      . Camera Calibration을 위해서는 사용하는 카메라로 촬영한, 패턴이 명확한 여러장의 chessboard 이미지를 이용하여 왜곡 계수를 구함.
"""
import cv2
import numpy as np
import glob

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
c = 9 # column
r = 6 # row
objp = np.zeros((c*r,3), np.float32)
objp[:,:2] = np.mgrid[0:r,0:c].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
images = glob.glob('images/chessboard/frame*.jpg') # 여러장의 이미지로 테스트
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (r,c))

# If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)
        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (r,c), corners2,ret)
        cv2.imshow('img',img)
        cv2.waitKey(500)

"""
 - mtx : 3x3 float camera matrix(내부 파라미터. 초점거리(1,1;2,2)와 주점(1,3;2,3))
 - dist : 왜곡 계수(distortion coefficients)
 - rvecs : rotation vector
 - tvecs : translation vector
"""
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
np.savez('calibration.npz', ret=ret, mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs)
img = cv2.imread('images/chessboard/frame01.jpg')
h, w = img.shape[:2]
"""
 - newcameramtx : free sacale 기반의 camera matrix return
 - roi : all-good-pixcel outlines rectangle

"""
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h),1,(w,h))

# 왜곡 보정
dst = cv2.undistort(img, mtx, dist, newcameramtx)

# x,y, w, h = roi
# cv2.imshow('dst',dst[y:y+h, x:x+w])
cv2.imshow('dst',dst)
cv2.waitKey(0)

cv2.destroyAllWindows()

