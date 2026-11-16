import numpy as np

arr = np.array([[1, 2],
                [3, 4]])

result = np.linalg.matrix_power(arr, 2)

print(result)