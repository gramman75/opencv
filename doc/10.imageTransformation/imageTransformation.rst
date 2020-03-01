.. _imageTransformation

======================
이미지의 기하학적 변형
======================

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

    * 강체변환(Rigid-Body) : 크기 및 각도가 보존(ex; Translation, Rotation)
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

물체를 평면상의 한 점을 중심으로 𝜃 만큼 회전하는 변환 입니다. 양의 각도는 시계반대방향으로 회전을 합니다.
역시 변환 행렬이 필요한데, 변환 행렬을 생성하는 함수가 ``cv2.getRotationMatrix2D()`` 함수입니다.


.. py:function:: cv2.getRotationMatrix2D(center, angle, scale) -> M

    :param center: 이미지의 중심 좌표
    :param angle: 회전 각도
    :param scale: scale factor

위 결과에서 나온 변환행렬을 ``cv2.warpAffine()`` 함수에 적용합니다.

**Sample Code**

.. code-block:: python
    :linenos:

    #-*- coding:utf-8 -*-
    import cv2

    img = cv2.imread('images/logo.png')

    rows, cols = img.shape[:2]

    # 이미지의 중심점을 기준으로 90도 회전 하면서 0.5배 Scale
    M= cv2.getRotationMatrix2D((cols/2, rows/2),90, 0.5)

    dst = cv2.warpAffine(img, M,(cols, rows))

    cv2.imshow('Original', img)
    cv2.imshow('Rotation', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

**Result**

.. figure:: ../../_static/10.imageTransformation/result05.jpg
    :align: center


Affine Transformation
---------------------

Affine Transformation은 선의 평행성은 유지가 되면서 이미지를 변환하는 작업입니다. 이동, 확대, Scale, 반전까지 포함된 변환입니다.
Affine 변환을 위해서는 3개의 Match가 되는 점이 있으면 변환행렬을 구할 수 있습니다.

**Sample Code**

.. code-block:: python
    :linenos:

    #-*- coding:utf-8 -*-
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt

    img = cv2.imread('images/chessboard.jpg')
    rows, cols, ch = img.shape

    pts1 = np.float32([[200,100],[400,100],[200,200]])
    pts2 = np.float32([[200,300],[400,200],[200,400]])

    # pts1의 좌표에 표시. Affine 변환 후 이동 점 확인.
    cv2.circle(img, (200,100), 10, (255,0,0),-1)
    cv2.circle(img, (400,100), 10, (0,255,0),-1)
    cv2.circle(img, (200,200), 10, (0,0,255),-1)

    M = cv2.getAffineTransform(pts1, pts2)

    dst = cv2.warpAffine(img, M, (cols,rows))

    plt.subplot(121),plt.imshow(img),plt.title('image')
    plt.subplot(122),plt.imshow(dst),plt.title('Affine')
    plt.show()

**Result**

.. figure:: ../../_static/10.imageTransformation/result06.jpg
    :align: center



Perspective Transformation
--------------------------

Perspective(원근법) 변환은 직선의 성질만 유지가 되고, 선의 평행성은 유지가 되지 않는 변환입니다. 기차길은 서로 평행하지만
원근변환을 거치면 평행성은 유지 되지 못하고 하나의 점에서 만나는 것 처럼 보입니다.(반대의 변환도 가능)

4개의 Point의 Input값과이동할 output Point 가 필요합니다.

변환 행렬을 구하기 위해서는 ``cv2.getPerspectiveTransform()`` 함수가 필요하며, ``cv2.warpPerspective()`` 함수에 변환행렬값을 적용하여
최종 결과 이미지를 얻을 수 있습니다.

아래의 예는 원근법이 적용된 효과를 제거하는 예제입니다.

**Sample Code**

.. code-block:: python
    :linenos:

    #-*- coding:utf-8 -*-
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt

    img = cv2.imread('images/perspective.jpg')
    # [x,y] 좌표점을 4x2의 행렬로 작성
    # 좌표점은 좌상->좌하->우상->우하
    pts1 = np.float32([[504,1003],[243,1525],[1000,1000],[1280,1685]])

    # 좌표의 이동점
    pts2 = np.float32([[10,10],[10,1000],[1000,10],[1000,1000]])

    # pts1의 좌표에 표시. perspective 변환 후 이동 점 확인.
    cv2.circle(img, (504,1003), 20, (255,0,0),-1)
    cv2.circle(img, (243,1524), 20, (0,255,0),-1)
    cv2.circle(img, (1000,1000), 20, (0,0,255),-1)
    cv2.circle(img, (1280,1685), 20, (0,0,0),-1)

    M = cv2.getPerspectiveTransform(pts1, pts2)

    dst = cv2.warpPerspective(img, M, (1100,1100))

    plt.subplot(121),plt.imshow(img),plt.title('image')
    plt.subplot(122),plt.imshow(dst),plt.title('Perspective')
    plt.show()

**Result**

.. figure:: ../../_static/10.imageTransformation/result07.jpg
    :align: center
