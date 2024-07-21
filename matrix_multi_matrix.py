import numpy as np


def matrix_multi_matrix(matrix1, matrix2):
    len_of_vector = np.dot(matrix1, matrix2)

    return len_of_vector


m1 = np. array([[0, 1, 2], [2, -3, 1]])
m2 = np. array([[1, -3], [6, 1], [0, -1]])
print(matrix_multi_matrix(m1, m2))
