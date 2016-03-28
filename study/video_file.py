import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')
i=0

while(cap.isOpened()):
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame', gray)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	elif cv2.waitKey(0) == ord('s'):
		cv2.imwrite('capture {0}.png'.format(str(i)),gray)
		i+=1

cap.release()
cv2.destroyAllWindows()
