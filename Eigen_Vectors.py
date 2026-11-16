import numpy as np

arr = np.array([[2, 0],
                [0, 3]])

values, vectors = np.linalg.eig(arr)

print("Eigenvalues:", values)
print("Eigenvectors:")
print(vectors)