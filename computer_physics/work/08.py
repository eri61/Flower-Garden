import matplotlib.pyplot as plt
import numpy as np


def draw_trajectory(v0: float, theta: float) -> None:
    g: float = 9.8
    t_flight = 2 * v0*np.sin(theta) / g

    # 配列計算→numpy推奨です
    t = np.linspace(0., t_flight, 1000)
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - g * t ** 2 / 2
    draw_graph(x, y)


def get_max_height(x: np.ndarray, y: np.ndarray):
    # 最高到達点の座標(x,y)を返す
    return x[y.argmax()], y.max()


def draw_graph(x: np.ndarray, y: np.ndarray):
    max_height = get_max_height(x, y)   # return (x, y)
    print(max_height)
    plt.plot(x, y)
    plt.xlabel("x-coordinate")
    plt.ylabel("y-coordinate")
    plt.title("Trajectory of a ball")
    plt.plot(max_height[0], max_height[1], 'o')
    plt.show()


try:
    v0 = float(input("Enter the initial speec (m/s): "))
    theta = float(input("Enter the initial angle (degrees): "))
except ValueError:
    print("You enterd an invalid input")
else:
    theta = np.deg2rad(theta)
    draw_trajectory(v0, theta)
