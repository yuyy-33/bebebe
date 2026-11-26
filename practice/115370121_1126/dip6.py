import cv2
import numpy as np
from matplotlib import pyplot as plt

img_file="practice/115370121_1126/image/finger.jpg"

#read image
img = cv2.imread(img_file, 1)

##read image with chinese character in the path
img = cv2.imdecode(np.fromfile(img_file, dtype=np.uint8), 1)

cv2.imshow("Image - Finger Print", img)
cv2.waitKey(0)

##convert to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

##thresholding
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

##convert edges to 3 channels
thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

##show image and canny in hstack
concatenated = np.hstack((img, thresh))
cv2.imshow("Image - Finger Print (Thresholding)", concatenated)
cv2.waitKey(0)
cv2.destroyAllWindows()