# importing numpy module
import numpy as np

A = np.array([[1, 1, 1, 0],
             [0, 1, 0, 0],
             [1, 1, 1, 0],
             [0, 0, 0, 0]], dtype=np.bool_)

B = np.array([[0, 0, 0, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 1],
             [0, 1, 0, 1]], dtype=np.bool_)

union = np.logical_or(A, B)
intersection = np.logical_and(A, B)
reflection = np.fliplr(np.flipud(B))
complement = np.logical_not(A)
difference = np.logical_and(A, np.logical_not(B))

# logical operations between integer values
print("A:\n", A)
print("B:\n", B)
print("Union of A and B:\n", union)
print("Intersection of A and B:\n", intersection)
print("Reflection B:\n", reflection)
print("Complement of A:\n", complement)
print("Difference of A and B:\n", difference)







