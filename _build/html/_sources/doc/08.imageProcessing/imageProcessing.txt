.. _imageProcessing

===============
이미지 Processing
===============

Goal
====
    * Color-space중 Binary Image, Grayscale, RGB, HSV에 대해서 알 수 있다.
    * 각 Color-space 변환 방법에 대해서 알 수 있다.
    * 동영상에서 간단한 Object Tracking을 할 수 있다.
    * ``cv2.cvtColor()`` , ``cv2.inRange()`` 함수에 대해서 알 수 있다.

Binary Image
============

Grayscale Image
===============

Color Image
===========


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

