.. imageContourHierarchy

==================
Contours Hierarchy
==================

Goal
====
    * Contours의 Hierarchy구조에 대해서 알 수 있다.


Image에는 여러개의  Contours가 존재하고, 그 사이에는 서로 포함하는 관계가 존재합니다. 그 관계를 Contours Hierarchy라고 합니다.
이전, 이후, Parent, Child 관계를 파악할 수 있습니다. 이런 관계를 파악하기 위해서는 ``cv2.findContours()`` 에 Contour Retrieval Mode값에 의해서
결정이 됩니다.

그럼 먼저 Contours Hierarchy에 대해서 알아 보겠습니다.

Hierarchy
=========

아래 원본 이미지에 대해서 Contour Line을 적용한 결과 입니다.

.. figure:: ../../_static/18.imageContourHierarchy/image01.jpg
:align: center

    원본 이미지
.. code-block:: python
    :lineons:

    #-*- coding:utf-8 -*-
    import cv2
    import numpy as np
    import random
    from matplotlib import pyplot as plt

    img = cv2.imread('images/imageHierarchy.png')

    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray,125,255,0)

    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for i in xrange(len(contours)):
        #각 Contour Line을 구분하기 위해서 Color Random생성
        b = random.randrange(1,255)
        g = random.randrange(1,255)
        r = random.randrange(1,255)

        cnt = contours[i]
        img = cv2.drawContours(img, [cnt], -1,(b,g,r), 2)

    titles = ['Result']
    images = [img]

    for i in xrange(1):
        plt.subplot(1,1,i+1), plt.title(titles[i]), plt.imshow(images[i])
        plt.xticks([]), plt.yticks([])

    plt.show()

**Result**

.. figure:: ../../_static/18.imageContourHierarchy/result01.jpg
    :align: center

위 결과는 총 9개의 contour line으로 구성이 되어 있습니다. 주의해서 봐야할 부분은 3,3a와 4,4a입니다. Hirerarchy 구성시 child의 child가 있을 경우
바깥선과 안쪽선이 서로 분리가 되어  contour line을 구성합니다. 이는 포함 관계를 표현하기 위해서 입니다.(5의 경우는 child만 있기 때문에 contour line이 분리되지 않았습니다.)

이제 contour retrival mode에 따라서 hirerarchy값이 어떻게 표현이 되는 지 확인해 보겠습니다.

RETR_LIST
---------

hierarchy의 shape는 (1, x, 4)의 형태입니다. 여기서 3번째 차원의 4개의 값이 hierarchy를 표현합니다. 각 값의 의미는 (next, prev, child, parent) 입니다.
RETR_LIST는 선/후 관계만을 표현하고, parent/child관계를 표현하지 않는 mode입니다.
먼저 위 예제에서 mode를 ``cv2.RETR_LIST`` 로 한 결과를 확인해 보겠습니다.

>>> hierarchy
array([[[ 1, -1, -1, -1],
        [ 2,  0, -1, -1],
        [ 3,  1, -1, -1],
        [ 4,  2, -1, -1],
        [ 5,  3, -1, -1],
        [ 6,  4, -1, -1],
        [ 7,  5, -1, -1],
        [ 8,  6, -1, -1],
        [-1,  7, -1, -1]]])

mode의 특성대로 next와 prev는 값이 있지만, child와 parent는 모두 -1 입니다.(-1은 대상이 없음을 의미함.)
예를 들으 보면 contour-0는 next가 contour-1이고, prev와 child, parent가 없다는 의미 입니다.
contour-1은 next가 contour-2이고, prev가 contour-0이고, child와 parent는 해당 사항이 없습니다.
Hierarchy를 구할 필요가 없을 때 사용하면 좋습니다.

RETR_EXTERNAL
-------------

이 mode는 가장 바깥쪽에 있는 contour만을 return합니다. 위 예에서는 1,2,3번 line입니다.(parent/child는 구성하지 않습니다.)

>>> hierarchy
array([[[ 1, -1, -1, -1],
        [ 2,  0, -1, -1],
        [-1,  1, -1, -1]]])

RETR_CCOMP
----------

이 mode는


>>> hierarchy
array([[[ 3, -1,  1, -1],
        [ 2, -1, -1,  0],
        [-1,  1, -1,  0],
        [ 5,  0,  4, -1],
        [-1, -1, -1,  3],
        [ 7,  3,  6, -1],
        [-1, -1, -1,  5],
        [ 8,  5, -1, -1],
        [-1,  7, -1, -1]]])

