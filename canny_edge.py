import cv2
import numpy as np
import glob

#images = glob.glob("C:\\DataBM\\Drive_BackUp\\Research\\Robotics\\AlphaPilot\\Code\\Images\\Data_Training\\Data_Training\\*.JPG")
images = glob.glob("../../Downloads/Data_Training/*.JPG")

print(len(images))

i = 100
while True:
	img = cv2.imread(images[i])

	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)	# find Harris corners
	dst = cv2.Canny(gray,100,200)

	cv2.imshow(images[i], img)
	cv2.imshow('Result', dst)

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

