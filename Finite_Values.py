import numpy as np

a = np.array([10, np.inf, 20, -np.inf, 30])

b = np.isfinite(a)

print("Array:", a)
print("Finite Values:", b)