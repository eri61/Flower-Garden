import matplotlib.pyplot as plt
import numpy as np


def trajectory_graph_settings(func):
    # func -> x, y のndarrayが帰ってくる関数
    def wrapper(*args, **kargs) -> None:
        x, y = func(*args, **kargs)
        max_index = y.argmax()
        x_max, y_max = x[max_index], y[max_index]
        print(f"maximum height; {y_max}")
        plt.figure(figsize=(7, 4))
        plt.xlabel("x-coordinate")
        plt.ylabel("y-coordinate")
        plt.title("Trajectory of a ball")
        plt.plot(x, y, color='c', zorder=1, label='trajectory')
        plt.scatter(x_max, y_max, marker='o',
                    s=30, c='m', zorder=2, label='maximum height')
        plt.legend()
        plt.show()
    return wrapper


@trajectory_graph_settings
def draw_trajectory(
    v0, theta, g=9.8
) -> np.ndarray:

    t_flight = 2 * v0 * np.sin(theta) / g
    t = np.arange(0, t_flight, 0.001)
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - g * t**2 / 2
    return x, y


try:
    v0 = float(input("Enter the initial speec (m/s): "))
    theta = float(input("Enter the initial angle (degrees): "))
except ValueError:
    print("You enterd an invalid input")
else:
    theta = np.radians(theta)
    draw_trajectory(v0, theta)
