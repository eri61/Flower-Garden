import numpy as np

i0 = 1j

sig_x = np.array([[0, 1, 0, 0], [1, 0, 0, 0],
                  [0, 0, 0, 1], [0, 0, 1, 0]])
sig_y = np.array([[0, -1j, 0, 0], [1j, 0, 0, 0],
                  [0, 0, 0, -1j], [0, 0, 1j, 0]])
sig_z = np.array([[1, 0, 0, 0], [0, -1, 0, 0],
                  [0, 0, 1, 0], [0, 0, 0, -1]])

sXsY = sig_x @ sig_y
isZ = 1j * sig_z
# print(f"sX*sY = {sXsY}")
# print(f"i*sZ = {1j * sig_z}")
print(f"sX*sY = \n{sXsY}")
print(f"i.sZ = \n{sig_z}")
print(
    f"{{sX, sY}} = \n{sig_x @ sig_y + sig_y @ sig_x}"
)
