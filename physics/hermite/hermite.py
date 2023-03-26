import math

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import eval_hermite


def wave_func(n, x):
    norm = np.sqrt(2**n * math.factorial(n) * np.sqrt(np.pi))**(-1)
    H = eval_hermite(n, x)
    wave_func = norm * H * np.exp(-x**2 / 2)
    return wave_func


def classic(n):
    return n + 1/2


def hermite(n):
    x = np.linspace(-7.5, 7.5, 10000)
    y = wave_func(n, x)

    # plot
    text = plt.text(-7.5, 0.5, f"n = {n}", va='top', ha='left', fontsize=12)
    frame = plt.plot(x, y, color='royalblue',
                     label='Hermite polynomial')
    return frame + [text]


hermite(12)
