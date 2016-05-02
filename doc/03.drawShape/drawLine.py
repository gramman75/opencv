import numpy as np
import cv2

img = np.zeros((512, 512), np.uint8)
img = cv2.line(img, (200, 0), (100, 511), (255, 0, 0), 5)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()