import cv2
import numpy as np

img = cv2.imread('hough_images.jpg')
edges = cv2.Canny(img,50,200,apertureSize = 3)
gray = cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)
minLineLength = 30
maxLineGap = 0

lines = cv2.HoughLinesP(edges,1,np.pi/360,100,minLineLength,maxLineGap)
for i in xrange(len(lines)):
    for x1,y1,x2,y2 in lines[i]:
        cv2.line(gray,(x1,y1),(x2,y2),(0,0,255),2)
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),3)


cv2.imshow('img1',img)
cv2.imshow('img',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()




