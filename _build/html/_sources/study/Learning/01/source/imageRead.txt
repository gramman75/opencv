.. _imageRead:

**********
Image Read
**********

test
====

이번 장에서는 Image File을 읽는 방법에 대해서 알아보겠습니다.
먼저 아래와 같이 OpenCV 모듈을 Import합니다.

::

    import cv2
    import numpy as np

이태릭체 *italic*

강조 **bold**

code ``Code``

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

Args:
    path (str): The path of the file to wrap
    field_storage (FileStorage): The :class:`FileStorage` instance to wrap
    temporary (bool): Whether or not to delete the file when the File
       instance is destructed

Returns:
    BufferedFileStorage: A buffered writable file descriptor


code:
    >>> a
    >>> b



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

.. literalinclude:: imageRead.py
    :emphasize-lines: 10,11
    :linenos:
    :caption: this.py
    :name: this-py

imdecode
--------
Reads an image from a buffer in memory.

.. ocv:function:: Mat imdecode( InputArray buf,  int flags )

.. ocv:function:: Mat imdecode( InputArray buf,  int flags, Mat* dst )

.. ocv:cfunction:: IplImage* cvDecodeImage( const CvMat* buf, int iscolor=CV_LOAD_IMAGE_COLOR)

.. ocv:cfunction:: CvMat* cvDecodeImageM( const CvMat* buf, int iscolor=CV_LOAD_IMAGE_COLOR)

.. ocv:pyfunction:: cv2.imdecode(buf, flags) -> retval

    :param buf: Input array or vector of bytes.

    :param flags: The same flags as in :ocv:func:`imread` .

    :param dst: The optional output placeholder for the decoded matrix. It can save the image reallocations when the function is called repeatedly for images of the same size.