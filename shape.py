import cv2
import imutils
import numpy as np

#func for getting color of click pos
def click_pos(event, x, y, flags, param):
	global mouseX , mouseY
	if event == cv2.EVENT_LBUTTONDOWN:
		mouseX, mouseY = x, y
		print(frame[y,x])

#The camera
cap = cv2.VideoCapture(0);
font = cv2.FONT_HERSHEY_SIMPLEX

# while True:
	# cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
global frame
# ret, frame = cap.read()
gray = cv2.imread("Polygons.JPG", cv2.IMREAD_GRAYSCALE)
# gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY_INV)
canny = cv2.Canny(gray,100,200)

contours, hierarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for cont in contours:
	approx = cv2.approxPolyDP(cont, 0.01*cv2.arcLength(cont, True), True)
	cv2.drawContours(gray, approx, 0, (0), 5)
	print(len(approx))

	if(len(approx)) == 3:
		x = approx.ravel()[0]
		y = approx.ravel()[1]
		cv2.putText(gray, "Triangle", (x,y), font, 0.8, (0))
	elif len(approx) == 4:
		x = approx.ravel()[0]
		y = approx.ravel()[1]
		cv2.putText(gray, "Quadrilateral", (x,y), font, 0.8, (0))
	elif len(approx) == 6:
		x = approx.ravel()[0]
		y = approx.ravel()[1]
		cv2.putText(gray, "Hexagon", (x,y), font, 0.8, (0))

# cont_img = cv2.drawContours(gray, contours, -1, (0,255,0), 	3)

cv2.namedWindow("Canny", cv2.WINDOW_NORMAL)
cv2.resizeWindow('Canny', 1024,768)
cv2.imshow('Canny', canny)
cv2.namedWindow("Contours", cv2.WINDOW_NORMAL)
cv2.resizeWindow('Contours', 1024,768)
cv2.imshow("Contours", gray)
	
	# cv2.setMouseCallback('frame', click_pos)

cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()