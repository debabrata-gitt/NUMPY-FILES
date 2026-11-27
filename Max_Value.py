import numpy as np

a = np.array([[10, 20, 30],
              [40, 50, 60],
              [15, 25, 35]])

result = np.max(a, axis=0)

print("Column Maximum:", result)