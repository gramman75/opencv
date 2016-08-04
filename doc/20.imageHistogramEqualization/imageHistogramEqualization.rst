.. imageHistograms

=================
히스토그램 균일화
=================

Goal
====
    * 히스토그램 균일화(Histogram Equalization)에 대해서 알 수 있고, 이것을 이용하여 이미지의 contrast를 향상시킬 수 있다.

Theory
======

이미지의 히스토그램이 특정영역에 너무 집중되어 있으면 contrast가 낮아 좋은 이미지라고 할 수 없습니다.
전체 영역에 골고루 분포가 되어 있을 때 좋은 이미지라고 할 수 있습니다. 아래 히스토그램을 보면 좌측 처럼 특정 영역에
집중되어 있는 분포를 오른쪽 처럼 골고루 분포하도록 하는 작업을 Histogram Equalization 이라고 합니다.

.. figure:: ../../_static/20.imageHistogramEqualization/image01.png
    :align: center

이론적인 방법은 이미지의 각 픽셀의 cumulative distribution function(cdf)값을 구하고 Histogram Equalization 공식에 대입하여
0 ~ 255 사이의 값으로 변환을 하게 됩니다. 이렇게 새롭게 구해진 값으로 이미지를 표현하면 균일화된 이미지를 얻을 수 있습니다.

자세한 내용은 `Wikipedia <https://en.wikipedia.org/wiki/Histogram_equalization>`_ 를 참고하시기 바랍니다.

그럼 우선 Numpy를 이용하여 균일화 작업을 하는 예제입니다.







