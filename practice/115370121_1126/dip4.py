import cv2
import numpy as np
from matplotlib import pyplot as plt

img_file="practice/115370121_1126/image/tiger.jpeg"

#read image
img = cv2.imread(img_file, 1)

##read image with chinese character in the path
img=cv2.imdecode(np.fromfile(img_file, dtype=np.uint8),1)

##show image
cv2.imshow("image", img)

##新增：讓圖片越來越模糊
for i in range(1, 102, 2):
    blur = cv2.GaussianBlur(img, (5+2*i, 5+2*i), 0)
    cv2.imshow("blur", blur)
    cv2.waitKey(100)

cv2.waitKey(0)
cv2.destroyAllWindows()