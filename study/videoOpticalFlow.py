#-*- coding: utf-8 -*-
"""
# Optical Flow
    . 프레임에 대한 사전 정보 없이, 연속된 프레임사이의 움직임을 추정할 수 있는 방법

    . 가정
        1. 연속된 프레임사잉의 대상에 pixel 밀집도는 변화가 없다.
        2. 주변 pixel은 유사한 움직임을 갖는다.
    . 특정시점에서 특정 시간동안 명암의 변화가 거의 없이 얼마만큰 이동했다라는 개념(즉, Pixel의 이동속도 계산)
    . Lucas-Kanade method
        . 한 프레임에서 Pixel윈도우를 설정하고, 다음 윈도우에서 가장 잘 일치하는 곳을 찾음.
        . 대상의 이동이 pixel윈도우를 벗어나는 움직임이 발생하면 계산하지 못함.
        . 이를 개선하기 위해서 Image Pyramid를 활용하여 Scale변화시켜 더 큰 움직임도 계산할 수 있도록 함.
    .  cv2.calcOpticalFlowPyrLK(prevImg, nextImg, prevPts, nextPts, [status, err, windSize, maxLevel,criterial, flags, imiEigThreshold])
        . prevImg – first 8-bit input image or pyramid constructed by buildOpticalFlowPyramid().
        . nextImg – second input image or pyramid of the same size and the same type as prevImg.
        . prevPts – vector of 2D points for which the flow needs to be found;
                     point coordinates must be single-precision floating-point numbers.
        . nextPts – output vector of 2D points (with single-precision floating-point coordinates) containing the calculated new positions of input features in the second image;
                    when OPTFLOW_USE_INITIAL_FLOW flag is passed, the vector must have the same size as in the input.
        . status – output status vector (of unsigned chars);
                   each element of the vector is set to 1 if the flow for the corresponding features has been found, otherwise, it is set to 0.
        . err – output vector of errors; each element of the vector is set to an error for the corresponding feature,
                 type of the error measure can be set in flags parameter;
                 if the flow wasn’t found then the error is not defined (use the status parameter to find such cases).
        . winSize – size of the search window at each pyramid level.
        . maxLevel – 0-based maximal pyramid level number; if set to 0, pyramids are not used (single level), if set to 1, two levels are used, and so on;
                     if pyramids are passed to input then algorithm will use as many levels as pyramids have but no more than maxLevel.
        . criteria – parameter, specifying the termination criteria of the iterative search algorithm
                     (after the specified maximum number of iterations criteria.maxCount or when the search window moves by less than criteria.epsilon.
        . flags –

            OPTFLOW_USE_INITIAL_FLOW uses initial estimations, stored in nextPts; if the flag is not set, then prevPts is copied to nextPts and is considered the initial estimate.
            OPTFLOW_LK_GET_MIN_EIGENVALS use minimum eigen values as an error measure (see minEigThreshold description);
                  if the flag is not set, then L1 distance between patches around the original and a moved point, divided by number of pixels in a window, is used as a error measure.
        . minEigThreshold – the algorithm calculates the minimum eigen value of a 2x2 normal matrix of optical flow equations

"""
import cv2
import numpy as np

cap = cv2.VideoCapture('images/woman.mp4')

if not cap.isOpened():
    print 'Error : Opev Video'
    exit(0)
# Thi-Tomasi Parameter
feature_params = dict( maxCorners = 100,
                      qualityLevel = 0.3,
                      minDistance = 7,
                      blockSize = 7)

#lukas-Kanade parameter
lk_params = dict(winSize = (15,15),
                 maxLevel = 2,
                 criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# np.random.randint(min,max, size)
# size=(100,3) => row=100, col=3인 ndarray생성
color = np.random.randint(0,255,(100,3))

ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

# Shi-Tomasi corner Detect
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

# 주어진 Array와 동일한 zero arry return
# mask는 빈 Array로 이동선을 그리고, 나중에 frame와 add
mask = np.zeros_like(old_frame)

while(1):
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Lukas-Kanade Method
    # p1 : 새로게 이동된 point
    # st : p1의 값이 잘 계산이 되었는지, 1이면 성공, 아니면 실패

    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    # st==1이면, 즉, 연관된 point가 정상적으로 계산이 된 것만, good_new에 할당.
    good_new = p1[st==1]
    good_old = p0[st==1]

    for i,(new,old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        mask = cv2.line(mask,(a,b),(c,d),color[i].tolist(),2)
        frame = cv2.circle(frame,(a,b), 5, color[i].tolist(),-1)

    img = cv2.add(frame, mask)

    # 이미지 반전,  0:상하, 1 : 좌우
    dst = cv2.flip(img,1)
    cv2.imshow('frame', dst)

    k = cv2.waitKey(30) & 0xFF

    if k == ord('q'):
        break

    old_gray = frame_gray.copy()
    # array의 모양 변경. 원본과 원소의 수가 같도록 변경해야 함.
    # -1은 원본과 매칭이 되는 dimension수를 그대로 사용함.
    # 아래의 예는 good_new의 (56,2)를 56,1,2로 변경
    # 56의 수는 변동이 될수 있기에 -1로 하여 원본과 동일하게 유지.
    p0 = good_new.reshape(-1,1,2)

cv2.destroyAllWindows()
cap.release()


ret, frame = cap.read()
cv2.imwrite('vtest.jpg',frame)


while True:
    ret, frame = cap.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if ret == True:

        cv2.imshow('img',frame)

        k = cv2.waitKey(30)

        if (k & 0xFF) == 27:
            break
    else:
        break

cv2.destroyAllWindows()
cap.release()