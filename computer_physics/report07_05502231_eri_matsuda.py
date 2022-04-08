import matplotlib.pyplot as plt
import numpy as np


def fibo(n):
    if n == 0:
        f_p = 0
    elif n == 1:
        f_p = 1
    else:
        f_p_2 = 0
        f_p_1 = 1
        for p in range(2, n+1):
            f_p = f_p_1 + f_p_2

            f_p_2 = f_p_1
            f_p_1 = f_p

    return f_p


x = np.arange(1, 101)
y_n = np.zeros_like(x).astype(np.float32)
for i in x:
    print(fibo(i+1) / fibo(i))
    y_n[i - 1] = fibo(i+1) / fibo(i)
print(y_n)
plt.plot(x, y_n)
plt.show()
