import cv2
import numpy as np
img1 = cv2.imread('capture 0.png')
img2 = cv2.imread('capture 1.png')
img3 = cv2.imread('capture 2.png')

dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

dst = cv2.addWeighted(dst,0.7,img3,0.3,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

