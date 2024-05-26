import numpy as np
from mayavi import mlab

# Superficie parametrica
u = np.linspace(np.pi / 6, np.pi / 2, 100)
v = np.linspace(-np.pi / 2, np.pi, 100)
u, v = np.meshgrid(u, v)

x = np.sin(u) * np.cos(v)
y = np.sin(u) * np.sin(v)
z = np.cos(u)
#

# Trayectoria de la hormiga
t = np.linspace(0, np.pi/2, 100)
x_traj = (np.sqrt(3) / 2) * np.sin(t)
y_traj = np.full_like(t, 1 / 2)
z_traj = (np.sqrt(3) / 2) * np.cos(t)
#

# Limites de la superficie
u_min = np.pi / 6
u_max = np.pi / 2

v_min = -np.pi / 2
v_max = np.pi
#

# Verificar si un punto de la trayectoria esta en la superficie
def dentro_rango(x, y, z, u_min, u_max, v_min, v_max):
    sin_u = np.sqrt(x**2 + y**2)
    if sin_u < np.sin(u_min) or sin_u > np.sin(u_max):
        return False
    v = np.arctan2(y, x)
    if v < v_min or v > v_max:
        return False
    return True
#

# Calcular el valor maximo de t dentro de la superficie
max_t = None
puntos_salida = None

for i in range(len(t)):
    if not dentro_rango(x_traj[i], y_traj[i], z_traj[i], u_min, u_max, v_min, v_max):
        break
    max_t = round(t[i], 3)
    puntos_salida = (round(x_traj[i], 3), round(y_traj[i], 3), round(z_traj[i], 3))

if max_t is not None:
    print(f"La hormiga permanece en la superficie hasta t = {max_t}, en el punto {puntos_salida}")
else:
    print("La hormiga permanece en la superficie durante todo el intervalo considerado.")
#


#parte grafica
mlab.figure(bgcolor=(0.15, 0.15, 0.15))

# Grafica de la trayectoria
mlab.plot3d(x_traj, y_traj, z_traj, color=(0, 1, 0), tube_radius=0.02, line_width=1)

# Grafica del punto de salida
if puntos_salida is not None:
    mlab.points3d(puntos_salida[0], puntos_salida[1], puntos_salida[2], color=(1, 0, 0), scale_factor=0.1)

# Configurar los ejes
mlab.axes(xlabel='eje X', ylabel='eje Y', zlabel='eje Z')

# Grafica de la superficie
mlab.mesh(x, y, z, color=(1, 0, 1), opacity=0.8)

mlab.outline()

# Mostrar el gráfico
mlab.show()
#