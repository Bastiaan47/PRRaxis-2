import numpy as np
from scipy.integrate import quad

los_puntos_control= [
    np.array([[0, 0], [1, 2], [3, 3], [4, 0]]),
    np.array([[0, 0], [2, 4], [3, 0], [4, 0]]),
    np.array([[0, 0], [1, 1], [2, 1], [3, 0]]),
    np.array([[0, 0], [1, 3], [3, 3], [4, 0]])
]

#calcular la posicion de un punto en la curva
def curva_de_bezier(t, control_puntos):
    n= len(control_puntos)-1
    curva= np.zeros((2,))
    for i in range(n+1):
        coeficiente_bi= np.math.comb(n,i)
        curva+coeficiente_bi* ((1-t)**(n-i))*(t**i)*control_puntos[i]
    return curva

#calcular la derivada de la curva de bezier
def derivada(t, puntos_control):
    n= len(puntos_control)-1
    deriva= np.zeros((2,))
    for i in range(n):
        binomial= np.math.comb(n-1, i)
        deriva += binomial*((1-t)**(n-1-i))*(t**i)*(puntos_control[i+1]- puntos_control[i])*n
    return deriva

#calcular la longitud de la curva
def longitud(puntos_c):
    lam= lambda t: np.linalg.norm(derivada(t, puntos_c))
    long,_= quad(lam, 0, 1)
    return long

#mostrar en consola  
for i, ctrl_p in enumerate(los_puntos_control):
    loong= longitud(ctrl_p)
    print(f"Longitud de la curva de Bezier {i+1}: {loong}")        
    
        
        