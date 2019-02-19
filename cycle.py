import cv2
import numpy as np
import glob

#images = glob.glob("C:\\DataBM\\Drive_BackUp\\Research\\Robotics\\AlphaPilot\\Code\\Images\\Data_Training\\Data_Training\\*.JPG")
images = glob.glob("../../Downloads/Data_Training/*.JPG")

print(len(images))
images = sorted(images)

i = 6000
while True:
	img = cv2.imread(images[i])
	img_large = cv2.resize(img, (1920, 1080))
	cv2.imshow(images[i], img_large)

	code = cv2.waitKeyEx(0)
	if code == ord('q'):
		cv2.destroyAllWindows()
		break
	elif code == ord('f'):
		print(images[i])
	elif (code == 2555904 or code == 65363 or code == ord('a')):
		i+=1
		cv2.destroyAllWindows()
	elif (code == 2424832 or code == 65361 or code == ord('f')):
		if i>1: i-=1
		cv2.destroyAllWindows()


