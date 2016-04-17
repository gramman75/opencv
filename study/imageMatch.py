#-*-coding:utf-8-*-
"""
#Match
    . 
"""
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('capture 0.png',1)
# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template = cv2.imread('cap_template.png',1)
w,h = template.shape[::-1]

res = cv2.matchTemplate(img,template,cv2.TM_SQDIFF)
min_val,max_val,min_loc, max_loc = cv2.minMaxLoc(res)
top_left = min_loc #max_loc
bottom_right = (top_left[0]+w,top_left[1]+h)
cv2.rectangle(img,top_left,bottom_right,255,5)

plt.subplot(121),plt.imshow(img),plt.yticks([]),plt.xticks([])
plt.subplot(122),plt.imshow(template)
plt.show()