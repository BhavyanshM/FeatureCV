import cv2
import imutils
import numpy as np

#func for getting color of click pos
def click_pos(event, x, y, flags, param):
	global mouseX , mouseY
	if event == cv2.EVENT_LBUTTONDOWN:
		mouseX, mouseY = x, y
		print(frame[y,x])

def nothing(x):
	pass

#The camera
cap = cv2.VideoCapture(0);

cv2.namedWindow('Trackbars')
cv2.createTrackbar('L-H', 'Trackbars', 0, 180, nothing)
cv2.createTrackbar('L-S', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('L-V', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('U-H', 'Trackbars', 180, 180, nothing)
cv2.createTrackbar('U-S', 'Trackbars', 255, 255, nothing)
cv2.createTrackbar('U-V', 'Trackbars', 255, 255, nothing)

font = cv2.FONT_HERSHEY_SIMPLEX

# while True:
	# cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
global frame
# ret, frame = cap.read()

width = 640
height = 480

while True:
	_, frame = cap.read()

	# gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	lh = cv2.getTrackbarPos('L-H', 'Trackbars')
	uh = cv2.getTrackbarPos('U-H', 'Trackbars')
	ls = cv2.getTrackbarPos('L-S', 'Trackbars')
	us = cv2.getTrackbarPos('U-S', 'Trackbars')
	lv = cv2.getTrackbarPos('L-V', 'Trackbars')
	uv = cv2.getTrackbarPos('U-V', 'Trackbars')

	lower_red = np.array([lh, ls, lv])
	upper_red = np.array([uh, us, uv])



	mask = cv2.inRange(hsv, lower_red, upper_red)
	cv2.line(frame, (int(width/3), 0), (int(width/3), height), (255, 255, 0), 5, 1)
	cv2.line(frame, (int(2*width/3), 0), (int(2*width/3), height), (255, 255, 0), 5, 1)
	cv2.line(frame, (0, int(height/3)), (width, int(height/3)), (255, 255, 0), 5, 1)
	cv2.line(frame, (0, int(2*height/3)), (width, int(2*height/3)), (255, 255, 0), 5, 1)

	print(frame.shape)

	cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
	cv2.resizeWindow('Frame', width,height)
	cv2.imshow('Frame', frame)

	# cv2.namedWindow("Mask", cv2.WINDOW_NORMAL)
	# cv2.resizeWindow('Mask', width,height)
	# cv2.imshow('Mask', mask)

	# gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	# _, thresh = cv2.threshold(hsv, 250, 255, cv2.THRESH_BINARY_INV)
	# canny = cv2.Canny(hsv,100,200)



	# contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

	# for cont in contours:
	# 	approx = cv2.approxPolyDP(cont, 0.01*cv2.arcLength(cont, True), True)
	# 	cv2.drawContours(frame, approx, 0, (0), 5)
	# 	print(len(approx))

	# 	# if(len(approx)) == 3:
	# 	# 	x = approx.ravel()[0]
	# 	# 	y = approx.ravel()[1]
	# 	# 	cv2.putText(gray, "Triangle", (x,y), font, 0.8, (0))
	# 	if len(approx) == 4:
	# 		x = approx.ravel()[0]
	# 		y = approx.ravel()[1]
	# 		cv2.putText(gray, "Square", (x,y), font, 0.8, (0))
		# elif len(approx) == 6:
		# 	x = approx.ravel()[0]
		# 	y = approx.ravel()[1]
		# 	cv2.putText(gray, "Hexagon", (x,y), font, 0.8, (0))

	# cont_img = cv2.drawContours(gray, contours, -1, (0,255,0), 	3)

	# cv2.namedWindow("Canny", cv2.WINDOW_NORMAL)
	# cv2.resizeWindow('Canny', 1024,768)
	# cv2.imshow('Canny', canny)
	# cv2.namedWindow("Contours", cv2.WINDOW_NORMAL)
	# cv2.resizeWindow('Contours', 800,600)
	# cv2.imshow("Contours", frame)
		
		# cv2.setMouseCallback('frame', click_pos)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()