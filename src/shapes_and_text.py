import cv2
import  numpy as np

img = np.zeros((512, 512, 3), np.uint8)

img[200:400, 100:300]= 255, 3, 155 # filled rectagle
cv2.line(img, (50, 50), (300, 300), (0, 255, 0), 3) #line
cv2.rectangle(img, (100, 100), (200, 200), (100, 248, 200), 3) # rectangle
cv2.circle(img, (250, 250), 200, (250, 147, 88), 8) #circle
cv2.putText(img, "zebi", (100, 250), cv2.FONT_HERSHEY_COMPLEX, 5, (255, 255, 255), 2)



cv2.imshow("Output", img)
cv2.waitKey(0)
