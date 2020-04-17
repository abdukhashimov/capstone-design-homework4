"""Assignment 4 and task 1

This script manually inserts the rectangles to the people and moon.
ID: U1610131
Name: Madiyor Abdukhashimov
"""

import cv2


image = cv2.imread('images/moonphcamera.jpg')

# place the red rectangle onto people.
people_and_moon = cv2.rectangle(
    img=image,
    pt1=(72, 80),
    pt2=(208, 307),
    color=(0, 0, 255),
    thickness=3,
)

# place the rectangle onto the Moon
people_and_moon = cv2.rectangle(
    img=people_and_moon,
    pt1=(392, 126),
    pt2=(432, 160),
    color=(0, 0, 0),
    thickness=1,
)


# display the image
cv2.imshow('people_and_moon_selected', people_and_moon)

# save the file
cv2.imwrite('results/task1/people_and_moon_selected.jpeg', people_and_moon)

# wait 5 seconds
cv2.waitKey(5000)
