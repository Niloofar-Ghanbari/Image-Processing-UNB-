# Q3
# Part a):
# watershed with compactness is a useful initial segmentation but too
  # fine as a final result. this causes the oversegmentation metrics to shoot up.
  # This method of watershed segmentation tries to ensure that the regions produced
  # by the segmentation are as compact as possible, by minimizing their perimeter
  # while still keeping the boundaries meaningful.

# Canny edge filter is a popular method for detecting edges in an image.
  # This algorithm uses a multi-stage approach to identify edges,
  # first by smoothing the image using a Gaussian filter,
  # then by computing the gradient magnitude and orientation,
  # and finally by applying non-maximum suppression and hysteresis thresholding
  # to obtain the final edge map.

# morphological geodesic active contours is a method that generally produces good results,
  # but requires a long time to converge on a good answer.
  #are a method for extracting meaningful boundaries from an image,
  # based on the concept of a geodesic distance. The method works by computing
  # the distance between each pixel in the image and a set of seed points,
  # and then defining a boundary as the set of pixels where this distance is minimized.

# part b):
# The adapted Rand error and the variation of information are used for the evaluation
 #The adapted Rand errorfunction outputs:
 # The adapted Rand precision: this is the number of pairs of pixels that have the same label in the test label image and in the true image, divided by the number in the test image.
 # The adapted Rand recall: this is the number of pairs of pixels that have the same label in the test label image and in the true image, divided by the number in the true image.
 # The variation of information:
 #vi:ndarray of float, shape (2,)
 #The conditional entropies of image1|image0 and image0|image1.

# part c): The results show that the Canny filter method performed the best,
        # with the lowest adapted Rand error and the highest precision and recall. The other two methods,
        # Compact watershed and Morphological Geodesic Active Contours,
        # had higher error rates and were more prone to oversegmentation or undersegmentation.
        # Overall, the choice of segmentation method will depend on the specific needs of the application,
        # and the evaluation metrics used can help identify the most accurate and suitable method.

# part d): Based on the given information, increasing the parameter "iterations" from 10 to 250 improves the results of the segmentation.
           # This can be observed from the decrease in the Adapted Rand error and false splits and merges metrics as the number of iterations increases.
           # However, increasing the iterations beyond 250 does not appear to have a significant impact on the results.
           # The Adapted Rand error, precision, and recall, as well as false splits and merges, remain relatively constant for iterations 300 to 500.
           # It is worth noting that the optimal number of iterations may depend on the specific image being segmented and the chosen parameters of the morphological_geodesic_active_contour() function.
           # Therefore, it may be useful to try a range of values for iterations and compare the results to determine the best choice for a specific application.

# part e):

