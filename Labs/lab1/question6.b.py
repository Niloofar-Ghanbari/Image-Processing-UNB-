import numpy as np
from PIL import Image
import cv2 as cv
Array = np.array([[5, 8, 3, 7],
              [1, 3, 3, 9],
              [6, 8, 2, 7],
              [4, 1, 0, 9]])







# original image
parrot_img = Image.open("parrot.png")
img_array = np.array(parrot_img)


# convert to grayscale
gray_img = parrot_img.convert("L")


gray_img_array = np.array(gray_img)

columns = gray_img.size[0]
rows = gray_img.size[1]

k = 0
l = rows * columns


def calculate_histogram(img, columns, rows):
    h = np.full((256, 1), 0)
    for x in range(columns):
        for y in range(rows):
            h[img[y][x]] = h[img[y][x]] + 1

    return h


def calculate_normalized_histogram(histogram, n):
    return histogram / n


def calculate_running_sum(a):
    length = len(a)
    s = np.full((length, 1), 0.0)
    s[0] = a[0]
    for k in range(1, length - 1):
        s[k] = s[k - 1] + a[k]
    return s


def calculate_histogram_equalization(img, columns, rows):
    I = np.full((rows, columns), 0)

    histogram = calculate_histogram(img, columns, rows)
    normalized_histogram = calculate_normalized_histogram(histogram, columns * rows)

    for x in range(columns):
        for y in range(rows):
            I[y][x] = np.round(256 * (calculate_running_sum(normalized_histogram)[img[y][x]]))
    return I


histogram_equalization = calculate_histogram_equalization(gray_img_array, columns, rows)

I_new = Image.fromarray(histogram_equalization)
I_new.show()

# open cv module
src = cv.imread("parrot.png")
src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
dst = cv.equalizeHist(src)
cv.imshow('Source image', src)
cv.imshow('Equalized Image', dst)
cv.waitKey()





difference = np.full((rows, columns), 0)
for x in range(columns):
    for y in range(rows):
        if (dst[y][x] != histogram_equalization[y][x]):
            difference[y][x] = 255

difference_image = Image.fromarray(difference)
difference_image.show()