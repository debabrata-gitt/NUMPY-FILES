import numpy as np

arr = np.array([10, 20, 30, 40, 50])

result = np.logical_and(arr > 15, arr < 45)

print("Condition:", result)
print("Filtered Values:", arr[result])