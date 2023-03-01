from PIL import Image
from skimage import img_as_ubyte
import math
from skimage.measure import label, regionprops
from skimage.morphology import (opening, closing)
from skimage.morphology import disk
import matplotlib.pyplot as plt

# open the fruit image
fruit_image = img_as_ubyte(Image.open("fruit.PNG").convert("1"))
open = opening(fruit_image)
close = closing(open, img_as_ubyte(disk(3)))

label_img = label(close)
region = regionprops(label_img)

# show the result
fig1, ax1 = plt.subplots(nrows=1, ncols=3)

ax1[0].imshow(fruit_image, cmap="gray")
ax1[0].axis('off')
ax1[0].title.set_text('Fruit image')

ax1[1].imshow(open, cmap="gray")
ax1[1].axis('off')
ax1[1].title.set_text('Opening')

ax1[2].imshow(close, cmap="gray")
ax1[2].axis('off')
ax1[2].title.set_text('Closing')

fig2, ax2 = plt.subplots(nrows=1)
ax2.imshow(close, cmap="gray")
ax2.axis('off')
for props in region:
    y0, x0 = props.centroid
    orientation = props.orientation
    x1 = x0 + math.cos(orientation) * 0.5 * props.axis_minor_length
    y1 = y0 - math.sin(orientation) * 0.5 * props.axis_minor_length
    x2 = x0 - math.sin(orientation) * 0.5 * props.axis_major_length
    y2 = y0 - math.cos(orientation) * 0.5 * props.axis_major_length

    minr, minc, maxr, maxc = props.bbox
    bx = (minc, maxc, maxc, minc, minc)
    by = (minr, minr, maxr, maxr, minr)
    ax2.plot(bx, by, '-r', linewidth=1)

plt.show()