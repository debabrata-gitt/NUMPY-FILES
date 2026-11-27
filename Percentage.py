import numpy as np

a = np.array([0, 10, 20, 0, 30, 40])

result = (np.count_nonzero(a) / a.size) * 100

print("Non-Zero Percentage:", result)