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
with np.load('calibration.npz') as X:
    ret, mtx, dist, _, _ = [X[i] for i in ('ret','mtx','dist','rvecs','tvecs')]



