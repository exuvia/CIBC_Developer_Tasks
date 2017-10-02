# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30  2017

@author: Aboozar Mapar
@email: A.Mapar@gmail.com


Goal: Demonstrate your ability to build Python scripts.

In python generate a script that will load in two 2D color images and evaluate the differences between them. The script must somehow quantify the differences between images.

You can use common python packages in you implementations (numpy, scipy, etc). Write some pytest code to test your implementations with the included test data.

For sample input data, download this (https://www.dropbox.com/s/k13v6pa2kr1z5we/test_data.zip?dl=0) zip.
"""
import os 
import sys
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
#from skimage.measure import compare_ssim as ssim
import skimage.measure as skm
import cv2



ImagePath = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), 'test_data','2D_registration'))
# Processing B&W images

FileName = [ "w0.png", "w1.png", "test_image_1.png", "test_image_2.png"]

 
w0 = misc.imread(os.path.join(ImagePath, FileName[0]),flatten=True, mode = 'L')    
w1 = misc.imread(os.path.join(ImagePath, FileName[1]),flatten=True, mode = 'L')    

# Calculating the mean-squared error between two images.
MSE = skm.compare_mse(w0,w1)
# Calculating the mean structural similarity index between two images.
(SSIM, diff) = skm.compare_ssim(w0, w1, full=True)

# setup the figure
fig = plt.figure("Balck and White")
plt.suptitle("MSE: %.2f,  SSIM: %.2f" % (MSE, SSIM))
 
# show first image
ax = fig.add_subplot(1, 2, 1)
plt.imshow(w0, cmap = plt.cm.gray)
plt.axis("off")
 
# show the second image
ax = fig.add_subplot(1, 2, 2)
plt.imshow(w1, cmap = plt.cm.gray)
plt.axis("off")
 
# show the images
plt.show()

# plotting the difference image
diff = (diff * 255).astype("uint8")
cv2.imshow("Difference between the back and white images", diff)
cv2.waitKey(0)


# Processing color images


# load the two input images
image1 = cv2.imread(os.path.join(ImagePath, FileName[2]))
image2 = cv2.imread(os.path.join(ImagePath, FileName[3]))

# convert the images to grayscale
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Calculating the mean-squared error between two images.
MSE = skm.compare_mse(gray1,gray2)
# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
(SSIM, diff) = skm.compare_ssim(gray1, gray2, full=True)

# setup the figure
fig = plt.figure("Color images")
plt.suptitle("MSE: %.2f,  SSIM: %.2f" % (MSE, SSIM))
 
# show first image
ax = fig.add_subplot(1, 2, 1)
plt.imshow(gray1, cmap = plt.cm.gray)
plt.axis("off")
 
# show the second image
ax = fig.add_subplot(1, 2, 2)
plt.imshow(gray2, cmap = plt.cm.gray)
plt.axis("off")
 
# show the images
plt.show()

# plotting the difference image
diff = (diff * 255).astype("uint8")
cv2.imshow("Difference between the two color images", diff)
cv2.waitKey(0)
