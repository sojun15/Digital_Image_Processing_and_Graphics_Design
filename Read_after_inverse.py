import cv2
import numpy as np 

image = cv2.imread('sun.jpg',)
image = 255 - image 

cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(image)