import numpy as np

arr = np.array([10, 60, 30, 80, 40])

result = np.where(arr > 50, 0, arr)

print("Updated Array:", result)