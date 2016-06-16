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

    Grayscale Image(출처 `위키피디아 <https://ko.wikipedia.org/wiki/%EA%B7%B8%EB%A0%88%EC%9D%B4%EC%8A%A4%EC%BC%80%EC%9D%BC>`_ )


Color Image
-----------
Color 이미지는 pixel의 색을 표현하기 위해서 pixel당 24bit를 사용합니다. 총 16,777,216 가지의 색을 표현할 수 있습니다.
이것을 일반적으로 True color image라고 합니다. pixel은 RGB 각각을 위해서 8bit를 사용하게 됩니다.
OpenCV에서는 BGR로 표현을 하기 때문에 Blue->(255,0,0), Green->(0,255,0), Red->(0,0,255), White->(255,255,255), Black->(0,0,0)으로
표현할 수 있습니다.

각 pixel당 3Byte를 사용하기 때문에 용량이 큽니다. 이를 해결하기 위해서 lookup table을 사용하여, 해당 pixel에는 index만 을 저장하기도 합니다.

.. figure:: ../../_static/08.imageProcessing/image4.png
    :align: center

    Indexed Color Image

RGB Color-space
---------------
RGB 모델은 빛의 삼원색인 빨간색, 초록색, 파란색을 기본 색으로 사용을 합니다. 정육면체 모델 형태로 표현할 수 있습니다.

.. figure:: ../../_static/08.imageProcessing/image5.png
    :align: center

    RGB 모델(출처 : `위키피디아 <https://ko.wikipedia.org/wiki/RGB_%EA%B0%80%EC%82%B0%ED%98%BC%ED%95%A9>`_ )

HSV Color-space
---------------
이미지 처리에서 가장 많이 사용되는 형태의 Color 모델입니다. 하나의 모델에서 색과 채도, 명도를 모두 알 수 있습니다.
원뿔 형태의 모델로 표현이 됩니다.

.. figure:: ../../_static/08.imageProcessing/image6.png
    :align: center

    HSV 모델

HSV의 의미는 다음과 같습니다.

    * H(ue) : 색상. 일반적인 색을 의미함. 원추모형에서 각도로 표현이 됨.(0: Red, 120도 : Green, 240: Blue)
    * S(aturation) : 채도. 색읜 순수성을 의미하며 일반적으로 짙다, 흐리다로 표현이 됨. 중심에서 바깥쪽으로 이동하면 채도가 높음.
    * V(alue) : 명도. 색의 밝고 어두운 정도. 수직축의 깊이로 표현. 어둡다 밝다로 표현이 됨.


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