"""
===============================
Evaluating segmentation metrics
===============================

When trying out different segmentation methods, how do you know which one is
best? If you have a *ground truth* or *gold standard* segmentation, you can use
various metrics to check how close each automated method comes to the truth.
In this example we use an easy-to-segment image as an example of how to
interpret various segmentation metrics. We will use the the adapted Rand error
and the variation of information as example metrics, and see how
*oversegmentation* (splitting of true segments into too many sub-segments) and
*undersegmentation* (merging of different true segments into a single segment)
affect the different scores.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from PIL import Image
from skimage.metrics import (adapted_rand_error,
                              variation_of_information)
from skimage.filters import sobel
from skimage.measure import label
from skimage.util import img_as_float
from skimage.feature import canny
from skimage.morphology import remove_small_objects
from skimage.segmentation import (morphological_geodesic_active_contour,
                                  inverse_gaussian_gradient,
                                  watershed,
                                  mark_boundaries)

original_img = Image.open("fruit_gray.png")
gray_img = np.array(original_img.convert("L"))


elevation_map = sobel(gray_img)
markers = np.zeros_like(gray_img)
markers[gray_img < 50] = 1
markers[gray_img > 120] = 2
im_true = watershed(elevation_map, markers)
im_true = ndi.label(ndi.binary_fill_holes(im_true - 1))[0]

#

edges = sobel(gray_img)
im_test1 = watershed(edges, markers=468, compactness=0.001)

edges = canny(gray_img)
fill_fruit = ndi.binary_fill_holes(edges)
im_test2 = ndi.label(remove_small_objects(fill_fruit, 21))[0]



image = img_as_float(gray_img)
gradient = inverse_gaussian_gradient(image)
init_ls = np.zeros(image.shape, dtype=np.int8)
init_ls[10:-10, 10:-10] = 1
im_test3 = morphological_geodesic_active_contour(gradient, num_iter=20,
                                                 init_level_set=init_ls,
                                                 smoothing=5, balloon=-1,
                                                 threshold=0.6)
im_test3 = label(im_test3)

method_names = ['Compact watershed', 'Canny filter',
                'Morphological Geodesic Active Contours']
short_method_names = ['Compact WS', 'Canny', 'GAC']

precision_list = []
recall_list = []
split_list = []
merge_list = []
for name, im_test in zip(method_names, [im_test1, im_test2, im_test3]):
    error, precision, recall = adapted_rand_error(im_true, im_test)
    splits, merges = variation_of_information(im_true, im_test)
    split_list.append(splits)
    merge_list.append(merges)
    precision_list.append(precision)
    recall_list.append(recall)
    print(f'\n## Method: {name}')
    print(f'Adapted Rand error: {error}')
    print(f'Adapted Rand precision: {precision}')
    print(f'Adapted Rand recall: {recall}')
    print(f'False Splits: {splits}')
    print(f'False Merges: {merges}')

fig, axes = plt.subplots(2, 3, figsize=(9, 6), constrained_layout=True)
ax = axes.ravel()

ax[0].scatter(merge_list, split_list)
for i, txt in enumerate(short_method_names):
    ax[0].annotate(txt, (merge_list[i], split_list[i]),
                   verticalalignment='center')
ax[0].set_xlabel('False Merges (bits)')
ax[0].set_ylabel('False Splits (bits)')
ax[0].set_title('Split Variation of Information')

ax[1].scatter(precision_list, recall_list)
for i, txt in enumerate(short_method_names):
    ax[1].annotate(txt, (precision_list[i], recall_list[i]),
                   verticalalignment='center')
ax[1].set_xlabel('Precision')
ax[1].set_ylabel('Recall')
ax[1].set_title('Adapted Rand precision vs. recall')
ax[1].set_xlim(0, 1)
ax[1].set_ylim(0, 1)

ax[2].imshow(mark_boundaries(image, im_true))
ax[2].set_title('True Segmentation')
ax[2].set_axis_off()

ax[3].imshow(mark_boundaries(image, im_test1))
ax[3].set_title('Compact Watershed')
ax[3].set_axis_off()

ax[4].imshow(mark_boundaries(image, im_test2))
ax[4].set_title('Edge Detection')
ax[4].set_axis_off()

ax[5].imshow(mark_boundaries(image, im_test3))
ax[5].set_title('Morphological GAC')
ax[5].set_axis_off()

plt.show()


# part f): The line “im_test2 = ndi.label(remove_small_objects(fill_coins, 21))[0]” uses two functions from the ndimage module of the scipy library: ndi.label() and ndi.remove_small_objects().
# The ndi.label() function labels connected regions of an array with unique integers starting from 1. It takes an array as input and returns a tuple consisting of two arrays: the first array is the labeled image and the second array is the number of labels.
# The ndi.remove_small_objects() function removes connected regions from an array that have fewer pixels than a given size. It takes an array and a minimum size as input and returns the input array with small connected regions removed.
# In this specific case, the “fill_coins” binary image obtained using the canny edge filter is passed as input to the ndi.remove_small_objects() function with a minimum size of 21 pixels. This removes small noisy regions from the image, leaving only the larger and more significant edges. The resulting image is then labeled using ndi.label(), and the label “0” is selected from the labeled image. The labeled image is used in the later steps to evaluate the performance of the segmentation methods.