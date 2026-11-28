import numpy as np

a = np.array([[2, 3, 4],
              [5, 6, 7]])

result = np.prod(a, axis=0)

print("Column Products:", result)