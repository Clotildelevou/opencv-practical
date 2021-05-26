import cv2

#image
img = cv2.imread("../resources/lena.png")
cv2.imshow("Output", img)
cv2.waitKey(5000)

#video
cap = cv2.VideoCapture("resources/test_vid.mp4")
while True:
    success, img = cap.read()
    if success:
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

#webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640) #width
cap.set(1, 480) #height

while True:
    success, img = cap.read()
    if success:
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break