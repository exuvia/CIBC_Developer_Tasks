# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30  2017

@author: Aboozar Mapar
@email: A.Mapar@gmail.com


Goal: Scientific and numerical computing.

Continuing from Required Task 3 above, create a Python function that will find the affine transformation between two sets of 2D or 3D correspondence points. The affine transformation is a linear transformation and translation that can be expressed in a single matrix, 3x3 in the 2D case and 4x4 in the 3D case. See the Wikipedia page for more information. With a set of corresponding points, the affine transformation can be found by solving for the coefficients of the affine transformation in the least squared sense.

Create a Python function that will use the affine transformation calculated for 2D points to combine two images into one. Create some test code using pytest.


This code finds the affine transfer based on two sets of 2D points 
and uses the results to combine two images .
"""
import os 
import sys
import matplotlib.pyplot as plt
import numpy as np
import cv2

'''
This function uses openCV to estimate the affine transform of one image with
respect to another.

Inputs: 
    Image1: The original image
    points1: Points on the original image
    points2: Same points on the transformed image
    
Outputs:
    TransformedImaged: the original image after the affine transform
    
'''
def findAffineTrans(Image1, points1, points2):

    
    rows,cols,ch = Image1.shape


    trans = cv2.getAffineTransform(points1[0:3,:].astype("float32"),points2[0:3,:].astype("float32"))

    TransformedImaged = cv2.warpAffine(Image1,trans,(cols,rows))

    return TransformedImaged






ImagePath = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), 'test_data','2D_registration'))
# Processing B&W images

FileName = [ "w0.png", "w1.png"]

 

w0 = cv2.imread(os.path.join(ImagePath, FileName[0]))
w1 = cv2.imread(os.path.join(ImagePath, FileName[1]))


# points on w0
p0=np.array([434,   6,
451, 136,
540, 125,
550,  21,
542, 222,
563, 270,
454, 216,
355, 244,
402, 295,
535, 216,
563, 267,
565, 282,
566, 306]).reshape(13,2)
    
# points on w1    
p1=np.array([81,  72,
106, 227,
210, 203,
218,  69,
212, 328,
243, 383,
110, 325,
9, 360,
63, 418,
203, 322,
243, 383,
246, 399,
248, 429]).reshape(13,2)



# setup the figure
fig = plt.figure("Balck and White 0")
#plt.suptitle("MSE: %.2f,  SSIM: %.2f" % (MSE, SSIM))
 
# show first image
plt.imshow(w0, cmap = plt.cm.gray)
plt.plot(p0[:,0], p0[:,1], 'r.')
plt.axis("off")


fig = plt.figure("Balck and White 1")
# show the second image
plt.imshow(w1, cmap = plt.cm.gray)
plt.plot(p1[:,0], p1[:,1], 'r.')
plt.axis("off")
 
# show the images
plt.show()



# finding affine transform
TransformedImage = findAffineTrans(w0,p0,p1)

# plotting the original image
cv2.imshow("Original", w0)
# plotting the transformed image
cv2.imshow("Transformed", TransformedImage)
# plotting the combined images
combined = cv2.addWeighted(w1,.7,TransformedImage,0.3,0)
cv2.imshow("Combined", combined)
cv2.waitKey(0)
