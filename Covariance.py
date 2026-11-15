import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 4, 6, 8, 10])

result = np.cov(a, b)

print("Covariance Matrix:")
print(result)