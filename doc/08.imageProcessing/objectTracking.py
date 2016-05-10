#-*- coding: utf-8 -*-
import cv2
import numpy as np

# Camera 객체를 생성 후 사이즈르 320 X 240 으로 조정.
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

while(1):
    # camera에서 frame capture.
    ret, frame = cap.read()

    if ret:

        # BGR->HSV로 변환
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # blue 영역의 from ~ to
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])

        #이미지에서 blue영역
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        #bit연산자를 통해서 blue영역만 남김.
        res = cv2.bitwise_and(frame, frame, mask = mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()