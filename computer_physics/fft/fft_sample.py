import matplotlib.pyplot as plt
import numpy as np

N = 1000
n = np.arange(N)
freq = 3        # period
f = np.sin(freq * 2 * np.pi * (n/N)) + np.sin(5 * 2 * np.pi * (n/N)) + np.sin(1/7 * 2 * np.pi * (n/N))
F = np.fft.fft(f)

plt.figure(figsize=(6, 3))
plt.plot(f)

plt.figure(figsize=(6, 3))
plt.plot(np.abs(F))
plt.scatter(n, np.abs(F))
plt.xlim(0, 30)
plt.show()
plt.clf()
