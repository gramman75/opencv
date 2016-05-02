.. _drawShape

###########
도형 그리기
###########

Goal
====
    * 다양한 모양의 도형을 그릴 수 있다.
    * ``cv2.line()`` , ``cv2.circle()`` , ``cv2.rectangle()`` , ``cv2.putText()`` 사용법을 알 수 있다.

도형그리기는 동영상이나 이미지에서 Match가 되는 영역을 찾은 후에 사용자가 인식하기 쉽게 표시하는 목적으로
사용됩니다.


Line 그리기
===========

Start와 End 점을 연결하여 직선을 그립니다.

.. py:function:: cv2.line(img, start, end, color, thickness)

    :param img: 그림을 그릴 이미지 파일
    :param start: 시작 좌표(ex; (0,0))
    :param end: 종료 좌표(ex; (500. 500))
    :param color: BGR형태의 Color(ex; (255, 0, 0) -> Blue)
    :param thickness: 선의 두께. pixel
    :type thickness: int

**Sample Code**

.. code-block:: python
    :linenos:

    import numpy as np
    import cv2

    #모두 0으로 되어 있는 빈 Canvas(검정색)
    img = np.zeros((512, 512), np.uint8)
    img = cv2.line(img, (200, 0), (100, 511), (255, 0, 0), 5)

    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

사각형 그리기
=============

top-left corner와 bottom-right corner점을 연결하는 사각형을 그립니다.

.. py:function:: cv2.rectangle(img, start, end, color, thickness)

    :param img: 그림을 그릴 이미지 파일
    :param start: 시작 좌표(ex; (0,0))
    :param end: 종료 좌표(ex; (500. 500))
    :param color: BGR형태의 Color(ex; (255, 0, 0) -> Blue)
    :param thickness: 선의 두께. pixel
    :type thickness: int

**Sample Code**

.. code-block:: python

    img = cv2.rectangle(img, (384, 0), (510, 128), (0,255,0), 3)


원 그리기
=========

Polygon 그리기
==============


