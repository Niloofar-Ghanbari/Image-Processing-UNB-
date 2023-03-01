import matplotlib.pyplot as plt
import numpy as np
from skimage import transform, img_as_ubyte
from PIL import ImageDraw, Image



src_img = Image.open("Highway billboard.jpg")
dst_img = Image.open("Oil painting.jpg")

src_img_width = src_img.size[0]
dst_img_width = dst_img.size[0]
src_img_height = src_img.size[1]

dst_img = dst_img.resize((src_img_width, src_img_height))

n = src_img_width / dst_img_width

coord1_dst = (n * 600, n * 95)
coord2_dst = (n * 600, n * 1100)
coord3_dst = (n * 1380, n * 970)
coord4_dst = (n * 1380, n * 370)

coord1_src = (330, 140)
coord2_src = (330, 340)
coord3_src = (750, 340)
coord4_src = (740, 120)

src = np.array([coord1_src, coord2_src, coord3_src, coord4_src])
dst = np.array([coord1_dst, coord2_dst, coord3_dst, coord4_dst])

# Calculating the transformation matrix
tform = transform.ProjectiveTransform()
tform.estimate(src, dst)
print("\nTransformation matrix = \n")
print(tform.params)

# Warping the image
dst_img_array = np.array(dst_img)
warped_img_array = transform.warp(dst_img_array, tform, output_shape=(src_img_height, src_img_width))
warped_img = Image.fromarray(img_as_ubyte(warped_img_array))

# Defining the mask
mask_im = Image.new("L", src_img.size, 0)
draw = ImageDraw.Draw(mask_im)
draw.polygon((coord1_src, coord2_src, coord3_src, coord4_src), outline=1, fill=255)

# Pasting the image
src_img.paste(warped_img, (0, 0), mask=mask_im)

fig, ax = plt.subplots(nrows=3, figsize=(20, 10))

ax[0].imshow(dst_img, cmap=plt.cm.gray)
ax[0].plot(dst[:, 0], dst[:, 1], '.r')
ax[1].imshow(warped_img, cmap=plt.cm.gray)
ax[1].plot(src[:, 0], src[:, 1], '.r')
ax[2].imshow(src_img, cmap=plt.cm.gray)
ax[2].plot(src[:, 0], src[:, 1], '.r')
for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()
