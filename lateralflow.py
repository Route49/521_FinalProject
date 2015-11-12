#! /usr/bin/python

#Team: Route49
#Names: Cindy Wong, Sonia Parra
#Date Modified: 11-12-2015
#Description: 

import time
import picamera
import numpy as np
import cv2
import matplotlib.pyplot as plt

#------------Take picture with pi camera--------------
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

cv2.imshow('Sample', gray)
cv2.waitKey(0)
cap.release
cv2.destroyAllWindows()

cv2.imwrite('test.jpg', gray)


#-----------Create Templates from base Image--------
USBtemp = cv2.imread('template.jpg', 0)
cv2.imshow('USB temp', USBtemp)
cv2.waitKey(0)
cv2.destroyAllWindows()

USBtempWT = USBtemp[0:150, 150:525]
cv2.imshow('USBtempWT', USBtempWT)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('tempWT.jpg', USBtempWT)

USBtempMnt = USBtemp[320:460, 150:525]
cv2.imshow('USBtempMnt', USBtempMnt)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('tempMnt.jpg', USBtempMnt)

#------------Display Images to be Processed----------
#filename = filename + '.jpg'
#filename = '20151015-154636.jpg'
#filename = 'DoubleControl.tif'
#filename = 'DoublePosSource.tif'
#img = cv2.imread(filename, 0)
img = gray
#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#-------------Extract ROI-----------------------------
#templateWT = cv2.imread('WTControl.tif', 0)	#wild type control image
#templateMnt = cv2.imread('MntControl.tif', 0)	#mutant control image
templateWT = USBtempWT
templateMnt = USBtempMnt


#cv2.imshow('templateWT', templateWT)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#cv2.imshow('templateMnt', templateMnt)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#-------------Template Matching-----------------------
#width and height of ROI
wWT,hWT = templateWT.shape[: : -1]
wMnt,hMnt = templateMnt.shape[: : -1]

#resulting template matching image and the area in the original image that matches
#res = cv2.matchTemplate(img, template, eval('cv2.TM_CCOEFF'))
resWT = cv2.matchTemplate(img, templateWT, eval('cv2.TM_CCOEFF_NORMED'))
#res = cv2.matchTemplate(img, template, eval('cv2.TM_CCORR'))
#res = cv2.matchTemplate(img, template, eval('cv2.TM_CCORR_NORMED'))
#res = cv2.matchTemplate(img, template, eval('cv2.TM_SQDIFF'))
#res = cv2.matchTemplate(img, template, eval('cv2.TM_SQDIFF_NORMED'))
resMnt = cv2.matchTemplate(img, templateMnt, eval('cv2.TM_CCOEFF_NORMED'))

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resWT)
top_leftWT = max_loc
bottom_rightWT = (top_leftWT[0]+wWT, top_leftWT[1]+hWT)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resMnt)
top_leftMnt = max_loc
bottom_rightMnt = (top_leftWT[0]+wMnt, top_leftWT[1]+hMnt)

#drawing a rectangle around the proper area in the original image and displaying it
img2 = img.copy()
cv2.rectangle(img2, top_leftWT, bottom_rightWT, 0, 2)
cv2.imshow('WT Rect', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#draw rect around area on bottom
img2 = img.copy()
cv2.rectangle(img2, top_leftMnt, bottom_rightMnt, 0, 2)
cv2.imshow('Mnt Rect', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#------------Histogram Equalization-------------------
ROIimgWT = img[top_leftWT[1]:top_leftWT[1]+hWT, top_leftWT[0]:top_leftWT[0]+wWT]
cv2.imshow('ROI WT', ROIimgWT)
cv2.waitKey(0)
cv2.destroyAllWindows()

equWT = cv2.equalizeHist(ROIimgWT)
cv2.imshow('Equal Hist WT', equWT)
cv2.waitKey(0)
cv2.destroyAllWindows()

equTempWT = cv2.equalizeHist(templateWT)
cv2.imshow('Equ Hist WT Temp', equTempWT)
cv2.waitKey(0)
cv2.destroyAllWindows()


ROIimgMnt = img[top_leftMnt[1]:top_leftMnt[1]+hMnt, top_leftMnt[0]:top_leftMnt[0]+wMnt]
cv2.imshow('ROI Mnt', ROIimgMnt)
cv2.waitKey(0)
cv2.destroyAllWindows()

equMnt = cv2.equalizeHist(ROIimgMnt)
cv2.imshow('Equal Hist Mnt', equMnt)
cv2.waitKey(0)
cv2.destroyAllWindows()

equTempMnt = cv2.equalizeHist(templateMnt)
cv2.imshow('Equ Hist Mnt Temp', equTempMnt)
cv2.waitKey(0)
cv2.destroyAllWindows()

#------------Extract Intensities along line----------
lineWT = equWT[hWT/2, 0:wWT]
templatelineWT = equTempWT[hWT/2, 0:wWT]

lineMnt = equMnt[hMnt/2, 0:wMnt]
templatelineMnt = equTempMnt[hMnt/2, 0:wMnt]

plt.plot(lineWT)
plt.show()

plt.plot(lineMnt)
plt.show()

count = 0
linesumWT = 0
templatesumWT = 0
linesumMnt = 0
templatesumMnt = 0

for i in range(100):
     for j in range(200):
          linesumWT = linesumWT + equWT[i,j]
          templatesumWT = templatesumWT + templateWT[i,j]
          linesumMnt = linesumMnt + equMnt[i,j]
          templatesumMnt = templatesumMnt + templateMnt[i,j]
print linesumWT
print templatesumWT
print linesumMnt
print templatesumMnt

changeWT = linesumWT/templatesumWT
if changeWT < 0.75:
     print 'positive WT sample'

changeMnt = linesumMnt/templatesumMnt
if changeMnt < 0.75:
     print 'positive Mnt sample'
