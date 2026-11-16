import numpy as np

arr = np.array([10, 20, 10, 30, 20, 10])

values, counts = np.unique(arr, return_counts=True)

print("Unique Values:", values)
print("Counts:", counts)