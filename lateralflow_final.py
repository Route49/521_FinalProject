#! /usr/bin/python

#Team: Route49
#Names: Cindy Wong, Sonia Parra
#Date Modified: 12-1-2015
#Description: This program takes an image of a lateral flow strip
#   and tests to see whether the strip is positive for wild type or
#   mutant strains of the sample of interest


#------------Import Statemtents----------------------
import time
import picamera
import numpy as np
import cv2
import matplotlib.pyplot as plt

#------------Preview with Camera----------------------
video_capture = cv2.VideoCapture(0)

#video continuously runs until the user presses the 'q' key
while True:
     ret, frame = video_capture.read()
     frame[220:230, 495:545] = 0
     frame[210:240, 515:525] = 0
     cv2.imshow('Video', frame)
     if cv2.waitKey(1) & 0xFF == ord('q'):
          break

#release and destroy all the videos and windows
video_capture.release()
cv2.destroyAllWindows()


#------------Take picture with USB camera--------------
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert the image to a gray scale

cv2.imwrite('cellphone/cell4c.jpg', img) #writes the value to a file

#displays the image to the user
cv2.imshow('Sample', img)
cv2.waitKey(0)
cap.release
cv2.destroyAllWindows()

#------------Histogram Equalization-------------------
#finding the ROI for the wild type
ROIimgWT = img[0:150, 200:500]
cv2.imshow('ROI WT', ROIimgWT)
cv2.waitKey(0)
cv2.imwrite('cellphone/cellROI_WT4c.jpg', img)
cv2.destroyAllWindows()

#wild type histogram equalization
equWT = cv2.equalizeHist(ROIimgWT)
cv2.imshow('Equal Hist WT', equWT)
cv2.waitKey(0)
cv2.imwrite('cellphone/cellHist_WT4c.jpg', img)
cv2.destroyAllWindows()

#finding the ROI for the mutant
ROIimgMnt = img[320:460, 200:500]
cv2.imshow('ROI Mnt', ROIimgMnt)
cv2.waitKey(0)
cv2.imwrite('cellphone/cellROI_Mnt4c.jpg', img)
cv2.destroyAllWindows()

#mutant histogram equalization
equMnt = cv2.equalizeHist(ROIimgMnt)
cv2.imshow('Equal Hist Mnt', equMnt)
cv2.waitKey(0)
cv2.imwrite('cellphone/cellHist_Mnt4c.jpg',img)
cv2.destroyAllWindows()

#------------Extract Intensities along line----------
lineWT = equWT[75, 0:200]
lineMnt = equMnt[75, 0:200]

#plot intensities over the wild type line
plt.plot(lineWT)
plt.savefig('cellphone/cellWTplot4c.jpg')
plt.show()
#plot intensities over the mutant type line
plt.plot(lineMnt)
plt.savefig('cellphone/cellMntplot4c.jpg')
plt.show()

countWT = 0   #count of the number of points below the threshold for wild type
countMnt = 0  #count of the number of points below the threshold for mutant

#sums up all the intensity values for the wild type and mutant
for j in range(200):
     if equWT[75,j] <= 55:
          countWT = countWT + 1
     if equMnt[75,j] <= 55:
          countMnt = countMnt + 1

#calculates the change in intensity based on percentage for wild type
if countWT >= 20:
     print 'positive WT sample'
else:
     print 'negative WT sample'

#calculates change in intensity based on percentage for mutant
if countMnt >= 35:
     print 'positive Mnt sample'
else:
     print 'negative Mnt sample'
