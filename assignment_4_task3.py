"""Assignment 4 and task 3

First decrease the size of an image then create blurred and sharpen
images from flower.jpg image. Save resulted images.

ID: U1610131
Name: Madiyor Abdukhashimov
"""


import cv2
# importing numpy as np - which helps to generate matrices
import numpy as np

# defining kernel for bluring image
kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.float32) / \
    (kernel_size*kernel_size)
# end of kernel for bluring image

# defining kernel for sharpening
kernel_sharpen = np.array([
    [-1, -1, -1, ],
    [-1, 9, -1],
    [-1, -1, -1]
])


# read the image from the `images/ directory`
image = cv2.imread('images/flower.jpg')

# getting the dimensions of the image horizonta, width, and dimension
h, w, d = image.shape

# resizing the image
resized_image = cv2.resize(image, (int(w/4), int(h/4)))

# bluring the image using filtering
blured_image = cv2.filter2D(resized_image, -1, kernel)

# end of sharpening the image
sharpened_image = cv2.filter2D(resized_image, -1, kernel_sharpen)


# save it to the file
cv2.imwrite('results/task3/resized_image.jpeg', resized_image)
cv2.imwrite('results/task3/blured_image.jpeg', blured_image)
cv2.imwrite('results/task3/sharpened_image.jpeg', sharpened_image)
# end of the saving to the file

# displaying the results of images
cv2.imshow('resized_image.jpeg', resized_image)
cv2.imshow('blured_image.jpeg', blured_image)
cv2.imshow('sharpened_image.jpeg', sharpened_image)
cv2.waitKey(5000)
# end of the displaying results of images
