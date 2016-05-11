.. _imageProcessing

=================
이미지 Processing
=================

Goal
====
    * 디지털 영상의 표현 방법에 대해서 알 수 있다.
    * Color-space중 Binary Image, Grayscale, RGB, HSV에 대해서 알 수 있다.
    * 각 Color-space 변환 방법에 대해서 알 수 있다.
    * 동영상에서 간단한 Object Tracking을 할 수 있다.
    * ``cv2.cvtColor()`` , ``cv2.inRange()`` 함수에 대해서 알 수 있다.

Digital Image
=============
| 디지털 영상은 2차원 행렬의 형태로 표현이 됩니다. 각 격자가 하나의 pixel이 됩니다. 이를 bitmap image라고 합니다.

| 각 pixel의 위치는 2가지 형태로 표현을 할 수가 있는데. 영상좌표와 행렬 위치로 표현이 됩니다.
| 영상 좌표는 좌측 상단의 꼭지점을 중심으로 (x,y)로 표현을 합니다. 행렬 위치는 (r,c)로 표현을 합니다. OpenCV에서 영상좌표와 행렬 위치 2가지 형태가 사용되기 때문에 유의해야 합니다.

.. figure:: ../../_static/08.imageProcessing/image1.png
    :align: center

    Pixel 표현 방법

Digital Image의 유형
====================

Binary Image
------------
Binary Image는 pixel당 1bit로 표현하는 영상을 의미합니다. 즉 흰색과 검은색으로만 표현이 되는 영상입니다.

.. figure:: ../../_static/08.imageProcessing/image2.png
    :align: center

    Binary Image

위 이미지에서 좌측 상단의 이미지가 원본 이미지 입니다. 원본 이미지를 thresholding처리를 하여 binary image로 변환한 결과가
우측 상단의 이미지 입니다. 우측 하단의 이미지는 화면에 표현할 때 사용하는 방법으로 binary image의 밀도를 조절하여 밝기를 표현
하는 방법입니다. 이를 dithering 이라고 합니다.

Grayscale Image
---------------

Grayscale Image는 Pixel당 8bit, 즉 256단계의 명암(빛의 세기)을 표현할 수 있는 이미지입니다.

.. figure:: ../../_static/08.imageProcessing/image3.png
    :align: center

    Grayscale Image(출처 `위키피디아 <https://ko.wikipedia.org/wiki/%EA%B7%B8%EB%A0%88%EC%9D%B4%EC%8A%A4%EC%BC%80%EC%9D%BC>`_)


Color Image
-----------
Color



RGB Color-space
---------------

HSV Color-space
---------------

Color-space 변환
===============

OpenCV에는 150여가지 변환 방법이 있습니다. 아래는 변환 방법을 확인하는 코드 입니다.

>>> import cv2
>>> flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
>>> print flags


그 중에 서 많이 사용되는 BGR<->Gray, BGR<->HSV에 대해서 알아 보겠습니다.
변환을 위해서 사용하는 함수는 ``cv2.cvtColor()`` 함수 입니다.

.. py:function:: cv2.cvtColor(src, code)

    :params src: image
    :params code: 변환 코드

BGR->Grayscale로 변환하기 위해서는 **cv2.COLOR_BGR2GRAY** 를 사용합니다. BGR->HSV로 변환하기 위해서는
**cv2.COLOR_BGR2HSV** 를 사용합니다.

.. note:: Hue는 [0,179], Saturation은 [0,255], Value는 [0,255]로 표현이 됩니다.

Object Tracking
===============

다음 예제는 단순한 Object Tracking입니다. 영상에서 파란색 부분을 찿아서 binary image로 보여줍니다.

    * Video로 부터 Frame을 읽어 들입니다.
    * frame을 HSV로 변환을 합니다.
    * 변환한 이미지에서 blue 영역을 찾아서 mask를 생성합니다.
    * frame에 mask를 적용하여 이미지를 보여 줍니다.

Code는 아래와 같습니다.

**Sample Code**

.. literalinclude:: objectTracking.py
    :linenos:


**Result**

.. figure:: ../../_static/08.imageProcessing/tracking.jpg
    :align: center

참고로 HSV의 색 영역을 확인하는 방법은 아래와 같습니다.

>>> green = np.uint8[[[0,255,0]]]
>>> green_hsv = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
>>> print green_hsv
[[[60, 255, 255]]]

위 결과에서 [H-10,100,100]과 [H+10,255,255]와 같이 상하한선을 정하여 색 영역 범위를 확인할 수 있습니다.

