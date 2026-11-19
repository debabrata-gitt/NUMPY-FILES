import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

result = np.diagonal(arr).sum()

print("Diagonal Sum:", result)