# -*- coding: utf-8 -*-
"""
# Dense Opticla Flow
    . Lucas-Kanade 방식은 frame의 특정 부분(ex; 코너점)에 대해서 계산함.
    . Dense Optical Flow는 Frame의 모든 점에 대해서 계산을 함.
    . "Two-Frame Motion Estimation Based on Polynomial Expanseion" by Gunner Farneback in 2003
    . 2개의 Channerl(Hue, Value)를 사용함.
    . Hue는 이미지의 방향, Value는 명암의 크기를 계산하는데 사용 됨.
    . cv2.calcOpticalFlowPyrLK(prev, next, flow, pyr_scale, levels, winsize, iterations, poly_n, poly_sigma, flags) → flow
         - prev : 8bit image
         - next : prev와 동일한 사이즈의 이미지
         - flow : prev와 동일한 사이즈이고 CV_32FC2 type의 flow image
         - pyr_scale : image sacle(<1). 0.5이면 pyramid에서 이전보다 2배 작은 pyramid. scale을 작게해서 넓은 부분도 계산(?)
         - levels : pyramid layer의 수,0이면 원본 이미지만 사용함.
         - winsize: 값이 크면 이미지의 노이즈가 증가하지만, 빠른 모션도 처리할 확율이 높아짐.
         - iterations : 각 Pyramid 마다 algorithm을 반복할 횟수
         - poly_n : polynomial expansion(여러방향으로의 확장?)을 발견하기위해서 사용하는 주변 픽셀
                    값이 크면 표면이 부드러워지고, 모션이  blurred됨.
         - poly_sigma : Gaussian의 평균분포.  for poly_n=5, you can set poly_sigma=1.1, for poly_n=7, a good value would be poly_sigma=1.5
         - flgs : OPTFLOW_USE_INITIAL_FLOW , OPTFLOW_FARNEBACK_GAUSSIAN

"""
import cv2
import numpy as np

cap = cv2.VideoCapture('images/vtest.avi')
ret, frame1 = cap.read()
prvs = cv2.cvtColor( frame1, cv2.COLOR_BGR2GRAY )
hsv = np.zeros_like(frame1)
hsv[..., 1] =255 # Dense Optical Flow에서는 S(채도)는 사용하지 않기 때문에 특정 값으로 일괄 변경

while (1):
    ret, frame2 = cap.read()
    next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(prev = prvs, next= next, flow= None, pyr_scale=0.5, levels= 3, winsize= 15,\
                                        iterations=3, poly_n=5,poly_sigma=1.2, flags=0 )

    # mag : magnitute
    # ang : 호도법(radian값). HSV에서 H(Hue)값은 각도로 표현이 됨. rdian값에 180/pi를 하면 육십분법으로 표현됨.
    # cartToPolar : 2D Vector의 mangitute와 angle 계산
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])

    # hsv값에서 첫번째 Channel(Hue)값을 변경
    hsv[..., 0] = ang*180/np.pi/2

    # hsv에서 세번째(Value)값을 변경. 0~255 사이로 Min Max정규화.Value(0~255)
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)

    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow('frame2', rgb)

    k = cv2.waitKey(30) & 0xFF

    if k == 27:
        break;
    elif k == ord('s'):
        cv2.imwrite('opticalfg.png', frame2)
        cv2.imwrite('opticlahsv.png', rgb)

    prvs = next

cap.release()
cv2.destroyAllWindows()


