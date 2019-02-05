import cv2
import numpy as np

img = cv2.imread("C:\\DataBM\\Drive_BackUp\\Research\\Robotics\\AlphaPilot\\Code\\Images\\Data_Training\\Data_Training\\IMG_0006.JPG")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

cv2.imshow('Image', img)
cv2.imshow('Result', dst)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]
cv2.waitKey(0)
cv2.destroyAllWindows()
