import numpy as np

arr = np.array([10, np.nan, 30, np.nan])

result = np.isnan(arr)

print("NaN Check:", result)