import numpy as np

a = np.array([10, 20, 30, 40, 50])

b = np.take(a, [0, 2, 4])

print("Original Array:", a)
print("Selected Elements:", b)