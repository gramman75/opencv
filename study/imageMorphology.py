#-*- coding:utf-8 -*-
"""
# 이미지를 Segmentation하여 단순화/제거/보정을 통해서 
  형태를 파악하는 목적 
# Binary/GrayScale에 적용 가능. 방법은 동일하나 결과물은 다름.
# Operation
  . Dilation(팽창) & Erosion(침식) 방법 
  . Morphology기법은 위 2가지 방법을 조합하여 처리됨. 
# structuring element
  . 원본 이미지에 적용하는 kernel
  . 중심을 원점으로 사용하고, 원점도 변경할 수 있음. 
  . 꽉찬 사각형, 타원형, 십자형을 많이 사용
"""

"""
# Dilation
  . 대상을 확장한 후 작은 구멍을 채우는 방법 
  . 각 pixel을 대상으로 structuring element를 적용함.
  . 대상 pixel에 SE를 or연산을 수행함.
  . 대상이 확장이 된 결과가 나옴.
  . 결과적으로 경계가 부드러워지고, 구멍들이 메꿔지는 효과가 나옴 
"""

"""
# Erosion
   . 각 pixel에 SE를 적용하여 하나라도 0이 있으면 대상 pixel을 제거함.
   . 작은 Object는 제거가 됨 
"""

"""
# Opening
   . Erosion적용 후 Dilation을 적용.
   . 작은 Object 제거나 돌기 제거에 도움. 
# Closing
   . Diation적용 후 Erosion적용.
   . 전체적인 윤곽 파악에 도움. 
"""

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

dotImage = cv2.imread('dot_image.png')
holeImage = cv2.imread('hole_image.png')

# kernel = np.ones((5,5),np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

erosion = cv2.erode(dotImage,kernel,iterations = 1)
dilation = cv2.dilate(holeImage,kernel,iterations = 1)

opening = cv2.morphologyEx(dotImage, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(holeImage, cv2.MORPH_CLOSE,kernel)

images =[dotImage, erosion, opening, holeImage, dilation, closing]
titles =['Dot Image','Erosion','Opening','Hole Image', 'Dilation','Closing']

for i in xrange(6):
	plt.subplot(2,3,i+1),plt.imshow(images[i]),plt.title(titles[i])
	plt.xticks([]),plt.yticks([])

plt.show()	