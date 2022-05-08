import sys
from functools import lru_cache

import matplotlib.pyplot as plt
import numpy as np

sys.setrecursionlimit(15000)


@lru_cache(128)
def fibo(n: int) -> int:
    if n > 1:
        f_p = fibo(n-1) + fibo(n-2)
    else:
        f_p = n
    return f_p


np.random.seed(seed=0)
y = np.random.rand(100)
x = range(1, 101)           # numpyを使用するとfor分でoverflowが起こるため注意

for i, val in enumerate(x):
    y[i] = fibo(val+1) / fibo(val)
plt.plot(x, y)
plt.show()
