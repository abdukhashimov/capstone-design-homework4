"""Assignment 4 and task 2

This script manually separates moonphcamera.jpg image into two different images

ID: U1610131
Name: Madiyor Abdukhashimov
"""

import cv2

image = cv2.imread('images/moonphcamera.jpg')

cv2.imwrite('results/task2/people.jpeg', image[80:310, 72:210])
cv2.imwrite('results/task2/cameras.jpeg', image[120:335, 257:494])
