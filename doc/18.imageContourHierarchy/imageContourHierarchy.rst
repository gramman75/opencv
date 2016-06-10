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

    image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

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
