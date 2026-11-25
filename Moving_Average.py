import numpy as np

a = np.array([10, 20, 30, 40, 50])

window = 3

result = np.convolve(a, np.ones(window)/window, mode='valid')

print("Moving Average:", result)