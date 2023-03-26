import numpy as np
from scipy import integrate


def circle_trajectory(x):
    y = np.sqrt(1 - x**2)
    return y


integ, err = integrate.quad(circle_trajectory, 0, 1)
area = 4 * integ
print(f"pi= {area}")
print(f"error= {err}")
