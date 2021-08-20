import cv2
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
cv2.resizeWindow('Trackbars', 1200, 800)
cv2.createTrackbar('L-H', 'Trackbars', 9, 255, nothing)
cv2.createTrackbar('L-S', 'Trackbars', 32, 255, nothing)
cv2.createTrackbar('L-V', 'Trackbars', 92, 255, nothing)
cv2.createTrackbar('U-H', 'Trackbars', 23, 255, nothing)
cv2.createTrackbar('U-S', 'Trackbars', 78, 255, nothing)
cv2.createTrackbar('U-V', 'Trackbars', 175, 255, nothing)

cv2.namedWindow('Trackbars-Color')
cv2.resizeWindow('Trackbars-Color', 1200, 800)
cv2.createTrackbar('L-R', 'Trackbars-Color', 0, 255, nothing)
cv2.createTrackbar('L-G', 'Trackbars-Color', 0, 255, nothing)
cv2.createTrackbar('L-B', 'Trackbars-Color', 0, 255, nothing)
cv2.createTrackbar('U-R', 'Trackbars-Color', 255, 255, nothing)
cv2.createTrackbar('U-G', 'Trackbars-Color', 255, 255, nothing)
cv2.createTrackbar('U-B', 'Trackbars-Color', 255, 255, nothing)

font = cv2.FONT_HERSHEY_SIMPLEX

global frame
frame = cv2.imread("../Images/Ignore/lab_door_01.jpeg")

while True:
	# _, frame = cap.read()

	# gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# Door: 9 22 33 68 92 173 [8 30 30 69 94 175]

	lh = cv2.getTrackbarPos('L-H', 'Trackbars')
	uh = cv2.getTrackbarPos('U-H', 'Trackbars')
	ls = cv2.getTrackbarPos('L-S', 'Trackbars')
	us = cv2.getTrackbarPos('U-S', 'Trackbars')
	lv = cv2.getTrackbarPos('L-V', 'Trackbars')
	uv = cv2.getTrackbarPos('U-V', 'Trackbars')

	lr = cv2.getTrackbarPos('L-R', 'Trackbars-Color')
	ur = cv2.getTrackbarPos('U-R', 'Trackbars-Color')
	lg = cv2.getTrackbarPos('L-G', 'Trackbars-Color')
	ug = cv2.getTrackbarPos('U-G', 'Trackbars-Color')
	lb = cv2.getTrackbarPos('L-B', 'Trackbars-Color')
	ub = cv2.getTrackbarPos('U-B', 'Trackbars-Color')

	lower_red = np.array([lh, ls, lv])
	upper_red = np.array([uh, us, uv])
	print(lh, uh, ls, us, lv, uv)

	mask = cv2.inRange(hsv, lower_red, upper_red)

	y = np.expand_dims(mask, axis=2)
	newmask = np.concatenate((y, y, y), axis=2)

	newFrame = newmask * frame

	lower_rgb = np.array([lr,lg,lb])
	upper_rgb = np.array([ur, ug, ub])

	img = cv2.inRange(newFrame, lower_rgb, upper_rgb)

	cv2.namedWindow('Mask', cv2.WINDOW_NORMAL)
	cv2.resizeWindow('Mask', mask.shape[1]*2, mask.shape[0]*2)
	cv2.imshow('Mask', img)
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