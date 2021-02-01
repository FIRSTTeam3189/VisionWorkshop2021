import cv2
import numpy as np

img = cv2.imread('test-img.jpg')
img = cv2.resize(img, (1280, 960))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_green = np.array([40, 150, 50])
upper_green = np.array([60, 255, 180])

mask = cv2.inRange(hsv, lower_green, upper_green)
blurred = blur = cv2.GaussianBlur(mask, (5, 5), 0)
element = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
filtered = cv2.morphologyEx(blurred, cv2.MORPH_OPEN, element)
contours, hierarchy = cv2.findContours(filtered, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

rect = cv2.minAreaRect(max(contours, key=lambda x: cv2.contourArea(x)))
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

cv2.imshow('image', img)
cv2.imshow('mask', mask)
cv2.imshow('blurred', blurred)
cv2.imshow('filtered', filtered)

cv2.waitKey()

cv2.destroyAllWindows()
