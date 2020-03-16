''' file name : canny.py

Description : This sample shows how to find edges using canny edge detection

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/imgtrans/canny_detector/canny_detector.html

Level : Beginner

Benefits : Learn to apply canny edge detection to images.

Usage : python canny.py

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials '''


import cv2
import sys
import numpy as np

def CannyThreshold(lowThreshold):

    #k = cv2.getTrackbarPos('Kernel size','canny demo')
    #if k%2==0:
    #    k+=1

    detected_edges = cv2.GaussianBlur(gray,(kernel_size,kernel_size),0) # This kernel affects the canny performance a lot !!
    detected_edges = cv2.Canny(detected_edges,lowThreshold,lowThreshold*ratio,apertureSize = kernel_size)
    dst = cv2.bitwise_and(img,img,mask = detected_edges)  # just add some colours to edges from original image.
    cv2.imshow('canny demo',dst)

lowThreshold = 50
max_lowThreshold = 255
ratio = 3
kernel_size = 5 # can take values 3, 5 or 7 !!! Affects output a lot

img = cv2.imread(sys.argv[1])
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.namedWindow('canny demo')

cv2.createTrackbar('Min threshold','canny demo',lowThreshold, max_lowThreshold, CannyThreshold)
#cv2.createTrackbar('Kernel size','canny demo',kernel_size, 7, CannyThreshold)


CannyThreshold(0)  # initialization
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

# visit for output results : http://opencvpython.blogspot.com/2012/06/image-derivatives-sobel-and-scharr.html
