import cv2 as cv

img = cv.imread('images/sv2_en_001.jpg')
# cv.imshow('Card', img)

def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img_resized = rescaleFrame(img)
cv.imshow('Card', img_resized)

cv.waitKey(0) 