.. imageContourFeature

===============
Contour Feature
===============

Goal
====
    * Contours의 특징(영역, 중심점, bounding box 등)을 찾을 수 있습니다.
    * Contours 특징을 찾는 다양한 함수에 대해서 알 수 있습니다.

Moments
=======

Image Moment는 대상을 구분할 수 있는 특징을 의미합니다.. 특징으로는 Area, Perimeter, 중심점 등이 있습니다.
Image Moments는 대상을 구분한 후, 다른 대상과 구분하기 위해 대상을 설명(describe)하는 자료로 사용됩니다.

.. code-block:: python
    :linenos:

    #-*- coding:utf-8 -*-
    import cv2
    import numpy as np

    img = cv2.imread('images/rectangle.jpg')
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray,127,255,0)

    image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # 첫번째 contours의 moment 특징 추출
    cnt = contours[0]
    M = cv2.moments(cnt)

    print M.items()

>>> [('mu02', 35950058.66666663), ('mu03', 1.52587890625e-05), ('m11', 884446080.0), ('nu02', 0.03873697916666662), ('m12', 113614624853.33333), ('mu21', 1.9073486328125e-05), ('mu20', 166374058.6666665), ('nu20', 0.17927170868347322), ('m30', 570292325120.0), ('nu21', 1.1775050154231546e-16), ('mu11', 0.0), ('mu12', 3.814697265625e-06), ('nu11', 0.0), ('nu12', 2.3550100308463093e-17), ('m02', 463733162.6666666), ('m03', 63472543680.0), ('m00', 30464.0), ('m01', 3609984.0), ('mu30', 0.0001220703125), ('nu30', 7.53603209870819e-16), ('nu03', 9.420040123385237e-17), ('m10', 7463680.0), ('m20', 1994975658.6666665), ('m21', 236404615552.0)]

위 Dictionary Data에는 contours의 특징을 찾을 수 있는 기본 정보들이 있습니다(총 24개). 예를 들면 Contour의 중심값을 찾기 위해서는 아래 값을 사용하면 됩니다.

>>> cx = int(M['m10']/M['m00'])
>>> cy = int(M['m01']/M['m00'])

Contour Area
------------

Contour면적은 moments의 ``m00`` 값이거나 ``cv2.contourArea()`` 함수로 구할 수 있다.

>>> cv2.contourArea(cnt)
30464.0

Contour Perimeter
-----------------

Contour의 둘레 길이를 구할 수 있습니다. 사각형의 경우는 둘레길이의 합이 됩니다. 아래 함수의 2번째 argument가 true이면 폐곡선 도형을 만들어
둘레길이를 구하고, False이면 시작점과 끝점을 연결하지 않고 둘레 길이를 구합니다.

>>> cv2.arcLength(cnt, True)
750.0
>>> cv2.arcLength(cnt, False)
494.0


Contour Approximation
---------------------

Convex Hull
-----------

Checking Convexity
------------------

Bounding Rectangle
------------------

Minumum Enclosing Circle
------------------------

Fitting an Ellipse
------------------

Fitting a Line
---------------

