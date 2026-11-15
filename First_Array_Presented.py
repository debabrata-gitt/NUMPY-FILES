import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([20, 40, 50])

result = np.setdiff1d(a, b)

print("Difference:", result)