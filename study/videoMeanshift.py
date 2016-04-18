#-*- coding: utf-8 -*-
"""
# Meanshift
    . 영상에서 물체의 이동을 추적
    . 대상이 되는 이미지(set of point)가 있고, 그것을 포함하는 window가 주어지면
      window는 주변에서 가장 point 밀도가 높은쪽으로 window를 이동
    . 추적하는 대상과 배경이 유사하면 실패할 확률이 높아 고정된 환경(공장 자동화)에서 활용
    . Histogram분석시 빛의 영향을 덜 받는 Hue값을 사용함.
    . cv2.meanShif
"""
import numpy as np
import cv2

cap = cv2.VideoCapture('images/vtest.avi')

# video로 부터 첫번째 frame 얻기
ret, frame = cap.read()

# 임의의 window 생성
# r,h,c,w =342,103,698,70
r,h,c,w =150,103,500,70
track_window = (c,r,w,h)

# img3 = cv2.rectangle(frame, (c, r), (c + w, r + h), 255, 2)
# cv2.imwrite('temp.jpg',img3)

# Tracking을 위한 Region of Image(ROI)생성
roi = frame[r:r+h, c:c+w]
hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# 어두운 영역을 제거하기 위해서 inRange함수 사용
mask = cv2.inRange(hsv_roi, np.array((0.,60.,32.)), np.array((180.,255.,255.)))

# ROI영역에 대한 Histogram생성 후 정규화. 대상 Search를 위함
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

# meanShift반복 횟수. 10번 반복하거나 1pt이동시까지 반복
term_crit = (cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT, 10, 1)
while(1):
    ret, frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 새로운 Frame에서 ROI Histogram을 적용하여 대상 찾기
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

        # 새로운 위치를 얻기 위해서 meanshift적용
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)

        # 새로운 Frame에 새로운 사각형 그리기
        x,y,w,h = track_window
        img2 = cv2.rectangle(frame,(x,y), (x+w,y+h), 255,2)
        cv2.imshow('img2',img2)

        k = cv2.waitKey(60) & 0xFF
        if k == 27:
            break
        else:
            cv2.imwrite(chr(k) + ".jpg",img2)
    else:
        break

cv2.destroyAllWindows()
cap.release()