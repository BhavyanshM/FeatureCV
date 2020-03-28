import numpy as np
import cv2


image = cv2.imread("./Chess.JPG")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

img = np.array(image)
print(img.shape)

cv2.imshow("Harris Corners", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
