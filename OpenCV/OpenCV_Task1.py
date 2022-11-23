import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# Blank image
img = np.zeros((201, 201, 3), dtype='uint8')

# Draw squares
cv.rectangle(img, (100, 100), (200, 0), (255, 0, 0), -1)  # red
cv.rectangle(img, (100, 100), (200, 200), (0, 0, 255), -1)  # blue
cv.rectangle(img, (100, 100), (0, 200), (0, 255, 0), -1)  # green
cv.rectangle(img, (100, 99), (0, 0), (0, 0, 0), -1)  # black

# Display image
plt.imshow(img)
plt.show()
