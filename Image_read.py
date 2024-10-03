import cv2
import numpy as np 

image = cv2.imread('pic.jpg',0)

cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(image)