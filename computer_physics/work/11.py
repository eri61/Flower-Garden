from math import gamma

import numpy as np


def n_dim_sphere(n, Nmax):
    # n: dimension
    distance = np.zeros(Nmax)
    for i in range(1, n+1):
        q = np.random.random(Nmax)
        distance = distance + q**2
    count = (distance <= 1).sum()
    area = 2**(n) * count / Nmax
    return area


Nmax = int(1e6)
n = 4
area = n_dim_sphere(n, Nmax)
theoretical_area = np.pi**(n/2) / gamma(n/2 + 1)

print(f"v4d={area}")
print(f"v4d_exac={theoretical_area}")
