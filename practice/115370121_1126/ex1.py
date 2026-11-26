import cv2
import numpy as np
from matplotlib import pyplot as plt

img_file="practice/115370121_1126/image/tiger.jpeg"
#read image
img = cv2.imread(img_file, 1) ##1:color, 0:gray, -1:unchanged

##read image with chinese character in the path 
img=cv2.imdecode(np.fromfile(img_file, dtype=np.uint8),1)
print(img.shape)

##convert to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) ##cvt:convert, BGR:Blue Green Red

##negative image
negative = cv2.bitwise_not(gray) ##bitwise_not:invert the pixel value

##color negative image
negative_color = 255 - img

##save image
cv2.imwrite("practice/115370121_1126/image/tiger_gray.jpeg", gray)
cv2.imwrite("practice/115370121_1126/image/tiger_negative.jpeg", negative)
cv2.imwrite("practice/115370121_1126/image/tiger_negative_color.jpeg", negative_color)

##display image
cv2.imshow("image", img)
cv2.imshow("gray", gray)
cv2.imshow("negative", negative)
cv2.imshow("negative_color", negative_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

