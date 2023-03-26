from functools import cache

import matplotlib.pyplot as plt
import numpy as np


# cacheデコレーションを使用することで数列計算が可能です。
# pythonで用意されている関数は(後ろでコンパイラ型言語が動いて)処理が速いです。
@cache
def fibo(n: int) -> int:
    if n > 1:
        f_p = fibo(n-1) + fibo(n-2)
    else:
        f_p = n
    return f_p


# Get the Fibonacci sequence
# 推奨: y[0] = ... 等の追加方法
# 非推奨: y.append()
np.random.seed(seed=0)
y = np.random.rand(100)     # random関数で初期値
x = range(1, 101)           # numpyを使用するとfor分でoverflowが起こるため注意
for i, val in enumerate(x):
    y[i] = fibo(val+1) / fibo(val)


# plot
plt.plot(x, y)
plt.show()
