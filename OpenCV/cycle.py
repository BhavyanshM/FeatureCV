import cv2
import numpy as np
import glob
import sys
import json

#images = glob.glob("C:\\DataBM\\Drive_BackUp\\Research\\Robotics\\AlphaPilot\\Code\\Images\\Data_Training\\Data_Training\\*.JPG")
print(sys.argv[1])
images = glob.glob(sys.argv[1])


print((images))
images = sorted(images)

with open(sys.argv[2],'r') as f:
    pred_data = json.load(f)

i = 0
while True:
	img = cv2.imread(images[i])
	# img_large = cv2.resize(img, (1920, 1080))
	imgFileName = images[i].replace("../../Downloads/Datasets/Testing/", "")
	box = np.array(pred_data[imgFileName])
	if box.shape[0] == 1:
		print("HERE:", box[0])
		x_ul, y_ul, x_ur, y_ur, x_lr, y_lr, x_ll, y_ll = int(box[0][0]), int(box[0][1]), int(box[0][2]), int(box[0][3]), int(box[0][4]), int(box[0][5]), int(box[0][6]), int(box[0][7]) 
		cv2.circle(img,(int(x_ul), int(y_ul)), 20, (0,0,255), -1)
		cv2.circle(img,(int(x_ur), int(y_ur)), 20, (0,0,255), -1)
		cv2.circle(img,(int(x_lr), int(y_lr)), 20, (0,0,255), -1)
		cv2.circle(img,(int(x_ll), int(y_ll)), 20, (0,0,255), -1)
	else:
		print("EMPTY")
		# cv2.putText("NO", text=fps, org=(3, 15), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.50, color=(255, 0, 0), thickness=2)
	cv2.imshow(images[i], img)

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


