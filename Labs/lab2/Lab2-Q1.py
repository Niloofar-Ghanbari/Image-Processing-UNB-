# Lab 2- Question 1

import math
import numpy as np
import matplotlib.pyplot as plt

from skimage import data
from skimage import transform
from skimage import img_as_float


# Part a:

# Print out the transformation matrix
tform = transform.SimilarityTransform(scale=0.5, rotation=math.pi*3/8,
                                       translation=(20, 30))
print(tform.params)

# Using an image to visualize the transformation
img = img_as_float(data.coffee())
tf_img = transform.warp(img, tform.inverse)

fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].imshow(img)
ax[0].title.set_text('Original Image')

ax[1].imshow(tf_img)
ax[1].title.set_text('Similarity transformation')

plt.show()

# part b:
matrix = np.array([[1, -0.5, 100],
                   [0.1, 0.9, 50],
                   [0.0015, 0.0015, 1]])
tform = transform.ProjectiveTransform(matrix=matrix)
tf_img = transform.warp(img, tform.inverse)

fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].imshow(img)
ax[0].title.set_text('Original Image')

ax[1].imshow(tf_img)
ax[1].title.set_text('Projective transformation')
plt.show()