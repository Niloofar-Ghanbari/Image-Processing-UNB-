
height = 480
width = 640
(x1, y1) = (38, 52)
(x2, y2) = (592, 241)
(x3, y3) = (33, 0)
# 2D to 1D coordinates
def i(x, y, width):
    return x+y*width

print("i1: " + str(i(x1, y1, width)))
print("i2: " + str(i(x2, y2, width)))
print("i3: " + str(i(x3, y3, width)))


# 1D index to 2D coordinates
def coordinate(i, width):
    return (i % width, i // width)


print("Point_a:" + str(coordinate(8092, width)))
print("Point_b: " + str(coordinate(24061, width)))
print("Point_c: " + str(coordinate(38190, width)))

