.. mlKnn

========================
k-Nearest Neighbour(kNN)
========================

Goal
====

	* k-Nearest Neighbour(kNN) 알고리즘에 대해서 알 수 있다.

Theory
======

Machine Learning에는 지도학습(Supervised Learning)과 비지도학습(Unsupervised Learning)가 있습니다.

지도학습은 훈련용 Data를 만들고, 사람이 답을 알려 줍니다. 그러면 컴퓨터는 알고리즘을 이용하여 훈련용으로 제시되지 않은 Data에 대해서도 값을 찾아 냅니다.

비지도학습은 훈련용 Data에 답을 제시하고 않고 컴퓨터가 스스로 답을 찾아내는 방법입니다.

kNN은 지도학습 중 단순한 알고리즘을 이용한 방법입니다. 

.. figure:: ../../_static/28.mlKnn/image01.png
    :align: center


위 그림은 삼각형과 사각형이 있는 공간 입니다. 이 공간에 가운데 초록색 원이 있습니다. 이 원은 삼각형일까요 사각형일까요. 이것을 판단하는 방법은 여러가지가 있을 것 입니다.

먼저 가장 가까운 점은 찾는 것 입니다. 위 이미지에서 보면 빨간색이 가까이에 있으니 초록색 원은 빨간색으로 판단할 수도 있습니다. 하지만 좀더 범위를 넓혀보면 오히려 파란색 점이 많이 있습니다. 
이때 범위를 몇단계까지 넓혀 판단할 것인지에 결정하게 되는데 이때 넗히는 단계를 k값으로 정합니다.

위 그림에서 k가 3이면 빨간색 2개와 파란색 1개 이기 때문에 초록색원은 빨간색으로 판단할 수 있습니다. 만약 k값으 7로 하면 빨간색 2개와 파란색 5개가 있기 때문에 파란색으로 판단할 수 있습니다.

또한 k값에 가중치를 줄 수 있는데, 가까운곳에 더 많은 가중치를 두어서 판단할 수도 있습니다.


아래는  0 ~ 100의 좌표에 25개의 Random한 점을 생성합니다. Red는 0으로, Blue는 1로 분류를 한 후에 임의의 초록색 점을 생성하고, 그 값이 Red(0)인지 Blue(1)인지 판단하는 예제입니다. 

.. code-block:: python

	import cv2
	import numpy as np
	from matplotlib import pyplot as plt

	trainData = np.random.randint(0,100,(25,2)).astype(np.float32)

	response = np.random.randint(0,2,(25,1)).astype(np.float32)

	red = trainData[response.ravel() == 0] #red는 0 class로 분류
	plt.scatter(red[:,0],red[:,1], 80,'r','^')

	blue = trainData[response.ravel() == 1] #blue는 1 Class분류 
	plt.scatter(blue[:,0], blue[:,1], 80, 'b', 's')

	newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
	plt.scatter(newcomer[:,0], newcomer[:,1],80,'g', 'o')

	knn = cv2.ml.KNearest_create()
	knn.train(trainData, cv2.ml.ROW_SAMPLE, response)
	ret, results, neighbours, dist = knn.findNearest(newcomer, 3) #k 값을 3으로 설정

	print "result : ", results
	print "neighbours :", neighbours
	print "distance: ", dist

	plt.show()

**Result**


.. figure:: ../../_static/28.mlKnn/result01.jpg
    :align: center


>>> result :  [[ 0.]]
>>> neighbours : [[ 1.  0.  0.]]
>>> distance:  [[ 250.  293.  873.]]