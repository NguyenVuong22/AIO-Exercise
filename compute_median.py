import numpy as np


def compute_median(X):
    size = len(X)
    X = np.sort(X)
    print(X)

    if (size % 2 == 0):
        median = (X[int(size/2)-1] + X[int(size/2)])/2

    else:
        median = X[(int(size + 1)/2) - 1]
    return median


X = [1, 5, 4, 4, 9, 13]
print(" Median : ", compute_median(X))
