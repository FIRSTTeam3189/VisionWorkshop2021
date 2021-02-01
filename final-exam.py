import cv2
import numpy as np

img = cv2.imread('test-img.jpg')
img = cv2.resize(img, (1280, 960))

# Add your image processing here

cv2.imshow('image', img)

cv2.waitKey()
cv2.destroyAllWindows()
