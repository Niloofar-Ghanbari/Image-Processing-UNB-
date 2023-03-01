import math

# Define the 5 by 5 image
img = [[4, 2, 8, 10, 20],
    [25, 23, 1, 7, 10],
    [14, 21, 9, 7, 14],
    [22, 17, 2, 11, 24],
    [21, 25, 5, 16, 1]]


# coordinates of the central pixel
center_x = 2
center_y = 2

# Compute the Euclidean distance for each pixel
distances = []
for y in range(len(img)):
    row_distances = []
    for x in range(len(img[y])):
        Euclidean_distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
        row_distances.append(Euclidean_distance)
    distances.append(row_distances)

# Print the distances
print("\nEuclidean_distance: \n")
for row in distances:
    print(row)

# Compute the Manhattan distance for each pixel
distances = []
for y in range(len(img)):
    row_distances = []
    for x in range(len(img[y])):
        Manhattan_distance = abs(x - center_x) + abs(y - center_y)
        row_distances.append(Manhattan_distance)
    distances.append(row_distances)

# Print the distances
print("\nManhattan_distance: \n")
for row in distances:
    print(row)


# Compute the chessboard distance for each pixel
distances = []
for y in range(len(img)):
    row_distances = []
    for x in range(len(img[y])):
        chessboard_distance = max(abs(x - center_x), abs(y - center_y))
        row_distances.append(chessboard_distance)
    distances.append(row_distances)

# Print the distances
print("\nchessboard_distance: \n")
for row in distances:
    print(row)

