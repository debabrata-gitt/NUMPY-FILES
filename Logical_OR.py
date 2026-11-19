import numpy as np

arr = np.array([10, 20, 30, 40, 50])

result = np.logical_or(arr < 20, arr > 40)

print("Filtered Values:", arr[result])