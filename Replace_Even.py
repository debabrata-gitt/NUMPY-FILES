import numpy as np

a = np.array([10, 15, 20, 25, 30, 35])

a[a % 2 == 0] = 0

print("Updated Array:", a)