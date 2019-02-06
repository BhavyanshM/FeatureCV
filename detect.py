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
	# find Harris corners
	gray = np.float32(gray)
	dst = cv2.cornerHarris(gray,2,3,0.04)
	dst = cv2.dilate(dst,None)
	ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
	dst = np.uint8(dst)

	# find centroids
	ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

	# define the criteria to stop and refine the corners
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
	corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

	# Now draw them
	res = np.hstack((centroids,corners))
	res = np.int0(res)
	img[res[:,1],res[:,0]]=[0,0,255]
	img[res[:,3],res[:,2]] = [0,255,0]

	cv2.imshow(images[i], img)
	cv2.imshow('Canny', canny)
	cv2.imshow('Harris', dst)

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

