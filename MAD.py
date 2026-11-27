import numpy as np

a = np.array([10, 20, 30, 40])

result = np.mean(np.abs(np.diff(a)))

print("Mean Absolute Difference:", result)