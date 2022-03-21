import cv2
import  numpy as np

img = cv2.imread("../resources/lena.png")
print(img.shape)

imgHor = np.hstack((img, img))
print(imgHor.shape)
imgVer = np.vstack((img, img))
print(imgVer.shape)

cv2.imshow("Hor", imgHor)
cv2.imshow("Ver", imgVer)
cv2.waitKey(0)