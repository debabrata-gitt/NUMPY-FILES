import numpy as np

a = np.array([10, 20, 30, 40])

np.put(a, [1, 3], [100, 200])

print("Updated Array:", a)