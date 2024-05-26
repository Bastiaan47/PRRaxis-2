import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#ecuacion del cono
def cono(x, y):
    return np.sqrt(x**2 + y**2), -np.sqrt(x**2 + y**2)

#ecuacion de la curva
def r(t):
    return t * np.cos(t), t * np.sin(t), t

#ecuacion para verificar si la curva se encuentra en el cono
def verificar(t):
    x, y, z = r(t)
    return z**2 - x**2 - y**2

#valores del cono
x = np.linspace(-10, 10, 25)
y = np.linspace(-10, 10, 25)
x, y = np.meshgrid(x, y)
z_positivo, z_negativo = cono(x, y)

#valores de la curva
t = np.linspace(-10, 10, 90)
curva_x, curva_y, curva_z = r(t)

#se verifica la curva sobre el cono, verificando que el valor sea cercano a 0
if np.allclose(verificar(t), 0):
    print("la curva esta en el cono")
else:
    print("la curva no esta en el cono")

#parte grafica
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#grafica de la parte positiva y negativa del cono
ax.plot_surface(x, y, z_positivo, alpha=0.6, color="r") 
ax.plot_surface(x, y, z_negativo, alpha=0.6, color="r") 

#grafica de la curva
ax.plot(curva_x, curva_y, curva_z, color="black")

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
