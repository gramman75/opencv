.. imageWaterShed

====================================
Watershed 알고리즘을 이용한 이미지 분할
====================================

Goal
====

	* Watershed 알고리즘을 이용하여 이미지를 구분할 수 있다.
	* ``cv2.watershed()`` 함수에 대해서 알 수 있다.

Theory
======

이미지를 Grayscale로 변환하면 각 Pixel의 값(0 ~255)은 높고 낮음으로 구분할 수 있을 것입니다. 이것을 지형의 높낮이로 가정하고 높은 부분을 봉우리, 낮은 부분을 계곡이라고 표현할 수 있습니다.

그럼 그곳에 물을 붓는다고 생각하면 물이 섞이는 부분이 생길것입니다. 그 부분에 경계선을 만들어 서로 섞이지 않게 합니다.
바로 그 경계선을 이미지의 구분지점으로 파악하여 이미지 분할을 하게 됩니다.

아래 그림은 위 내용을 이미지로 표현한 것입니다.

 .. figure:: ../../_static/27.imageWatershed/image01.gif
    :align: center

    (출처: `CMM Webpage <http://cmm.ensmp.fr/~beucher/wtshed.html>`_ )


Code
====

이제 어떤 순서로 진행이 되는지 알아보겠습니다.

아래는 이미지 분할을 위한 원본이미지 입니다.

.. figure:: ../../_static/27.imageWatershed/image02.jpg
    :align: center

먼저 이미지를 grayscale로 변환을 합니다.

.. code-block:: python

	import cv2
	import numpy as np
	from matplotlib import pyplot as plt

	img = cv2.imread('images/water_coins.jpg')

	# binaray image로 변환
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)


다음으로 morphology를 이용하여 이미지의 노이즈나 hole을 제거 합니다.

.. code-block:: python

	#Morphology의 opening, closing을 통해서 노이즈나 Hole제거
	kernel = np.ones((3,3),np.uint8)
	opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)
	
다음은 전경과 배경을 구분을 해야 합니다. dilate를 이용하여 경계를 확장을 시킵니다. 그러면 서로 연결되지 않은 부분을 배경으로 간주 합니다. 다음은 전경을 찾아야 합니다. 전경은 opning한 결과에 거리 변환함수를 적용합니다. 거리변환 함수를 적용하면 중심으로 부터 skeloton image를 얻을 수 있습니다. 즉, 중심으로 부터 점점 옅어져가는 영상을 파악할 수 있습니다. 그 결과에 threshold를 적용하여 확실한 전경을 찾아 냅니다.

.. code-block:: python

	# dilate를 통해서 확실한 Backgroud
	sure_bg = cv2.dilate(opening,kernel,iterations=3)

	#distance transform을 적용하면 중심으로 부터 Skeleton Image를 얻을 수 있음.
	# 즉, 중심으로 부터 점점 옅어져 가는 영상.
	# 그 결과에 thresh를 이용하여 확실한 FG를 파악
	dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
	ret, sure_fg = cv2.threshold(dist_transform,0.5*dist_transform.max(),255,0)
	sure_fg = np.uint8(sure_fg)

다음은 확실하지 않은 영역을 파악합니다. 이것은 이전에 구한 배경에서 전경을 뺀 영역입니다.

.. code-block:: python

	# Background에서 Foregrand를 제외한 영역을 Unknow영역으로 파악
	unknown = cv2.subtract(sure_bg, sure_fg)		


이제 전경에 labelling작업을 합니다. labelling은 서로 이어져 있는 부분에 라벨을 붙여 서로 동일한 객체라는 것을 구분하기 위함입니다.

.. code-block:: python
	
	# FG에 Labelling작업
	ret, markers = cv2.connectedComponents(sure_fg)
	markers = markers + 1
	markers[unknown == 255] = 0


이제 watershed함수를 적용하고 그 결과값이 -1인 영역이 경계값이 됩니다. 그 부분에 붉은 색을 지정하면 동전의 경계에 붉은 원이 생긴것을 볼 수 있습니다.

.. code-block:: python
	
	# watershed를 적용하고 경계 영역에 색지정
	markers = cv2.watershed(img,markers)
	img[markers == -1] = [255,0,0]


아래는 전체 코드입니다.

.. code-block:: python

	#-*-coding:utf-8-*-
	
	import cv2
	import numpy as np
	from matplotlib import pyplot as plt


	# img = cv2.imread('images/watershed.jpg')
	img = cv2.imread('images/water_coins.jpg')

	# binaray image로 변환
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

	#Morphology의 opening, closing을 통해서 노이즈나 Hole제거
	kernel = np.ones((3,3),np.uint8)
	opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)

	# dilate를 통해서 확실한 Backgroud
	sure_bg = cv2.dilate(opening,kernel,iterations=3)

	#distance transform을 적용하면 중심으로 부터 Skeleton Image를 얻을 수 있음.
	# 즉, 중심으로 부터 점점 옅어져 가는 영상.
	# 그 결과에 thresh를 이용하여 확실한 FG를 파악
	dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
	ret, sure_fg = cv2.threshold(dist_transform,0.5*dist_transform.max(),255,0)
	sure_fg = np.uint8(sure_fg)

	# Background에서 Foregrand를 제외한 영역을 Unknow영역으로 파악
	unknown = cv2.subtract(sure_bg, sure_fg)

	# FG에 Labelling작업
	ret, markers = cv2.connectedComponents(sure_fg)
	markers = markers + 1
	markers[unknown == 255] = 0

	# watershed를 적용하고 경계 영역에 색지정
	markers = cv2.watershed(img,markers)
	img[markers == -1] = [255,0,0]


	images = [gray,thresh,sure_bg,  dist_transform, sure_fg, unknown, markers, img]
	titles = ['Gray','Binary','Sure BG','Distance','Sure FG','Unknow','Markers','Result']

	for i in xrange(len(images)):
	    plt.subplot(2,4,i+1),plt.imshow(images[i]),plt.title(titles[i]),plt.xticks([]),plt.yticks([])

	plt.show()


**Result(새탭에서 이미지를 열어 크게 보세요)**	

.. figure:: ../../_static/27.imageWatershed/result01.jpg
    :align: center



.. figure:: ../../_static/27.imageWatershed/result02.jpg
    :align: center
