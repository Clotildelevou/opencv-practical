import cv2
import numpy as np

#image
img = cv2.imread("../resources/cards.jpg")
width, height = img.shape[1], img.shape[0]
cards_points = np.float32([[286, 55], [394, 54], [289, 185], [417, 184]])
img_points = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(cards_points, img_points)
imgOut = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Output2", img)
cv2.imshow("Output", imgOut)
cv2.waitKey(0)
