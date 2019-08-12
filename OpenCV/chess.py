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
cap = cv2.VideoCapture(1);

# while True:
	# cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
global gray
# ret, frame = cap.read()
# gray = cv2.imread("Chess.png", cv2.IMREAD_GRAYSCALE)
# gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

return_val, gray = cap.read()

# Find the chess board corners
# ret, corners = cv2.findChessboardCorners(gray, (6,7),None)

# # If found, add object points, image points (after refining them)
# if ret == True:

#     # Draw and display the corners
#     gray = cv2.drawChessboardCorners(gray, (6,7), corners,ret)

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image', 1024,768)
cv2.imshow("Image", gray)
	
	# cv2.setMouseCallback('frame', click_pos)

cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()