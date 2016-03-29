import cv2
import numpy as np 

e1 = cv2.getTickCount()

img = cv2.imread('copy1.png')

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_blue = np.array([110,0,0])
upper_blue = np.array([130,255,255])

mask = cv2.inRange(hsv,lower_blue,upper_blue)

res = cv2.bitwise_and(img,img,mask=mask)

cv2.imshow('image',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)

e2 = cv2.getTickCount()

t = (e2-e1) / cv2.getTickFrequency()

print t

cv2.waitKey(0)

cv2.destroyAllWindows()