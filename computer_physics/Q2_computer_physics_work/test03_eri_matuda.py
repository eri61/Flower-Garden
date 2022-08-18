import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, np.pi * 2, 1000)
x = np.sin(2*t)
y = np.sin(3*t)

plt.plot(x, y)
plt.xlabel('sin(2t)')
plt.ylabel('sin(3t')
plt.show()
