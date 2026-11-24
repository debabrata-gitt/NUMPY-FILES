import numpy as np

a = np.array([1, 2, 3])

b = np.pad(a, (2, 2), mode='constant')

print("Original Array:", a)
print("Padded Array:", b)