import numpy as np

arr = np.array([10, np.nan, 40, np.nan, 50])

result = np.nan_to_num(arr, nan=0)

print("Updated Array:", result)