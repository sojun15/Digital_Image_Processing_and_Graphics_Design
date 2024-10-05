import cv2
import numpy as np

image = cv2.imread('sun.jpg',1)

c = 5
gamma = .5
print(image)
print('gap between two array!')

for x in range(image.shape[0]):
    for y in range(image.shape[1]):
        ftv = np.float16(image[x][y])
        ftv = c *  (ftv ** gamma)
        image[x][y] = np.uint8(ftv)

print(image)
cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
