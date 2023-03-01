from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Original Image
rgb_img = Image.open("Arch.jpg")

rgb_img_array = np.array(rgb_img)

# convert img to grayscale
gray_img = rgb_img.convert("L")

img = np.array(gray_img)


# flip, flop, invert, rotate_90

def flip_img(x, y, rows):
    return (x, rows - 1 - y)


def flop_img(x, y, columns):
    return (columns - 1 - x, y)


def rotate_90_img(x, y, rows):
    return (rows - y - 1, x)


columns = gray_img.size[0]
rows = gray_img.size[1]

flip = img.copy()
flop = img.copy()
invert = 255 - img
rotate = np.full((columns, rows), 0)


for x in range(columns):
    for y in range(rows):
        (x_flip, y_flip) = flip_img(x, y, rows)
        (x_flop, y_flop) = flop_img(x, y, columns)
        (x_rotate, y_rotate) = rotate_90_img(x, y, rows)
        flip[y][x] = img[y_flip][x_flip]
        flop[y][x] = img[y_flop][x_flop]
        rotate[x][y] = img[x_rotate][y_rotate]



flip_img = Image.fromarray(flip)
flop_img = Image.fromarray(flop)
invert_img = Image.fromarray(invert)
rotate_img = Image.fromarray(rotate)




fig0, ax0 = plt.subplots(nrows=3, ncols=2, sharey='all')

ax0[0, 0].imshow(rgb_img, cmap="gray")
ax0[0, 0].axis('off')
ax0[0, 0].title.set_text('Original Img')

ax0[0, 1].imshow(gray_img, cmap="gray")
ax0[0, 1].axis('off')
ax0[0, 1].title.set_text('Grayscale Img')

ax0[1, 1].imshow(flop_img, cmap="gray")
ax0[1, 1].axis('off')
ax0[1, 1].title.set_text('Flop Img')

ax0[1, 0].imshow(flip_img, cmap="gray")
ax0[1, 0].axis('off')
ax0[1, 0].title.set_text('Flip Img')

ax0[1, 1].imshow(flop_img, cmap="gray")
ax0[1, 1].axis('off')
ax0[1, 1].title.set_text('Flop Img')

ax0[2, 0].imshow(invert_img, cmap="gray")
ax0[2, 0].axis('off')
ax0[2, 0].title.set_text('Invert Img')

ax0[2, 1].imshow(rotate_img, cmap="gray")
ax0[2, 1].axis('off')
ax0[2, 1].title.set_text('Rotate Img')

plt.show()










