import numpy as np

x = np.arange(1000, 1500)
x = x[x % 13 == 11]

for i in x:
    print(i)

size = 1000000
x = np.random.random(size)
y = np.random.random(size)
z = np.random.random(size)

area = (x**2 + y**2 + z**2) <= 1
x = x[area]
y = y[area]
circle = (x**2 + y**2) <= 1/2
x = x[circle]
area_size =  x.size * 4 / size
print(f"v_3d= {area_size}")
print(f"v_3d_exac= {np.sqrt(2)/3*np.pi}")


