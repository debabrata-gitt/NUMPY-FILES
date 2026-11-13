import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

result = np.max(arr, axis=1)

print("Maximum of Each Row:", result)