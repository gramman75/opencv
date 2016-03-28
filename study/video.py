import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0)
i = 0

print 'width: {0}, height: {1}'.format(cap.get(3),cap.get(4))
cap.set(3,320)
cap.set(4,240)
while(True):
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow('frame', gray)

	if cv2.waitKey(0) & 0xFF == ord('q'):		
		break
	elif cv2.waitKey(0) == ord('s'):
		cv2.imwrite('capture'+ str(i)+'.png', gray)
		i = i+1


cap.release()
cv2.destroyAllWindows()