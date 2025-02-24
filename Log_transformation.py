import cv2
import numpy as np

image = cv2.imread('sun.jpg', 1) 
c = int(input('enter the value of c:'))

for row in range(image.shape[0]):
    for col in range(image.shape[1]): 
        img = np.float16(image[row, col])
        img = c * np.log10(1+img)
        image[row,col] = np.uint8(img)

image = np.clip(image, 0, 255)
print(image)
cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()