import cv2
import numpy as np

img = cv2.imread("../resources/lena.png")
kernel = np.ones((3,3), np.uint8)

# grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blurred
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
# detect edges
imgCanny = cv2.Canny(img, 150, 150)
# dialation
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# erosion
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)


cv2.imshow("Output", imgGray)
cv2.imshow("OutputBlur", imgBlur)
cv2.imshow("OutputCanny", imgCanny)
cv2.imshow("OutputCannyDia", imgDialation)
cv2.imshow("OutputCannyEroded", imgEroded)
cv2.waitKey(5000)
