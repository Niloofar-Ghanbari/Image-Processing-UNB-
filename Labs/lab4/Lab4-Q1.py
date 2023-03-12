import numpy as np
from scipy.signal import convolve2d
# Part a):
I = np.array([[5, 4, 0, 3], [6, 2, 1, 8], [7, 9, 4, 2], [8, 3, 6, 1]])
G = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16

# Convolve I with G using convolve2d
I_G = convolve2d(I, G, mode='same', boundary='symm')

print(I_G)

# Part b):

"""
As we can see, the results are the same in both cases.
This is because convolution is associative,
which means that the order of convolutions does not matter as long as we use the same kernel.
In this case, the separable version of the kernel is equivalent to the original kernel,
so the results are the same regardless of the order of convolution.
"""
# Horizontal kernel
h_kernel = np.array([1, 2, 1]) / 4

# Vertical kernel
v_kernel = np.array([1, 2, 1]) / 4

# Convolve horizontally first, then vertically
I_h = convolve2d(I, h_kernel[np.newaxis], mode='same', boundary='symm')
I_hv = convolve2d(I_h, v_kernel[np.newaxis].T, mode='same', boundary='symm')

# Convolve vertically first, then horizontally
I_v = convolve2d(I, v_kernel[np.newaxis].T, mode='same', boundary='symm')
I_vh = convolve2d(I_v, h_kernel[np.newaxis], mode='same', boundary='symm')

print(I_hv)
print(I_vh)

# Part c):
"""
Yes, the results from (a) and (b) are the same. 
This is because the original kernel G and the separable version of the kernel both represent the same convolution operation.
When we convolve the image I with G directly,
 it is equivalent to convolving it first with the horizontal kernel and then with the vertical kernel.
Similarly, when we convolve the image I with the separable kernel
by first convolving with the vertical kernel and then with the horizontal kernel,
it is equivalent to convolving it directly with G.
Therefore, the results obtained from both methods should be the same.
"""