# CHAPTER 2 BASIC FUNCTIONS
import cv2
import numpy as np

img = cv2.imread('lena.png')

# Greyscale Function
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', imgGray)

# Blur Function
imgBlur = cv2.GaussianBlur(imgGray, (7,7),0)  # has to be odd number for ksize
cv2.imshow('Blur Image', imgBlur)

# Edge Detector
imgCanny = cv2.Canny(img, 150, 200)
cv2.imshow('Canny Image', imgCanny)

# Dilation
kernel = np.ones((5,5), np.uint8)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
cv2.imshow('Dilation Image', imgDialation)

# Erosion
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
cv2.imshow('Eroded Image', imgEroded)

cv2.waitKey(0)
