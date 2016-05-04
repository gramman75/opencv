.. _drawWithMouse

##############
Mouse로 그리기
##############


Goal
====
    * Mouse Event의 적용 방법에 대해서 알 수 있다.
    * ``cv2.setMouseCallback()`` 함수에 대해서 알 수 있다.

작동방법
========

OpenCV에는 이미 Mouse Event의 종류에 대해서 사전 정의가 되어 있습니다. 확인을 하기 위해서 Python Terminal에서 아래와 같이 입력해보시기 바랍니다.

>>> import cv2
>>> events = [i for i in dir(cv2) if 'EVENT' in i]
>>> print events

실행을 하면 다양한 Mouse Event의 종류를 알 수 있습니다. 어떤 종류의 Event인지는 이름을 보면 쉽게 알 수 있습니다.::

    'EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP'

Mouse Event를 확인하고 Callback을 호출하는 함수가 ``cv2.setMouseCallback()`` 입니다.

.. py:function:: cv2.setMouseCallback(windowName, callback, param=None)

    :param windowName: windowName
    :param callback: callback함수. callback함수에는 (event, x, y, flags, param)가 전달 됨.
    :param param: callback함수에 전달되는 Data


간단한 Demo
===========

아래 Demo는 화면에 Double-Click을 하면 원이 그려지는 예제입니다.

.. code-block:: python
    :linenos:

    import cv2
    import numpy as np

    # callback함수
    def draw_circle(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(img,(x,y), 100,(255,0,0),-1)

    # 빈 Image 생성
    img = np.zeros((512,512,3), np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)

    while(1):
        cv2.imshow('image', img)
        if cv2.waitKey(0) & 0xFF == 27:
            break

    cv2.destroyAllWindows()


Advanced Demo
=============

다음은 마우스를 누른 상태에서 이동시 원 또는 사각형을 그리는 Demo입니다.
이 예제는 향후 대상 추적이나 이미지 Segmentaion시 응용될 수 있습니다.(ex; 이미지에서 대상을 마우스로 선택하고 동일한 대상을 찾는 경우)

.. literalinclude:: mouseEventMove.py
    :linenos:
