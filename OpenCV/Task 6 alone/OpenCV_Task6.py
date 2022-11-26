# import the necessary packages
import cv2
import numpy as np

# now let's initialize the list of reference point
ref_point = []


def shape_selection(event, x, y, flags, param):
    # grab references to the global variables
    global ref_point, crop

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being performed
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        ref_point.append((x, y))

        # draw a rectangle around the region of interest
        cv2.rectangle(imghor, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.imshow("Horizontal", imghor)


# load the images and put them in horizontal stack
img1 = cv2.imread(
    "D:\Bussiness\Vortex\Tasks\Python\OpenCV\Images\coral3.jpg")
img2 = cv2.imread(
    "D:\Bussiness\Vortex\Tasks\Python\OpenCV\Images\coral4.jpg")
resized_down1 = cv2.resize(
    img1, (640, 480), interpolation=cv2.INTER_LINEAR)  # resize the image
resized_down2 = cv2.resize(
    img2, (640, 480), interpolation=cv2.INTER_LINEAR)  # resize the image
#image = cv2.imread("Images/coral1.jpg")
imghor = np.hstack((resized_down1, resized_down2))

# clone our image, then setup the mouse callback function
clone = imghor.copy()
cv2.namedWindow("Horizontal")
cv2.setMouseCallback("Horizontal", shape_selection)


# keep looping until the 'c' key is pressed
while True:
    # display the image and wait for a keypress
    cv2.imshow("Horizontal", imghor)
    key = cv2.waitKey(1) & 0xFF

    # press 'r' to reset the window
    if key == ord("r"):
        imghor = clone.copy()

    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break

# close all open windows
cv2.destroyAllWindows()
