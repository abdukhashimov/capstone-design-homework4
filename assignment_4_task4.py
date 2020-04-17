"""Assignment 4 and task 4

Convert the image to the grayscale and using histogram equalization increase
the brightness of the dark.jpg image. Save resulted images

ID: U1610131
Name: Madiyor Abdukhashimov
"""
# importing opencv library - to be able to import opencv you need to install
# it using pip. The process of installation is provided in [README.md](../README.md)
import cv2
import numpy as np

# the value of brightness, which is in the range of 0 to 100
value = 80    # brightness control in range [0 - 100]

# we are reading the image from the `images` directory
image = cv2.imread('images/dark.jpg')

# getting the dimensions of the image
h, w, d = image.shape

# just resizing it to the half
resized_image = cv2.resize(image, (int(w/2), int(h/2)))

# converting the image to the grey color
grey = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# equalizing the grey scale image color distribution
grey_equalized_image = cv2.equalizeHist(grey)
# we are substracing the grey matrix elements from 255 and making them 100, 255, and adding the birghtness
bright_image = np.where((255 - grey) < 100, 255, grey + value)

# saving
cv2.imwrite('results/task4/original_grey.jpeg', grey)
cv2.imwrite('results/task4/grey_equalized_image.jpeg', grey_equalized_image)
cv2.imwrite('results/task4/bright_image.jpeg', bright_image)
# end of the saving process

# displaying
cv2.imshow('original', grey)
cv2.imshow('gray_equalized_image', grey_equalized_image)
cv2.imshow('bright', bright_image)
cv2.waitKey(5000)
# end of the displaying
