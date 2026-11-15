import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([20, 40, 50, 60])

result = np.intersect1d(a, b)

print("Common Elements:", result)