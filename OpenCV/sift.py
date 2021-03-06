import cv2
import numpy as np
import glob

images = glob.glob("../../Downloads/Data_Training/*.JPG")

print(len(images))

i = 0
while True:
	img = cv2.imread(images[i], 0)

	sift = cv2.xfeatures2d.SIFT_create()
	surf = cv2.xfeatures2d.SURF_create()
	orb = cv2.ORB_create()

	feature = sift
	keypoints, descriptors = feature.detectAndCompute(img, None)
	img = cv2.drawKeypoints(img, keypoints, None)

	cv2.imshow("Result", img)
	# cv2.imshow("Image", img)
	# cv2.imshow("Gate", gate)

	code = cv2.waitKeyEx(0)
	print(code)
	if code == ord('q'):
		cv2.destroyAllWindows()
		break
	elif (code == 2555904 or code == 65363 or code == ord('a')):
		i+=1
		print("Going Right")
		cv2.destroyAllWindows()
	elif (code == 2424832 or code == 65361 or code == ord('f')):
		if i>1: i-=1
		print("Going Left")
		cv2.destroyAllWindows()

