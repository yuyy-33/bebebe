import cv2
import numpy as np
from matplotlib import pyplot as plt

img_file="practice/115370121_1126/image/tiger.jpeg"
#read image
img = cv2.imread(img_file, 1) ##1:color, 0:gray, -1:unchanged

##read image with chinese character in the path 
img=cv2.imdecode(np.fromfile(img_file, dtype=np.uint8),1)
print(img.shape)

print(img[50,100]) ##print the pixel value at (50,100) in BGR format
img[50,100]=[0,255,0] ##change the pixel value at (50,100) to green (BGR format)  
img[51,100]=[0,255,0]
img[52,100]=[0,255,0]
img[53,100]=[0,255,0]
img[54,100]=[0,255,0]
img[55,100]=[0,255,0]
img[56,100]=[0,255,0]
img[57,100]=[0,255,0]
img[58,100]=[0,0,255]


cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()