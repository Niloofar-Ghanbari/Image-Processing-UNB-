import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Creating the 4*5 NumPy Array
image_array = np.array([[224, 49, 100, 24, 250],
                        [78, 120, 53, 82, 155],
                        [170, 22, 38, 9, 88],
                        [98, 47, 77, 36, 134]])

# rows = 4
# columns = 5

img = Image.fromarray(image_array)
plt.imshow(img)
plt.show()

