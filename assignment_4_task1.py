"""Assignment 4 and task 1

This script manually inserts the rectangles to the people and moon.
ID: U1610131
Name: Madiyor Abdukhashimov
"""

# importing opencv library - to be able to import opencv you need to install
# it using pip. The process of installation is provided in [README.md](../README.md)
import cv2


# read the image from the `images/ directory`
image = cv2.imread('images/moonphcamera.jpg')

# place the red rectangle onto people.
people_and_moon = cv2.rectangle(
    img=image,  # the image that we have loaded
    pt1=(72, 80),  # starting point for rectangle
    pt2=(208, 307),  # ending point for rectangle
    color=(0, 0, 255),  # the red color that we are sending
    thickness=3,  # the size for the line of rectangle
)

# place the rectangle onto the Moon
people_and_moon = cv2.rectangle(
    img=people_and_moon,  # the image that has moon and people
    pt1=(392, 126),  # the starting point for rectangle
    pt2=(432, 160),  # the ending poin for rectangle
    color=(0, 0, 0),  # the color of rectangle
    thickness=1,  # the size for the line of rectangle
)


# display the image
cv2.imshow('people_and_moon_selected', people_and_moon)

# save the file
cv2.imwrite('results/task1/people_and_moon_selected.jpeg', people_and_moon)

# wait 5 seconds
cv2.waitKey(5000)
