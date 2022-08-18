import numpy as np

K = 0.1
t = np.array([[np.exp(K), np.exp(-K)],
            [np.exp(-K), np.exp(K)]])
T = t @ t @ t @ t @ t
print(f"Sum T_ij = {T.sum()}")
