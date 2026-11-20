import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

result = np.median(arr, axis=0)

print("Column Median:", result)