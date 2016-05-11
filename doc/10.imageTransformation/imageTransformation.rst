.. _imageTransformation

================
이미지의 기하학적 변형
================

Goal
====

    * 기하학적 변형에 대해서 알 수 있다.
    * ``cv2.getPerspectiveTransform()`` 함수에 대해서 알 수 있다.

Transformations
===============

변환이란 수학적으로 표현하면 아래와 같습니다.

    * 좌표 x를 좌표 x'로 변환하는 함수

예로는 사이즈 변경(Scaling), 위치변경(Translation), 회전(Rotaion) 등이 있습니다.
변환의 종류에는 몇가지 분류가 있습니다.

    * 강체변환(Ridid-Body) : 크기 및 각도가 보존(ex; Translation, Rotation)
    * 유사변환(Similarity) : 크기는 변하고 각도는 보존(ex; Scaling)
    * 선형변환(Linear) : Vector 공간에서의 이동. 이동변환은 제외.
    * Affine : 선형변환과 이동변환까지 포함. 선의 수평성은 유지.(ex;사각형->평행사변형)
    * Perspective : Affine변환에 수평성도 유지되지 않음. 원근변환

Scaling
-------

Scaling은 이미지의 사이즈가 변하는 것 입니다. OpenCV에서는 ``cv2.resize()`` 함수를 사용하여 적용할 수 있습니다.
사이즈가 변하면 pixel사이의 값을 결정을 해야 하는데, 이때 사용하는 것을 보간법(Interpolation method)입니다.
많이 사용되는 보간법은 사이즈를 줄일 때는 ``cv2.INTER_AREA`` , 사이즈를 크게할 때는 ``cv2.INTER_CUBIC`` , ``cv2.INTER_LINEAR``
을 사용합니다.

.. py:function:: cv2.resize(img, dsize, fx, fy, interpolation)

    :param img: Image
    :param dsize: Manual Size. 가로, 세로 형태의 tuple(ex; (100,200))
    :param fx: 가로 사이즈의 배수. 2배로 크게하려면 2. 반으로 줄이려면 0.5
    :param fy: 세로 사이즈의 배수
    :param interpolation: 보간법

**Sample Code**

.. code-block:: python
    :linenos:

    #-*- coding:utf-8 -*-
    import cv2
    import numpy as np

    img = cv2.imread('images/logo.png')

    # 행 : Height, 열:width
    height, width = img.shape[:2]

    # 이미지 축소
    shrink = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # Manual Size지정
    zoom1 = cv2.resize(img, (width*2, height*2), interpolation=cv2.INTER_CUBIC)

    # 배수 Size지정
    zoom2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)


    cv2.imshow('Origianl', img)
    cv2.imshow('Shrink', shrink)
    cv2.imshow('Zoom1', zoom1)
    cv2.imshow('Zoom2', zoom2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

**Result**

.. figure:: ../../_static/10.imageTransformation/result01.jpg
    :align: center

    Original

.. figure:: ../../_static/10.imageTransformation/result02.jpg
    :align: center

    Shrink

.. figure:: ../../_static/10.imageTransformation/result03.jpg
    :align: center

    Zoom

Translation
-----------

Translation은 이미지의 위치를 변경하는 변환입니다.

.. py:function:: cv2.warpAffine(src, M, dsize)

    :param src: Image
    :param M: 변환 행렬
    :param dsize: output image size(ex; (width=columns, height=rows)
    :type dsize: tuple

.. warning:: width은 column의 수 이고, height는 row의 수 입니다.

여기서 변환행렬은 2X3의 이차원 행렬입니다. [[1,0,x축이동],[0,1,y축이동]] 형태의 float32 type의
numpy array입니다.

**Sample Code**

.. code-block:: python
    :linenos:

    #-*- coding:utf-8 -*-
    import cv2
    import numpy as np

    img = cv2.imread('images/logo.png')

    rows, cols = img.shape[:2]

    # 변환 행렬, X축으로 10, Y축으로 20 이동
    M = np.float32([[1,0,10],[0,1,20]])

    dst = cv2.warpAffine(img, M,(cols, rows))
    cv2.imshow('Original', img)
    cv2.imshow('Translation', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


**Result**

.. figure:: ../../_static/10.imageTransformation/result04.jpg
    :align: center

    Result

Rotation
--------



Affine Transformation
---------------------

Perspective Transformation
--------------------------

