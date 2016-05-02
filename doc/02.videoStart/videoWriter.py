# -*-coding: utf-8 -*-

import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.ViewoWriter('output.avi', fourcc, 25.0, (640,480))

while (cap.isOpend()):
    ret, frame = cap.read()

    if ret:
        # 이미지 반전,  0:상하, 1 : 좌우
        frame = cv2.flip(frame, 0)

        out.write(frame)

        cv2.imshow('frame', frame)

        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()