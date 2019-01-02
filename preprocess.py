import numpy as np
import cv2
import pywt

from mefun import find_biggest_contour, crop_image


def values(img):
    #convert image to gray scale and apply Gaussian Blur
    #convert image to gray scale and apply Gaussian Blur
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    # apply Otsu's method to threshold image
    ret, thresh = cv2.threshold(gray, 0, 255,
                                cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # noise removal
    kernel = np.ones((1, 1), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=6)

    # find biggest contour in thresholded image
    big_contour, mask, contours = find_biggest_contour(opening)

    # fill small gaps and remove specks
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # unpack max and min values from biggest contour
    xmax, xmin, ymax, ymin = crop_image(big_contour)

    # crop out only the area of interest
    crop = gray[ymin:ymax, xmin:xmax]

    # apply wavelet transform at level 3 with db4 wavelet
    coeff = pywt.wavedec(crop, 'db4', mode='symmetric', level=3)

    # extract coefficients
    a1 = coeff[1]
    a2 = coeff[2]
    a3 = coeff[3]

    # calculate coefficient of variation for the coefficients
    v2 = np.std(a1) / np.mean(a1)
    v3 = np.std(a2) / np.mean(a2)
    v4 = np.std(a3) / np.mean(a3)

    final_vals = [v2, v3, v4]

    return final_vals
