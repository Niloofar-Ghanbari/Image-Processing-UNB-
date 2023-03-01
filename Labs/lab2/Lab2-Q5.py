import numpy as np
from skimage import img_as_ubyte
from PIL import Image
import matplotlib.pyplot as plt

I = img_as_ubyte(Image.open("item.png"))


def values(binary_img, x, y):
    columns = binary_img.shape[0]
    rows = binary_img.shape[1]

    if x == columns or y == rows or x < 0 or y < 0:
        return 0
    else:
        return binary_img[x][y]


def dilate_B4(binary_img):
    columns = binary_img.shape[0]
    rows = binary_img.shape[1]
    dilated_array = np.zeros(binary_img.shape, dtype=bool)

    for x in range(columns):
        for y in range(rows):
            f1 = np.logical_or(
                values(binary_img, x, y),
                values(binary_img, x - 1, y))

            f2 = np.logical_or(
                values(binary_img, x + 1, y),
                values(binary_img, x, y - 1))

            f3 = np.logical_or(f1, f2)
            dilated_array[x][y] = np.logical_or(f3, values(binary_img, x, y + 1))

    return dilated_array


def erode_B4(binary_img):
    columns = binary_img.shape[0]
    rows = binary_img.shape[1]
    eroded_array = np.zeros(binary_img.shape, dtype=bool)

    for x in range(columns):
        for y in range(rows):
            f1 = np.logical_and(
                values(binary_img, x, y),
                values(binary_img, x - 1, y))

            f2 = np.logical_and(
                values(binary_img, x + 1, y),
                values(binary_img, x, y - 1))

            f3 = np.logical_and(f1, f2)
            eroded_array[x][y] = np.logical_and(f3, values(binary_img, x, y + 1))

    return eroded_array


original_img = Image.fromarray(I)

dilated_img = Image.fromarray(img_as_ubyte(dilate_B4(I)))

eroded_img = Image.fromarray(img_as_ubyte(erode_B4(I)))

# Plotting the result
fig, ax = plt.subplots(nrows=1, ncols=3)

ax[0].imshow(original_img, cmap="gray")
ax[0].axis('off')
ax[0].title.set_text('Original Img')

ax[1].imshow(dilated_img, cmap="gray")
ax[1].axis('off')
ax[1].title.set_text('Dilated Img')

ax[2].imshow(eroded_img, cmap="gray")
ax[2].axis('off')
ax[2].title.set_text('Eroded Img')

plt.show()