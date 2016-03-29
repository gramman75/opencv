import cv2

img1 = cv2.imread('capture 0.png')
img2 = cv2.imread('images.png')

rows, cols, channels = img2.shape
roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 1,10,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

img2_fg = cv2.bitwise_and(img2,img2,mask=mask)

dst = cv2.add(img1_bg, img2_fg)

img1[0:rows, 0:cols] = dst

cv2.imshow('image',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()