import cv2
import numpy as np
from matplotlib import pyplot as plt

img_file="practice/115370121_1126/image/tiger.jpeg"

#read image
img = cv2.imread(img_file, 1)

##read image with chinese character in the path
img=cv2.imdecode(np.fromfile(img_file, dtype=np.uint8),1)

##resize image
# img=cv2.resize(img, (800,600))
img=cv2.resize(img, None, fx=0.5, fy=0.5) ##resize by scale factor

###show image
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()