import cv2
import numpy as np
from matplotlib import pyplot as plt

img_file="practice/115370121_1126/image/tiger.jpeg"
#read image
img = cv2.imread(img_file, 1) ##1:color, 0:gray, -1:unchanged

##read image with chinese character in the path 
img=cv2.imdecode(np.fromfile(img_file, dtype=np.uint8),1)

##show histogram of a gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
plt.plot(hist)
cv2.imshow("image", img)
plt.show()

##show image
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
