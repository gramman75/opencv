.. _imageArithmetic

========
허프 변환  
========

Goal
====

	* 허프 변환에 대해서 알수 있다.
	* 허프 변환을 이용하여 이미지의 Line을 찾을 수 있다.
	* 허프 변환에서 사용하는 ``cv2.HoughLines()`` , ``cv2.HoughLinesP()`` 함수에 대해서 알 수 있다.


Theory
======

허프변환은 이미지에서 모양을 찾는 가장 유명한 방법입니다. 이 방법을 이용하면 이미지의 형태를 찾거나, 누락되거나 깨진 영역을 복원할 수 있습니다.

기본적으로 허프변환의 직선의 방정식을 이용합니다. 하나의 점을 지나는 무수한 직선의 방적식은
y=mx+c로 표현할 수 있으며, 이것을 삼각함수를 이용하여 변형하면 r = 𝑥 cos 𝜃 + 𝑦 sin 𝜃 으로 표현할 수 있습니다.

그럼 아래 이미지를 보고 설명을 하겠습니다. 3개의 점이 있고, 그중 우리가 찾는 직선은 핑크색 직선 입니다.

그럼 각 점(x,y)에 대해서 삼각함수를 이용하여 𝜃 값을 1 ~ 180까지 변화를 하면서 원점에서 (x,y)까지의 거리(r)을 구합니다. 그러면 (𝜃, r)로 구성된 180개의 2차원 배열을 구할 수 있습니다.

동일한 방법으로 두번째 점에 대해서도 𝜃값을 변화해 가면서 2차원 배열을 구합니다.



.. figure:: ../../_static/25.imageHoughLineTransform/image01.png
    :align: center

    (출처: `위키 피디아 <https://en.wikipedia.org/wiki/Hough_transform>`_ )

이렇게 해서 구해서 2차원 배열을 다시 그래프로 표현하면 아래와 같이 사인파 그래프로 표현이 됩니다. 
아래 3개의 방정식의 만나는 점이 바로 직선인 확율이 높은 점 입니다.
즉, 𝜃가 60이고 거리가 80인 직선의 방정식을 구할 수 있는 것 입니다. 

.. figure:: ../../_static/25.imageHoughLineTransform/image02.png
    :align: center

    (출처: `위키 피디아 <https://en.wikipedia.org/wiki/Hough_transform>`_ )



OpenCV를 이용한 허프변환
======================

OpenCV는 위에서 설명한 수학적 이론이 ``cv2.HoughLines()`` 함수에 구현이 되어 있습니다.


.. py:function:: cv2.HoughLines(image, rho, theta, threshold[, lines[, srn[, stn[, min_theta[, max_theta]]]]]) → lines

    :param image: 8bit, single-channel binary image, canny edge를 선 적용.
    :param rho: r 값의 범위 (0 ~ 1 실수) 
    :param theta: 𝜃 값의 범위(0 ~ 180 정수)
    :param threshold: 만나는 점의 기준, 숫자가 작으면 많은 선이 검출되지만 정확도가 떨어지고, 숫자가 크면 정확도가 올라감. 


**Sample Code**

.. code-block:: python

	#-*- coding:utf-8-*-
	import cv2
	import numpy as np

	img = cv2.imread(r'images\chessboard\frame01.jpg')
	img_original = img.copy()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,50,150,apertureSize=3)

	lines = cv2.HoughLines(edges,1,np.pi/180,100)

	for i in xrange(len(lines)):
	    for rho, theta in lines[i]:
	        a = np.cos(theta)
	        b = np.sin(theta)
	        x0 = a*rho
	        y0 = b*rho
	        x1 = int(x0 + 1000*(-b))
	        y1 = int(y0+1000*(a))
	        x2 = int(x0 - 1000*(-b))
	        y2 = int(y0 -1000*(a))

	        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

	res = np.vstack((img_original,img))
	cv2.imshow('img',res)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


**Result**

.. figure:: ../../_static/25.imageHoughLineTransform/result01.jpg
    :align: center

    threshold가 100일 경우 


.. figure:: ../../_static/25.imageHoughLineTransform/result02.jpg
    :align: center

    threshold가 130일 경우 


확율 허프 변환    
=============

허프변환은 모든 점에 대해서 계산을 하기 때문에 시간이 많이 소요됩니다. 확율 허프변환(Probabilistic Hough Transform)은 이전 허프변환을 최적화 한 것 입니다. 모든 점을 대상으로 하는 것이 아니라 임의의 점을 이용하여 직선을 찾는 것입니다. 단 임계값을 작게 해야만 합니다. 
``cv2.HoughLinesP()`` 함수를 이용하는데, 장점은 선의 시작점과 끝점을 Return해주기 때문에
쉽게 화면에 표현할 수 있습니다. 


.. py:function:: cv2.HoughLinesP(image, rho, theta, threshold, minLineLength, maxLineGap) → lines

    :param image: 8bit, single-channel binary image, canny edge를 선 적용.
    :param rho: r 값의 범위 (0 ~ 1 실수) 
    :param theta: 𝜃 값의 범위(0 ~ 180 정수)
    :param threshold: 만나는 점의 기준, 숫자가 작으면 많은 선이 검출되지만 정확도가 떨어지고, 숫자가 크면 정확도가 올라감. 
    :param minLineLength: 선의 최소 길이. 이 값보다 작으면 reject.
    :param maxLineGap: 선과 선사이의 최대 허용간격. 이 값보다 작으며	 reject.


**Sample Code**

.. code-block:: python

	import cv2
	import numpy as np

	img = cv2.imread('images\hough_images.jpg')
	edges = cv2.Canny(img,50,200,apertureSize = 3)
	gray = cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)
	minLineLength = 100
	maxLineGap = 0

	lines = cv2.HoughLinesP(edges,1,np.pi/360,100,minLineLength,maxLineGap)
	for i in xrange(len(lines)):
	    for x1,y1,x2,y2 in lines[i]:        
	        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),3)


	cv2.imshow('img1',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()




**Result**

.. figure:: ../../_static/25.imageHoughLineTransform/result03.jpg
    :align: center

    MinLineLength = 100, MaxLineGap = 10


.. figure:: ../../_static/25.imageHoughLineTransform/result04.jpg
    :align: center

    MinLineLength = 100, MaxLineGap = 0