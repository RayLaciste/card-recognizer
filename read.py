import cv2 as cv

img = cv.imread('images/sv2_en_001.jpg')

cv.imshow('Card', img)

cv.waitKey(0)