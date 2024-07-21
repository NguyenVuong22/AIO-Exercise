import numpy as np


def compute_cosine(v1, v2):
    cos_sin = (np.dot(v1, v2))/((np.linalg.norm(v1))*(np.linalg.norm(v2)))
    return cos_sin


v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

result = compute_cosine(v1, v2)
print(round(result, 3))
