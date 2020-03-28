import cv2
import numpy as np


img = cv2.imread("./ChessBoard.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# find Harris corners
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)

# find centroids
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

# Now draw them
res = np.hstack((centroids,corners))
res = np.int0(res)
print(centroids.shape, corners.shape)

for c in centroids:
	x,y = (int(c[0]),int(c[1]))
	img = cv2.circle(img, (x,y), 4, (0,255,255), -1)



cv2.imshow("Harris Corners", img)
# cv2.imshow('Result', dst)

code = cv2.waitKeyEx(0)
cv2.destroyAllWindows()

