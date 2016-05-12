#-*- coding:utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/perspective.jpg')
rows, cols, ch = img.shape

pts1 = np.float32([[455,725],[1698,183],[488,785],[1685,1280]])
# pts1 = np.float32([[725,455],[183,1698],[785,488],[1280,1685]])
pts2 = np.float32([[0,0],[1000,0],[0,1000],[1000,1000]])

# pts1의 좌표에 표시. Affine 변환 후 이동 점 확인.
# cv2.circle(img, (200,100), 10, (255,0,0),-1)
# cv2.circle(img, (400,100), 10, (0,255,0),-1)
# cv2.circle(img, (200,200), 10, (0,0,255),-1)

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (1000,1000))

plt.subplot(121),plt.imshow(img),plt.title('image')
plt.subplot(122),plt.imshow(dst),plt.title('Affine')
plt.show()



