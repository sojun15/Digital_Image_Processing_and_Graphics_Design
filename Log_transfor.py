import cv2
import numpy as np

image = cv2.imread('sun.jpg',1)
float_value = np.float16(image)
image = np.log10(1+float_value)
image2 = np.int8(image)

# image2 = cv2.normalize(image2,None,0,255,cv2.NORM_MINMAX)
image2 = np.clip(image2, 0, 255)
print(image2)
cv2.imshow('Image',image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
