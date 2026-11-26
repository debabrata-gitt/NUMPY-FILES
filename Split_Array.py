import numpy as np

arr = np.array([10, 20, 30, 40, 50, 70])

result = np.array_split(arr, 4)

for part in result:
    print(part)