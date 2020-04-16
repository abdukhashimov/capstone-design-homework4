"""Assignment 4 and task 2

This script manually separates moonphcamera.jpg image into two different images

ID: U1610131
Name: Madiyor Abdukhashimov
"""

import cv2

image = cv2.imread('images/moonphcamera.jpg')

people = image[80:310, 72:210]
cameras = image[120:335, 257:494]

# saving results
cv2.imwrite('results/task2/people.jpeg', people)
cv2.imwrite('results/task2/cameras.jpeg', cameras)
# end of saving results

# displaying results
cv2.imshow('people.jpeg', people)
cv2.imshow('cameras.jpeg', cameras)
cv2.waitKey(5000)