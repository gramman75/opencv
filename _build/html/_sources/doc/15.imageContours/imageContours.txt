.. imageContours

==============
Image Contours
==============

Goal
====

    * Contours에 대해서 알 수 있다
    * ``cv2.findContours()`` , ``cv2.drawContours()`` 함수에 대해서 알 수 있다.

Contours
========

Contours란 동일한 색 또는 동일한 강도를 가지고 있는 영역의 경계선을 연결한 선입니다. 우리가 자주 보는 것으로는 등고선이나 일기예보에서 볼 수 있습니다.

.. figure:: ../../_static/15.imageContours/image01.jpg
    :align: center

    등고선(Contours Line)(출처 `위키피디아 <https://en.wikipedia.org/wiki/Contour_line>`_ )

대상의 외형을 파악하는데 유용하게 사용이 됩니다.

    * 정확도를 높히기 위해서 Binary Image를 사용합니다. threshold나 canny edge를 선처리로 수행합니다.
    * ``cv2.findContours()`` 함수는 원본 이미지를 직접 수정하기 때문에, 원본 이미지를 보존 하려면 Copy해서 사용해야 합니다.
    * OpenCV에서는 contours를 찾는 것은 검은색 배경에서 하얀색 대상을 찾는 것과 비슷합니다. 그래서 대상은 흰색, 배경은 검은색으로 해야 합니다.

Find & Draw Contours
====================

OpenCV에서 contours를 찾고, 그리기 위해서 아래 2개의 함수를 사용합니다.

.. py:function:: cv2.findContours(image, mode, method[, contours[, hierarchy[, offset]]]) → image, contours, hierarchy

    :param image: 8-bit single-channel image. binary image.
    :param mode: contours를 찾는 방법

        * ``cv2.RETR_EXTERNAL`` : contours line중 가장 바같쪽 Line만 찾음.
        * ``cv2.RETR_LIST`` : 모든 contours line을 찾지만, hierachy 관계를 구성하지 않음.
        * ``cv2.RETR_CCOMP`` : 모든 contours line을 찾으며, hieracy관계는 2-level로 구성함.
        * ``cv2.RETR_TREE`` : 모든 contours line을 찾으며, 모든 hieracy관계를 구성함.

    :param method: contours를 찾을 때 사용하는 근사치 방법

        * ``cv2.CHAIN_APPROX_NONE`` : 모든 contours point를 저장.
        * ``cv2.CHAIN_APPROX_SIMPLE`` :  contours line을 그릴 수 있는 point 만 저장. (ex; 사각형이면 4개 point)
        * ``cv2.CHAIN_APPROX_TC89_L1`` : contours point를 찾는 algorithm
        * ``cv2.CHAIN_APPROX_TC89_KCOS`` : contours point를 찾는 algorithm

    :return: image, contours , hierachy

Method에 대해서 설명을 하면 아래 예제의 결과에서 처럼 사각형의 contours line을 그릴 때, ``cv2.CHAIN_APPROX_NONE`` 는 모든 point를 저장하고
``cv2.CHAIN_APPROX_SIMPLE`` 는 4개의 point만을 저장하여 메모리를 절약합니다.

>>> contours[0].shape #cv2.CHAIN_APPROX_SIMPLE(4 point)
(4, 1, 2)

>>> contours[0].shape #cv2.CHAIN_APPROX_NONE(750 point)
(750, 1, 2)

mode에 대해서는 Hierachy를 설명할 때 같이 설명하도록 하겠습니다.

.. py:function:: cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]]) → dst

    :param image: 원본 이미지
    :param contours: contours정보.
    :param contourIdx: contours list type에서 몇번째 contours line을 그릴 것인지. -1 이면 전체
    :param color: contours line color
    :param thickness: contours line의 두께. 음수이면 contours line의 내부를 채움.
    :return: image에 contours가 그려진 결과

아래는 예제와 결과입니다.

**Sample Code**

.. code-block:: python
    :linenos:

    #-*- coding:utf-8 -*-
    import cv2
    import numpy as np

    img = cv2.imread('images/rectangle.jpg')
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #threshold를 이용하여 binary image로 변환
    ret, thresh = cv2.threshold(imgray,127,255,0)

    #contours는 point의 list형태. 예제에서는 사각형이 하나의 contours line을 구성하기 때문에 len(contours) = 1. 값은 사각형의 꼭지점 좌표.
    #hierachy는 contours line의 계층 구조
    image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    image = cv2.drawContours(img, contours, -1, (0,255,0), 3)

    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

**Result**

.. figure:: ../../_static/15.imageContours/result01.jpg
    :align: center










