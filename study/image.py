import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('opencv-logo-white.png',cv2.IMREAD_COLOR)
# cv2.imshow('image',img)
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
# cv2.waitKey(0)

plt.imshow(img2)
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()