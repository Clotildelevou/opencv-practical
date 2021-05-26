import cv2

img = cv2.imread("../resources/lena.png")

# resize
imgResize = cv2.resize(img, (1024, 1024))

# crop
imgCropped = img[0:200, 300:512]

cv2.imshow("Output", img)
cv2.imshow("resized", imgResize)
cv2.imshow("cropped", imgCropped)
cv2.waitKey(5000)