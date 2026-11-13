import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

result = np.sum(arr, axis=0)

print("Column Sum:", result)