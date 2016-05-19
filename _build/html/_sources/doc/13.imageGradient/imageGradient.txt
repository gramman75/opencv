.. imageGradient

===============
Image Gradients
===============

Goal
====
	* Edge Detection에 대해서 알 수 있다.

Gradient(기울기)는 스칼라장(즉, 공간)에서 최대의 증가율을 나타내는 벡터장(방향과 힘)을 뜻합니다.

어렵죠? 영상처리에서 gradient는 영상의 edge 및 그 방향을 찾는 용도로 활용이 되는데요. 이미지 (x,y)에서의
벡터값(크기와 방향, 즉 밝기와 밝기의 변화하는 방향)을 구해서 해당 pixel이 edge에 얼마나 가까운지, 그리고 그 방향이
어디인지 쉽게 알수 있게 합니다.
(일반적으로 이미지의 Gradient를 생각해보시면 밝기의 변화와 그 방향을 알 수 있습니다.)

아래 설명할 방법들은 Gradient를 이용해서 이미지의 edge를 검출하는 방법입니다.

Sobel & Scharr Filter
=====================

Gaussian smoothing과 미분을 이용한 방법입니다. 그래서 노이즈가 있는 이미지에 적용하면 좋습니다. X축과 Y축을 미분하는 방법으로 경계값을 계산합니다.

직선을 미분하면 상수, 곡선을 미분하면 또 다른 방정식이 나오는 성질을 이용하여 edge에 대한 선을 그려주는 기능을 합니다.
X축 미분은 수평선(수직선이 남음), Y축 미분은 수직선(수평선이 남음)을 미분하여 경계가 사라지는 효과가 있습니다.
미분시 소실되는 표본의 정보가 많을 수 있어 ``aperture_size`` 값을 이용하여 소실되는 정도를 조절할 수 있습니다.

만약 ksize가 -1이면 3x3 Scharr filter가 적용이 되어 Sobel의 3x3보다 좀 더 나은 결과를 보여 줍니다.

.. py:function:: cv2.Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]]) → dst

    :param src: input image
    :param ddepth: output image의 depth, -1이면 input image와 동일.
    :param dx: x축 미분 차수.
    :param dy: y축 미분 차수.
    :param ksize: kernel size(ksize x ksize)

.. py:function:: cv2.Scharr(src, ddepth, dx, dy[, dst[, scale[, delta[, borderType]]]]) → dst

    ``cv2.Sobel()`` 함수와 동일하나 ksize가 sobel의 3x3 보다 좀더 정확하게 적용이 됩니다.




Laplacian 함수
=============

이미지의 가로와 세로에 대한 Gradient를 2차 미분한 값입니다. Sobel filter에 미분의 정도가 더해진 것과 비슷합니다.(dx와 dy가 2인 경우)
blob(주위의 pixel과 확연한 picel차이를 나타내는 덩어리)검출에 많이 사용됩니다.

.. py:function:: cv2.Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]]) → dst

    :param src: source image
    :param ddepth: output iamge의  depth.

Canny Edge Detection
=====================

가장 유명한 Edge Detection방법입니다. 여러 단계의 Algorithm을 통해서 경계를 찾아 냅니다.

#. Noise Reduction
    이미지의 Noise를 제거합니다. 이때 5x5의 Gaussian filter를 이용합니다.

#. Edge Gradient Detection

	    이미지에서 Gradient의 방향과 강도를 확인합니다. 경계값에서는 주변과 색이 다르기 때문에 미분값이 급속도로 변하게 됩니다. 이를 통해 경계값 후보군을 선별합니다.

#. Non-maximum Suppression

	    이미지의 pixel을 Full scan하여 Edge가 아닌 pixel은 제거합니다.

#. Hysteresis Thresholding

	    이제 지금까지 Edge로 판단된 pixel이 진짜 edge인지 판별하는 작업을 합니다. max val과 minVal(임계값)을 설정하여 maxVal 이상은 강한 Edge, min과 max사이는 약한 edge로 설정합니다.
	    이제 약한 edge가 진짜 edge인지 확인하기 위해서 강한 edge와 연결이 되어 있으면 edge로 판단하고, 그러지 않으면 제거합니다.

이와 같은 일련의 작업을 통해서 경계값만을 남겨두고 제거합니다.

.. py:function:: cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]]) → edges

    :param image: 8-bit input image
    :param threshold1: Hysteresis Thredsholding 작업에서의 min 값
    :param threshold2: Hysteresis Thredsholding 작업에서의 max 값


아래는 지금까지 설명한 edge detection방법에 대한 예제입니다.

**Sample Code**

.. code-block:: python
    :linenos:

    #-*- coding:utf-8 -*-
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt

    img = cv2.imread('images/dave.png')
    canny = cv2.Canny(img,30,70)

    laplacian = cv2.Laplacian(img,cv2.CV_8U)
    sobelx = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)
    sobely = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)

    images = [img,laplacian, sobelx, sobely, canny]
    titles = ['Origianl', 'Laplacian', 'Sobel X', 'Sobel Y','Canny']

    for i in xrange(5):
        plt.subplot(2,3,i+1),plt.imshow(images[i]),plt.title([titles[i]])
        plt.xticks([]),plt.yticks([])

    plt.show()

**Result**

.. figure:: ../../_static/13.imageGradient/result01.jpg
    :align: center
