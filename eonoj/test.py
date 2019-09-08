#This program reads an image, can binarize it, and save an the binarized image

import cv2 as cv
#reads image
img = cv.imread('crop_stop.jpg',0) #,0 is flag to read the images in monochrome

#thresholds image
#ret,thresh = cv.threshold(img,64,255,cv.THRESH_BINARY)

#saves image
#cv.imwrite('/home/oj/openpilot/oj_scripts/1bin.jpg', thresh)


#shows image
cv.imshow('image',img)
#cv.imshow('thresholded image',thresh)
cv.waitKey(0)
cv.destroyAllWindows()

