import numpy as np

matrix = np.random.rand(3, 4)
print(matrix)
print(matrix.mean())

vector = np.arange(10, 50, 10)
print(vector)

res = matrix + vector
print(res)