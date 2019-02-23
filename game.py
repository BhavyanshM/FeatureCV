import cv2
import imutils
import numpy as np

#func for getting color of click pos
def click_pos(event, x, y, flags, param):
	global mouseX , mouseY
	if event == cv2.EVENT_LBUTTONDOWN:
		mouseX, mouseY = x, y
		print(frame[y,x])

def detect_chess_corners(gray):
	ret, corners = cv2.findChessboardCorners(gray, (6,7),None)
	# If found, add object points, image points (after refining them)
	if ret == True:
		gray = cv2.drawChessboardCorners(gray, (6,7), corners,ret)

	return ret, corners

#The camera
cap = cv2.VideoCapture(0);

while True:
	# cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
	global frame
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
	success, chess = detect_chess_corners(gray)

	# image, contours, hierarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	# cont = cv2.drawContours(frame, contours, -1, (0,255,0), 3)

	# cv2.imshow('Canny', canny)
	# cv2.imshow('Frame', frame)
	if success:
		cv2.imshow('Chess', chess)
	else:
		cv2.imshow('Gray', gray)
	# cv2.imshow("Contours", cont)S
	
	# cv2.setMouseCallback('frame', click_pos)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
