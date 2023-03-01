import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage.morphology import disk, opening
from skimage.filters import gaussian, sobel
from skimage.segmentation import (morphological_geodesic_active_contour,
                                  inverse_gaussian_gradient, felzenszwalb, slic, watershed)
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float


# Load the image
original_image = Image.open("violin-and-hand.jpg")
gray_image = np.array(original_image.convert("L"))

# Initialize level set for Geodesic Active Contour
init_ls = np.zeros(gray_image.shape, dtype=np.int8)
init_ls[10:-10, 10:-10] = 1

# Preprocess the image for Geodesic Active Contour and Watershed
processed_image = opening(gray_image, disk(2))
processed_image = inverse_gaussian_gradient(processed_image)

# Apply Geodesic Active Contour
ls = morphological_geodesic_active_contour(processed_image, num_iter=500, smoothing=5,
                                           balloon=-1.5, threshold=0.7, init_level_set=init_ls)

# Apply Watershed
gradient = sobel(gray_image)
segments_watershed = watershed(gradient, markers=100, compactness=0.01)

# Apply SLIC
smoothed_image = gaussian(np.array(original_image), 1, preserve_range=False, multichannel=False)
segments_slic = slic(smoothed_image, n_segments=120, compactness=15, sigma=1, start_label=1)

# Apply Felzenszwalb
segments_fz = felzenszwalb(smoothed_image, scale=700, sigma=1, min_size=250)

# Plot the results
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.flatten()

ax[0].imshow(original_image, cmap="gray")
ax[0].contour(ls, [1], colors='b')
ax[0].set_title("Geodesic Active Contour", fontsize=12)
ax[0].set_axis_off()

ax[1].imshow(mark_boundaries(img_as_float(original_image), segments_watershed), cmap="nipy_spectral")
ax[1].set_title("Watershed", fontsize=10)
ax[1].set_axis_off()

ax[2].imshow(mark_boundaries(img_as_float(original_image), segments_slic), cmap="nipy_spectral")
ax[2].set_title("SLIC", fontsize=10)
ax[2].set_axis_off()

ax[3].imshow(mark_boundaries(img_as_float(original_image), segments_fz), cmap="nipy_spectral")
ax[3].set_title("Felzenszwalb", fontsize=10)
ax[3].set_axis_off()

fig.tight_layout()
plt.show()
