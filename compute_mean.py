import numpy as np


def compute_mean(X):
    result = np.mean(X)

    return result


X = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]

print("Mean : ", compute_mean(X))
