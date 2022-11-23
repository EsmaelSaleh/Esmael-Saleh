import cv2
import numpy as np

circles = np.zeros((4, 2), np.int)
counter = 0
i = 0
# Function To get Mouse Points and store it into Array Circles


def MousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:  # if we click on Left Button on image it will take that point and store it
        print(x, y)
        circles[counter] = x, y
        counter = counter+1
        print(circles)


img = cv2.imread(
    "D:\\Bussiness\\Vortex\\Tasks\\Python\\OpenCV\\OpenCV images&videos\\tasks_images_\\task_5\\computer vision.PNG")
while True:
    if counter == 4:
        width, height = 600, 500
        # Points that we click on image and store on Circles
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        # Standard Points
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        # Transformation Matrix
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutPut = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("Output Image", imgOutPut)

    # To Draw Circles
    for x in range(0, 4):
        cv2.circle(img, (circles[x][0], circles[x][1]),
                   6, (67, 12, 243), cv2.FILLED)

    cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("Original Image ", MousePoints)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == 27:     # wait for the escape key to be pressed
        exit()
