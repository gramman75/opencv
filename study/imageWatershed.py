#-*-coding:utf-8-*-
"""
# 영역 분할
    .Watershed
      - 이미지의 pixel값을 지형의 높낮이로 가정하고, 물을 채웠을 때, 웅덩이와 윤곽선이 나타나는 것처럼.
        픽셀의 고저 값을 통해서 봉우리와 골짜기로 가정하고 영역을 Segmentation함.
      - Edge-base의 분할은 노이즈에 민감하고 폐곡석을 얻기가 어렵워 Region-based방식으로 처리함.
      - 단 경계가 번지는 단점이 있음.
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('images/watershed.jpg')
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


images = [img,gray,thresh,sure_bg,  dist_transform, sure_fg, unknown, markers]
titles = ['Original','Gray','Binary','Sure BG','Distance','Sure FG','Unknow','Markers']

for i in xrange(len(images)):
    plt.subplot(2,4,i+1),plt.imshow(images[i]),plt.title(titles[i]),plt.xticks([]),plt.yticks([])

plt.show()

