import numpy as np

arr = np.array([5, 15, 25, 35, 45, 55])

result = arr[(arr < 20) | (arr > 40)]

print("Selected Values:", result)