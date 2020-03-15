''' file name : BasicLinearTransforms.py

Description : This sample shows how apply an equation on an image, g(x) = alpha*i(x) + beta

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/core/basic_linear_transform/basic_linear_transform.html

Level : Beginner

Benefits : Learn use of basic matrix operations in OpenCV and how they differ from corresponding numpy operations

Usage : python BasicLinearTransforms.py

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials '''

import cv2
import sys
import numpy as np


print " Basic Linear Transforms "
print "-----------------------------"

alpha = float(input('* Enter the alpha value to control contrast [1.0-3.0]: '))     # Simple contrast control
beta = int(input('Enter the beta value to control brightness [0-100]: '))             # Simple brightness control


img = cv2.imread(sys.argv[1])

mul_img = cv2.multiply(img,np.array([alpha]))                    # mul_img = img*alpha
new_img = cv2.add(mul_img,np.full_like(mul_img, beta))                      # new_img = img*alpha + beta
#new_img = cv2.add(mul_img,np.array([beta]))                      # new_img = img*alpha + beta

cv2.imshow('original_image', img)
cv2.imshow('new_image',new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

## NB : Please visit for more details: http://opencvpython.blogspot.com/2012/06/difference-between-matrix-arithmetic-in.html 
