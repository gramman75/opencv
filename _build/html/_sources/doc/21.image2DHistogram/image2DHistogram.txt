.. image2DHistogram

============
2D Histogram
============

Goal
====

    * 2D Histogram을 찿아서 plot형태로 그릴 수 있다.


소개
====

지금까지 Histogram은 1차원으로 grayscale 이미지의 pixel의 강도, 즉 빛의 세기를 분석한 결과였습니다.
2D Histogrm은 Color 이미지의 Hue(색상) & Saturation(채도)을 동시에 분석하는 방법입니다.

이 결과는 다음 장에서 설명할 Histogram Back-Projection에서 유용하게 사용이 됩니다.

적용
====

우선 Hue와 Saturation으로 분석을 하기 때문에 대상 이미지를 HSV Format로 변환을 해야 합니다.
그 다음에 ``calcHist()`` 라는 OpenCV의 Histogram분석 함수에 적용을 합니다.

.. function:: calcHist([image],[channel],mask,[bins],[range])

   Histogram 분석 함수

   :param image: HSV로 변환된 이미지
   :param channel: 0-> Hue, 1-> Saturation
   :param bins: [180,256] 첫번째는 Hue, 두번째는 Saturation
   :param range:  [0,180,0,256] : Hue(0~180), Saturation(0,256)


아래 이미지의 2D Histogram을 분석할 결과 입니다.

.. figure:: ../../_static/21.image2DHistogram/image01.jpg
    :align: center

**Sample Code**

.. code-block:: python
    :linenos:

    #-*- coding:utf-8-*-
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt

    img = cv2.imread('images/home.jpg')
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    hist = cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])

    cv2.imshow('Hist',hist)

    plt.imshow(hist) #, interpolation='nearest')
    plt.show()


.. figure:: ../../_static/21.image2DHistogram/result01.png
    :align: center

위 Histogram을 보면 X축은 Saturation, Y축은 Hue값을 나타냅니다.
Y축을 보면 100근처에 값이 모여 있는 것을 알 수 있습니다. HSV모델에서 H가 100이면 하늘색입니다.
그리고 25근처에도 값이 모여 있습니다. H값이 25이면 노란색입니다.
즉 이 이미지는 하늘색과 노란색이 많이 분포되어 있다는 것을 2D Histogram을 통해서 알 수 있습니다.

다음 장에서는 이 2D Histogram을 이용하여 Histogram Backprojection에 대해서 알아 보겠습니다.
