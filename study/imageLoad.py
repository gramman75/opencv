import cv2

imgs = ['capture 0.png','capture 1.png','capture 2.png']

for i in range(0,len(imgs)):

	if (i+1) == len(imgs):
		break;



	prevImg = cv2.imread(imgs[i])
	nextImg = cv2.imread(imgs[i+1])

	for j in range(1,11):
		n = j * 0.1
		b = 1-n
		
		dst = cv2.addWeighted(prevImg,b,nextImg,n,0)
		cv2.imshow('dst',dst)		
		cv2.waitKey(300)



cv2.destroyAllWindows()

