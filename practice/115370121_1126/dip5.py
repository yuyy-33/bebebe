import cv2
import numpy as np
from matplotlib import pyplot as plt

img_file="practice/115370121_1126/image/tiger.jpeg"

#read image
img = cv2.imread(img_file, 1)

##read image with chinese character in the path
img=cv2.imdecode(np.fromfile(img_file, dtype=np.uint8),1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

##canny edge detection
edges = cv2.Canny(gray, 120, 120) ##120:lower threshold, 120:upper threshold

##convert edges to 3 channels
edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

##show image and canny in hstack
concatenated = np.hstack((img, edges))
cv2.imshow("image and canny", concatenated)
cv2.waitKey(0)
cv2.destroyAllWindows()