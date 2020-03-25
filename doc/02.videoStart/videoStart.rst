.. _videoStart

###########
영상 다루기
###########


Goal
====
    * 동영상을 읽고, 보여주고, 저장할 수 있다.
    * 관련 함수인 ``cv2.VideoCapture()`` , ``cv2.VideoWriter()`` 에 대해서 알 수 있다.


Camera로 부터 영상 재생
=======================

Camera로부터 영상을 읽어, 화면에 보옂기 위해서 아래와 같은 순서로 진행을 합니다.

    * VideoCapture Object를 생성합니다. 변수로는 camera device index나 동영상 파일명을 넘겨줍니다.
      일반적으로 0 이면 Camera와 연결이 됩니다.
    * Loop를 돌면서 frame을 읽어 들입니다.
    * 읽은 frame에 대해서 변환작업을 수행한 후, 화면에 보여줍니다.
    * 영상 재생이 끝나면, VideoCapture Object를 release하고 window를 닫습니다.

아래 예제는 동영상을 읽어 grayscale로 변환 후 재생하는 예제입니다.

**Sample Code**

.. literalinclude:: videoStart.py
    :linenos:

File로 부터 영상 재생
=====================

File로 부터 동영상 재생도 Camera에서 영상 재생과 동일합니다.

**Sample Code**

.. code-block:: python
    :linenos:

    import cv2

    cap = cv2.VideoCapture('vtest.avi')

    while(cap.isOpened()):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

.. note:: 동영상 재생시에는 해당 동영상의 Codec이 설치되어 있어야 합니다.

영상 저장
=========

영상을 저장하기 위해서는 ``cv2.VideoWriter`` Object를 생성해야 합니다.

.. py:function:: cv2.VideoWriter(outputFile, fourcc, frame, size)

    영상을 저장하기 위한 Object

    :param outputFile: 저장될 파일명
    :type outputFile: str
    :param fourcc: Codec정보. cv2.VideoWriter_fourcc()
    :param frame: 초당 저장될 frame
    :type frame: float
    :param size: 저장될 사이즈(ex; 640, 480)
    :type size: list

fourcc정보는 ``cv2.VideoWriter_fourcc('M','J','P','G')`` 또는 ``cv2.VideoWriter_fourcc(*'MJPG)``
와 같이 표현할 수 있습니다. 각 OS마다 지원하는 codec 다릅니다.(Windows는 DIVX)

**Sample Code**

.. literalinclude:: videoWriter.py
    :linenos:

