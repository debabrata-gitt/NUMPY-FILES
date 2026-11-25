import numpy as np

a = np.array([[10, 20, 30],
              [40, 50, 60]])

result = np.average(a, axis=1)

print("Row Averages:", result)