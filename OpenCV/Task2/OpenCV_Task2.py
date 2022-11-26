import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Webcam
cap = cv.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

result = cv.VideoWriter(
    'filename.avi', cv.VideoWriter_fourcc(*'MJPG'), 10, (640, 480))

while True:
    success, img = cap.read()
    result.write(img)
    cv.imshow("Video", img)

    if cv.waitKey(1) & 0xFF == ord('c'):
        cv.imwrite('Frame.jpg', img)

    if cv.waitKey(1) & 0xFF == ord('r'):
        img_Rotated = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
        cv.imshow("img_Rotated Frame", img_Rotated)

    if cv.waitKey(1) & 0xFF == ord('g'):
        img_Gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imshow("img_Gray Frame", img_Gray)

    if cv.waitKey(1) & 0xFF == ord('h'):
        img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        cv.imshow("HSV Frame", img_hsv)

    if cv.waitKey(1) & 0xFF == ord('x'):
        img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        img_Gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img_Rotated = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
        cv.imshow("HSV Frame", img_hsv)
        cv.imshow("img_Rotated Frame", img_Rotated)
        cv.imshow("img_Gray Frame", img_Gray)
        cv.imshow("Img_Org Frame", img)

    if cv.waitKey(1) & 0xFF == ord('s'):
        break

    if cv.waitKey(1) & 0xFF == ord('z'):
        cv.imshow("Orig Frame", img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object
cap.release()
result.release()
cv.destroyAllWindows()
