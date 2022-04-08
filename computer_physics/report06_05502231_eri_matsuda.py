import numpy as np

n = np.arange(50, 151)


def find_prime(func):
    def cnt_division(n: int) -> int:
        m = func(n)
        prime = n % m == 0
        return prime.sum()
    return cnt_division


@find_prime
def num_division(n: int):
    return np.arange(1, n)


cnt = 0
prime = np.zeros(150)
for i in n:
    if num_division(i) == 1:
        prime[cnt] = i
        cnt += 1

prime = prime[prime != 0]
print(prime)
