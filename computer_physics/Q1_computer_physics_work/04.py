import numpy as np

# 行列演算はnumpyを用いることが計算コストの観点から推奨
# 行列Aの作成
A = np.ones((2, 2))
A[0][1] = -1.

# 逆行列
B = np.linalg.inv(A)

# 内積
c = A @ B       # or A.dot(B), np.dot(A, B)
print(A)
print(B)
print(c)
