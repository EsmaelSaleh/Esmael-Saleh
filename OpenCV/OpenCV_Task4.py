import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def getXY(event, x, y, flags, param):  # get the coordinates of the mouse click
    if event == cv.EVENT_LBUTTONDOWN:  # left click event to draw a circle
        print(x, y)
        values.append((x, y))
        cv.circle(img, values[-1], 5, (0, 0, 255), -1)
    elif event == cv.EVENT_RBUTTONDOWN:  # right click event to delete the last circle
        try:
            cv.circle(img, values[-1], 5, (0, 0, 0), -1)
            values.pop()
        except:  # if there is no circle to delete
            print("No more circles to delete")


values = []  # list to store the coordinates of the circles
img = np.zeros((600, 600, 3), np.uint8)     # create a black image
cv.namedWindow('image')

while(1):  # loop to keep the window open
    cv.setMouseCallback('image', getXY)     # set the mouse callback function
    cv.imshow('image', img)            # show the image
    if cv.waitKey(20) & 0xFF == 27:     # wait for the escape key to be pressed
        break

print(values)  # print the coordinates of the circles
cv.destroyAllWindows()  # close the window
