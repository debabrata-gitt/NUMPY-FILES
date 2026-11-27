import numpy as np

a = np.array([10, 25, 40, 55, 70])

target = 38

result = a[np.argmin(np.abs(a - target))]

print("Closest Value:", result)