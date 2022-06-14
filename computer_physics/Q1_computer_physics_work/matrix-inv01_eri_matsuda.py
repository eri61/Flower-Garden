import numpy as np

a = np.array([[1, -1], [1, 1]])
b = np.linalg.inv(a)

c = a @ b
print(a)
print(b)
print(c)
