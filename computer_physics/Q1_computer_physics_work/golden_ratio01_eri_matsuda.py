from functools import cache

import matplotlib.pyplot as plt
import numpy as np


@cache
def fibo(n: int) -> int:
    if n > 1:
        f_p = fibo(n-1) + fibo(n-2)
    else:
        f_p = n
    return f_p


# Get the Fibonacci sequence
np.random.seed(seed=0)
y = np.random.rand(100)
x = range(1, 101)           # numpyを使用するとfor分でoverflowが起こるため注意
for i, val in enumerate(x):
    y[i] = fibo(val+1) / fibo(val)


# plot
plt.plot(x, y)
plt.show()
