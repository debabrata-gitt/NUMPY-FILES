import numpy as np

a = np.array([[10, 50, 30],
              [80, 20, 40],
              [5, 60, 15]])

result = np.argmin(a, axis=0)

print("Minimum Index of Each Column:", result)