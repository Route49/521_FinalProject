#! /usr/bin/python

#Team: Route49
#Names: Cindy Wong, Sonia Parra
#Date Modified: 10-15-2015
#Version Number: 1
#Description: 

import time
import picamera
import numpy as np
import cv2

#------------Take picture with pi camera--------------
#camera = picamera.PiCamera()
#camera.resolution = (1024, 768)
#camera.start_preview()
#time.sleep(2)
#filename = time.strftime("%Y%m%d-%H%M%S")
#filename = 'test'
#camera.capture(filename + ".jpg")
#camera.stop_preview()

#------------Display Images to be Processed----------
#filename = filename + '.jpg'
#filename = '20151015-154636.jpg'
#filename = 'DoubleControl.tif'
filename = 'DoublePosSource.tif'
img = cv2.imread(filename, 0)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#-------------Extract ROI-----------------------------
#template = img[50:200, 50:300]
template = cv2.imread('WTControl.tif', 0)
#template = cv2.imread('MntControl.tif', 0)
#template = 'DoubleControl.tif'
cv2.imshow('template', template)
cv2.waitKey(0)
cv2.destroyAllWindows()

#-------------Template Matching-----------------------
#width and height of ROI
w,h = template.shape[: : -1]

#resulting template matching image and the area in the original image that matches
#res = cv2.matchTemplate(img, template, eval('cv2.TM_CCOEFF'))
res = cv2.matchTemplate(img, template, eval('cv2.TM_CCOEFF_NORMED'))
#res = cv2.matchTemplate(img, template, eval('cv2.TM_CCORR'))
#res = cv2.matchTemplate(img, template, eval('cv2.TM_CCORR_NORMED'))
#res = cv2.matchTemplate(img, template, eval('cv2.TM_SQDIFF'))
#res = cv2.matchTemplate(img, template, eval('cv2.TM_SQDIFF_NORMED'))
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0]+w, top_left[1]+h)

#drawing a rectangle around the proper area in the original image and displaying it
img2 = img.copy()
cv2.rectangle(img2, top_left, bottom_right, 0, 2)
cv2.imshow('image3', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


#------------Histogram Equalization-------------------
ROIimg = img[top_left[1]:top_left[1]+h, top_left[0]:top_left[0]+w]
cv2.imshow('ROI', ROIimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

equ = cv2.equalizeHist(ROIimg)
cv2.imshow('Equalized Hist', ROIimg)
cv2.waitKey(0)
cv2.destroyAllWindows()


#------------Extract Intensities along line----------

