import numpy as np
from PIL import Image


I1 = np.array([[18, 168, 94, 97],
               [120, 97, 78, 198],
               [83, 70, 208, 17],
               [238, 208, 189, 68]])

I2 = np.array([[21, 168, 92, 71],
               [122,71,191,227],
               [83, 212, 16, 187],
               [240, 216, 188, 68]])

I3 = np.array([[20, 171, 92, 70],
               [76, 193, 39, 255],
               [209, 20, 20, 194],
               [241, 210, 190, 73]])
# calculating double difference
def compute_double_difference(img0, img1, img2, T):
    columns = img0.shape[0]
    rows = img0.shape[1]
    double_difference = np.full((rows, columns), 0)

    d1 = abs(img0 - img1)
    d2 = abs(img1 - img2)


    for x in range(columns):
        for y in range(rows):

           if (d1[y][x] > T and d2[y][x] > T):
            double_difference[y][x] = 255
           else:
            double_difference[y][x] = 0

    return double_difference


# calculating triple difference

def compute_triple_difference(img0, img1, img2, T):
    columns = img0.shape[0]
    rows = img0.shape[1]
    triple_difference = np.full((rows, columns), 0)

    d1 = abs(img0 - img1)
    d2 = abs(img2 - img1)
    d3 = abs(img2 - img0)


    for x in range(columns):
        for y in range(rows):
            if ((d1[y][x] + d2[y][x] - d3[y][x]) > T):
                triple_difference[y][x] = 255
            else:
                triple_difference[y][x] = 0

    return triple_difference


d_difference = compute_double_difference(I1, I2, I3, 40)
t_difference = compute_triple_difference(I1, I2, I3, 40)
print("Double difference is:")
print(d_difference)
d_difference_img = Image.fromarray(d_difference)
d_difference_img.show()

print("Triple difference is:")
print(t_difference)
t_difference_img = Image.fromarray(t_difference)
t_difference_img.show()












