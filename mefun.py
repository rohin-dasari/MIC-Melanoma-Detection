import numpy as np
import cv2
import pywt


def find_biggest_contour(image):

    # Copy to prevent modification
    image = image.copy()
    image = cv2.medianBlur(image, 9)
    _, contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE,
                                              cv2.CHAIN_APPROX_SIMPLE)

    # Isolate largest contour
    contour_sizes = [(cv2.contourArea(contour), contour)
                     for contour in contours]
    biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]

    mask = np.zeros(image.shape, np.uint8)
    cv2.drawContours(mask, [biggest_contour], -1, 255, -1)
    return biggest_contour, mask, contours


def crop_image(cnt):
    # isolate x and y values
    x = []
    y = []
    x1 = []
    y1 = []
    xy = []

    for i in range(len(cnt)):
        val = cnt[i]
        val = val[0]
        xval = val[0]
        yval = val[1]
        x.append(xval)
        x1.append(xval)
        y.append(yval)
        y1.append(yval)
        xy.append([xval, yval])

    # convert to numpy arrays
    x1 = np.array(x1)
    y1 = np.array(y1)

    # find max x val
    xmax = np.amax(x1)

    # find min x val
    xmin = np.amin(x1)

    # find max y val
    ymax = np.amax(y1)

    # find min y val
    ymin = np.amin(y1)

    # return newnewx, newnewy, symmscore, xmax, xmin, ymax, ymin
    return xmax, xmin, ymax, ymin