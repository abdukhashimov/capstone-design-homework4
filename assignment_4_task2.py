"""Assignment 4 and task 1

This script manually inserts the rectangles to the people and moon.
ID: U1610131
Name: Madiyor Abdukhashimov
"""

import cv2

image = cv2.imread('images/moonphcamera.jpg')

cv2.imwrite('results/task2/people.jpeg', image[80:310, 72:210])
cv2.imwrite('results/task2/cameras.jpeg', image[120:335, 257:494])
