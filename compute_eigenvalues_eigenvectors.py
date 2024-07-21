import numpy as np


def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors


A = np.array([[4, 0.2], [0.1, 0.8]])
result = compute_eigenvalues_eigenvectors(A)
print(result)
