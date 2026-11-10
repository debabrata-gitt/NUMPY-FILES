import numpy as np

arr = np.arange(1,31).reshape(6,5)

print(arr)

arr3 = arr[3:5, 0:2]
arr4 = arr[3:6, 3:5]

print("First Slicing:")
print(arr3)

print("Second Slicing:")
print(arr4)
