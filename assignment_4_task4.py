"""Assignment 4 and task 4

Convert the image to the grayscale and using histogram equalization increase
the brightness of the dark.jpg image. Save resulted images

ID: U1610131
Name: Madiyor Abdukhashimov
"""

import cv2
import numpy as np

value = 80    # brightness control in range [0 - 100]

image = cv2.imread('images/dark.jpg')
h, w, d = image.shape
resized_image = cv2.resize(image, (int(w/2), int(h/2)))

grey = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
grey_equalized_image = cv2.equalizeHist(grey)
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
