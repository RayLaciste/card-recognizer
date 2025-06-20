import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# 1. Paint the image a certain color
# blank[200:300, 300:400] = 0, 255, 0
# cv.imshow('Green', blank)

# 2. Draw a rectanlge
# cv.rectangle(blank, (0,0), (250,250), (0, 255, 0), thickness=-1)
# cv.imshow('Rectangle', blank)

# 3. Draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=3)
# cv.imshow('Circle', blank)

# 4. Draw a Line
# cv.line(blank, (0,0), (250,250), (0, 255, 0), thickness=2)
# cv.imshow('Line', blank)

# 5. Write text
# cv.putText(blank, 'Hello', (255, 255), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
# cv.imshow('Text', blank)

cv.waitKey(0)