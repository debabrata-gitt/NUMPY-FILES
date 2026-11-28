import numpy as np

a = np.array([[10, 50, 30],
              [80, 20, 40]])

result = np.argmax(a, axis=1)

print("Maximum Index of Each Row:", result)