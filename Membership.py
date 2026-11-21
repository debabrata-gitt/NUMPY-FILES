import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([20, 40])

result = np.isin(a, b)

print("Membership:", result)
print("Common Elements:", a[result])