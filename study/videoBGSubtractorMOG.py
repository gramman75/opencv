# -*- coding: utf-8 -*-
"""
# Background Substraction
    . 사람의 이동이나 자동차의 이동을 파악하기 위해서 Background를 제거.
    . 고정된 장소를 촬영하는 CCTV에서 배경을 제거하고 움직이는 물체를 파악하기 위해 배경 제거
    . 특히, 움직이는 그림자도 제거해야 함.
    . cv2.BackgroundSubtractorMOG2
       .
"""
import cv2
import numpy as np

cap = cv2.VideoCapture('images/vtest.avi')

# mog = cv2.createBackgroundSubtractorMOG2()

mog = cv2.createBackgroundSubtractorKNN()

while(1):
    ret, frame = cap.read()
    fgmask = mog.apply(frame)
    k = cv2.waitKey(30) & 0xFF

    cv2.imshow('frame', fgmask)

    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

