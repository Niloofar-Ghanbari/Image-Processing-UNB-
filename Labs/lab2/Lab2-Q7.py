import matplotlib.pyplot as plt
from skimage import data, color
from skimage.morphology import (opening, closing)


# Load an image
image = color.rgb2gray(data.astronaut())

# Apply opening and closing operations multiple times

opened1 = opening(image)
opened2 = opening(opened1)
opened3 = opening(opened2)
opened4 = opening(opened3)
opened5 = opening(opened4)

closed1 = closing(image)
closed2 = closing(closed1)
closed3 = closing(closed2)
closed4 = closing(closed3)
closed5 = closing(closed4)

# Plot the original image and the results of opening and closing
fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(8, 3), sharex=True, sharey=True)
ax0.imshow(image, cmap=plt.cm.gray)
ax0.set_title("Original image")

ax1.imshow(opened5, cmap=plt.cm.gray)
ax1.set_title("Opened image")

ax2.imshow(closed5, cmap=plt.cm.gray)
ax2.set_title("Closed image")

plt.tight_layout()
plt.show()


