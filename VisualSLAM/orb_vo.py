import cv2
import numpy as np
import glob

cap = cv2.VideoCapture(1)

i = 0
width, height = 1024, 768

while True:
	ret, img = cap.read()

	orb = cv2.ORB_create(nfeatures=150)

	feature = orb

	keypoints, descriptors = feature.detectAndCompute(img, None)
	img = cv2.drawKeypoints(img, keypoints, None)

	cv2.namedWindow("Features", cv2.WINDOW_NORMAL)
	cv2.resizeWindow('Features', width,height)
	cv2.imshow('Features', img)
	# cv2.imshow("Image", img)
	# cv2.imshow("Gate", gate)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		cap.release()
		cv2.destroyAllWindows()
		break

