import cv2
import numpy as np 

img = cv2.imread('copy.png',cv2.IMREAD_COLOR)
# blank = np.zeros((100,200,3), np.uint8)
# obj = img[100:200, 200:400]
# img[300:400, 500:700] = obj
# obj = blank

img[:,:,:] = 0

cv2.imshow('image',img)

cv2.waitKey(0)

