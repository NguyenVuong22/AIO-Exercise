import numpy as np


def matrix_multi_vector(matrix, vector):
    result = matrix.dot(vector)

    return result


matrix = np.array([[-1, 1, 1], [0, -4, 9]])
vector = np.array([0, 2, 1])
result = matrix_multi_vector(matrix, vector)
print(result)
