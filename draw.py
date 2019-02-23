import numpy as np
import cv2
import time
import sys
from math import sin, cos, tan, ceil, floor, radians


def plotter(x, y, pattern):
	del_x = pattern['shift_x'] + int(pattern['scale_x']*sin(x+pattern['phase_x']))
	del_y = pattern['shift_y'] + int(pattern['scale_y']*cos(y+pattern['phase_y']))

	# print(del_x, del_y)

	cv2.circle(img,(del_x, del_y), pattern['radius'], pattern['color'], -1)

def polygon_plotter(point_x, point_y, angle):
	cv2.circle(img, (point_x, point_y), 5, (0,0,255), -1)

#Create a black image
img = np.zeros((800,800,3), np.uint8)
x, y = 0,0
point_x, point_y = 200, 100
rem = 0
angle = 0
inc_x, inc_y = 0.01, 0.01
if(len(sys.argv) >= 3):
	n_sides = int(sys.argv[2])
dist = 3


# Draw a diagonal blue line with thickness of 5 px
while True:
	x += inc_x
	y += inc_y

	# print(x, y)
	if(sys.argv[1] == 'conics'):
		conics = {
			"shift_x":400,
			"shift_y":400,
			"scale_x":200,
			"scale_y":200,
			"phase_x":0,
			"phase_y":0,
			"radius": int(sys.argv[2]) or 50,
			"color":(0, 0, 255)
		}
		plotter(x, y, 
			pattern = conics
		)	
	if(sys.argv[1] == 'magic'):
		magic = {
			"shift_x":250,
			"shift_y":200,
			"scale_x":abs(400*(cos(y))),
			"scale_y":abs(400*(sin(x))),
			"phase_x":abs(10*x),
			"phase_y":abs(10*sin(x*y)),
			"radius": (50 + int(45*(sin(x)))),
			"color":((255*sin(y*2)),(255*sin(x-y)),(255*sin(x*x)))
		}
		
		plotter(x, y, 
			pattern = magic
		)

	if(sys.argv[1] == 'polygon'):
		rem += 1
		# print(angle)
		if((rem % 50) == 0):
			angle += (360/n_sides)
		if angle == 360 or angle > 360:
			angle = 0
			dist = 0

		point_x = point_x + int(dist*cos(radians(angle)))
		point_y = point_y + int(dist*sin(radians(angle)))
		polygon_plotter(point_x, point_y, 
			angle = angle
		)

	# a += 0.1
	# b += 0.1
	# del_a = 180 + int(200*(sin(x)))
	# del_b = 100 + int(100*cos(y))

	# print(del_x, del_y)

	# cv2.circle(img,(del_x, del_y), 10, (255,255,255), -1)

	# cv2.circle(img,(200, 200), 63, (0,0,255), -1)
	cv2.namedWindow("Draw", cv2.WINDOW_NORMAL)
	cv2.resizeWindow('Draw', 600,600)
	cv2.imshow('Draw', img)

	time.sleep(0.0001)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()