import numpy as np

a = np.array([10, 20, 30, 40])
b = np.copy(a)

b[0] = 100

print("Original Array:", a)
print("Copied Array:", b)