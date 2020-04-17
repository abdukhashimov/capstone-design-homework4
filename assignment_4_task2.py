"""Assignment 4 and task 2

This script manually separates moonphcamera.jpg image into two different images

ID: U1610131
Name: Madiyor Abdukhashimov
"""

import cv2


# read the image from the `images/ directory`
image = cv2.imread('images/moonphcamera.jpg')

# selecting the people from the image and cutting then saving it
people = image[80:310, 72:210]

# selecting the cameras from the image and cutting then saving it
cameras = image[120:335, 257:494]

# saving results the the `results` directory
cv2.imwrite('results/task2/people.jpeg', people)
cv2.imwrite('results/task2/cameras.jpeg', cameras)
# end of saving results

# displaying results
cv2.imshow('people.jpeg', people)
cv2.imshow('cameras.jpeg', cameras)
# end of displaying

# wait 5 seconds
cv2.waitKey(5000)
