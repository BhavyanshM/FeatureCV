import cv2
import numpy as np

img = cv2.imread('../Images/Polygons.JPG')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,120)
for line in lines:
	rho,theta = line[0]
	a = np.cos(theta)
	b = np.sin(theta)
	x0 = a*rho
	y0 = b*rho
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))

	cv2.line(img,(x1,y1),(x2,y2),(0,0,0),2)

	print(rho,theta/np.pi*180)


print(img.shape, len(lines))

cv2.namedWindow("HoughLines", cv2.WINDOW_NORMAL)
cv2.resizeWindow("HoughLines", (1000,1200))
cv2.imshow('HoughLines',img)
cv2.imshow("Canny Edges", edges)
cv2.waitKey(0)