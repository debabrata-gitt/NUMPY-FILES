import numpy as np

a = np.array([[10, 20, 30],
              [40, 50, 60],
              [15, 25, 35]])

result = np.min(a, axis=1)

print("Row Minimum:", result)