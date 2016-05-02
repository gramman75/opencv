.. _imageRead:

##########
이미지 다루기
##########

이미지 읽기
===========

이번 장에서는 Image File을 읽는 방법에 대해서 알아보겠습니다.
먼저 아래와 같이 OpenCV 모듈을 Import합니다.:

.. code-block:: python

    >>> import cv2

이미지 파일을 읽기 위해서는 아래와 같이 ''cv2.imread'' 함수를 사용합니다.

    >>> img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)

이태릭체 *italic*

강조 **bold**

code ``Code``


>>> import cv2

* List

* this is
    * sub

* that is

#. number 1
#. number 2


* 들여쓰기

| this is line block
| block

* Block
This is a normal text paragraph. The next paragraph is a code sample::

    It is not processed in any way, except
    that the indentation is removed.
    It can span multiple lines.

This is a normal text paragraph again.

* Table
===== ====== ======
A     B      C
===== ====== ======
1     2      3
4     5      6
===== ====== ======

* 하이퍼 링크
| click  `Daum <http://daum.net>`_

Section 2
=========
| Section 2

SubSection
----------

.. image:: _static/copy.png

image:

    .. method:: cv2.imread(image, flag) => image

paramter::

    ========= ====== =====
    Parameter type   설명
    ========= ====== =====
    image     str    이미지 파일 경로
    flag      int    * cv2.IMREAD_COLOR : sa safd
                     * cv2.IKREAD_GRAYSCALE : asfas

Rerturn::

    * image : image 객체

Better pixel accessing and editing method :

.. code-block:: python
    :emphasize-lines: 3,5

    fname = 'lena.jpg'  # 이미지 파일경로

    color1 = cv2.imread(fname, cv2.IMREAD_COLOR) # 원본 이미지
    gray = cv2.imread(fname, cv2.IMREAD_GRAYSCALE) # Grayscale 이미지
    alpha = cv2.imread(fname, cv2.IMREAD_UNCHANGED) # alpha Chanell포함 이미지

    #각 이미지별 Show
    cv2.imshow('Original',color1)
    cv2.imshow('Gray',gray)
    cv2.imshow('alpha', alpha)


    b, g, r = cv2.split(color1)

.. literalinclude:: ../study/imageEdge.py
    :emphasize-lines: 10,11
    :linenos:
    :caption: this.py
    :name: this-py

Skipping members
----------------

.. function:: format_exception(etype, value, tb[, limit=None])

   Format the exception with a traceback.

   :param etype: exception type
   :type etype: str
   :param value: exception value
   :param tb: traceback object
   :param limit: maximum number of stack frames to show
   :type limit: integer or None
   :rtype: list of strings