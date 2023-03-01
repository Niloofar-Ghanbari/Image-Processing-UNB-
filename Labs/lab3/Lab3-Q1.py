import numpy as np
from skimage.filters import threshold_isodata, threshold_otsu, threshold_local
import matplotlib.pyplot as plt
from PIL import Image

# Define the image
img = np.array([[6, 5, 8, 7], [4, 2, 3, 8], [1, 8, 6, 1]])

# Compute an image threshold using the Ridler-Calvard algorithm
t_ridlercalvard = threshold_isodata(img)

# Compute an image threshold using the Otsu's method
t_Otsu = threshold_otsu(img)

print("Optimal threshold using Ridler-Calvard method = " + str(
    t_ridlercalvard) + "  =>  Rounded threshold (Ridler-Calvard) = " + str(round(t_ridlercalvard)))
print("Optimal threshold using Otsu's method = " + str(t_Otsu) + "  =>  Rounded threshold (Otsu) = " + str(round(t_Otsu)))

original_img = Image.open("dog.png")
dog_img = np.array(original_img.convert("L"))

t_ridlercalvard_dog = threshold_isodata(dog_img)
t_Otsu_dog = threshold_otsu(dog_img)

binary_rc = dog_img > t_ridlercalvard_dog
binary_ot = dog_img > t_Otsu_dog

block_size = 35
local_thresh = threshold_local(dog_img, block_size, offset=10)
binary_local = dog_img > local_thresh
# Plotting the result
fig, ax = plt.subplots(nrows=4, ncols=1, figsize=(7, 8))

ax[0].imshow(dog_img, cmap="gray")
ax[0].axis('off')
ax[0].title.set_text('Original Image')

ax[1].imshow(binary_rc, cmap="gray")
ax[1].axis('off')
ax[1].title.set_text('Ridler-Calvard algorithm')

ax[2].imshow(binary_ot, cmap="gray")
ax[2].axis('off')
ax[2].title.set_text('Otsu method')

ax[3].imshow(binary_local, cmap="gray")
ax[3].axis('off')
ax[3].title.set_text('Local thresholding')

plt.show()

# comment:
# c) Which method works better? Why? IN dog image, the output of the Ridler-Calvard algorithm and output of Otsu's method are almost the same and indistinguishable.
# d) Which method works better? Why? The global thresholding has better result in this image because the image noise characteristics does not vary across the dog image.