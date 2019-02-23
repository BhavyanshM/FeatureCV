import numpy as np
import cv2
import time
from math import sin, cos, tan, ceil


def plotter(x, y, shift_x, shift_y, scale_x, scale_y, phase_x, phase_y, radius, color):
	del_x = shift_x + int(scale_x*(sin(cos(x+phase_x))))
	del_y = shift_y + int(scale_y*tan(cos(y+phase_y)))

	print(del_x, del_y)

	cv2.circle(img,(del_x, del_y), radius, color, -1)

#Create a black image
img = np.zeros((512,512,3), np.uint8)
x, y = 0,0
inc_x, inc_y = 0.01, 0.01


# Draw a diagonal blue line with thickness of 5 px
while True:
	x += inc_x
	y += inc_y
	plotter(x, y, 250, 200, 100, 100, 0, 10, 10, (0,0,255))	

	# a += 0.1
	# b += 0.1
	# del_a = 180 + int(200*(sin(x)))
	# del_b = 100 + int(100*cos(y))

	# print(del_x, del_y)

	# cv2.circle(img,(del_x, del_y), 10, (255,255,255), -1)

	# cv2.circle(img,(200, 200), 63, (0,0,255), -1)
	cv2.namedWindow("Draw", cv2.WINDOW_NORMAL)
	cv2.resizeWindow('Draw', 1024,768)
	cv2.imshow('Draw', img)

	time.sleep(0.01)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()