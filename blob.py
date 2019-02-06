import cv2
import numpy as np
import glob

images = glob.glob("C:\\DataBM\\Drive_BackUp\\Research\\Robotics\\AlphaPilot\\Code\\Images\\Data_Training\\Data_Training\\*.JPG")

print(len(images))

i = 100
while True:
	img = cv2.imread(images[i])

	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	canny = cv2.Canny(gray,100,200)

	# Setup SimpleBlobDetector parameters.
	params = cv2.SimpleBlobDetector_Params()
	 
	# # Change thresholds
	# params.minThreshold = 127;
	# params.maxThreshold = 255;
	 
	# Filter by Area.
	params.filterByArea = True
	params.minArea = 200
	 
	# Filter by Circularity
	# params.filterByCircularity = True
	# params.minCircularity = 0.3
	 
	# # Filter by Convexity
	# params.filterByConvexity = True
	# params.minConvexity = 0.87
	 
	# # Filter by Inertia
	# params.filterByInertia = True
	# params.minInertiaRatio = 0.01

	# Set up the detector with default parameters.
	detector = cv2.SimpleBlobDetector_create(params)

	 
	# Detect blobs.
	keypoints = detector.detect(canny)
	 
	# Draw detected blobs as red circles.
	# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
	im_with_keypoints = cv2.drawKeypoints(canny, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	 
	# Show keypoints
	cv2.imshow("Keypoints", im_with_keypoints)

	cv2.imshow(images[i], img)
	cv2.imshow('Canny', canny)

	code = cv2.waitKeyEx(0)
	print(code)
	if code == ord('q'):
		cv2.destroyAllWindows()
		break
	elif code == 2555904:
		i+=1
		print("Going Right")
		cv2.destroyAllWindows()
	elif code == 2424832:
		if i>1: i-=1
		print("Going Left")
		cv2.destroyAllWindows()

