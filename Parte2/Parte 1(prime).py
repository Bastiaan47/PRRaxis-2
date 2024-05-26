from sympy import symbols, cos, sin, simplify

#definicion variable t
t= symbols('t')

#componentes de la curva
x= t* cos(t)
y= t* sin(t)
z= t

#sustituir ecuacuin del cono
parte_izqd= x**2+y**2
parte_drch= z**2

#simplificar los lados de la ecuacion
simpl_izqd= simplify(parte_izqd)
simpl_drch= simplify(parte_drch)

#verificar si sus lados son iguales
son_iguales= simplify(parte_izqd- parte_drch)
#--------------------------------------------#
#mostrar en consola
print(f"x(t)^2 + y(t)^2 = {simpl_izqd}\n")
print(f"z(t)^2 = {simpl_drch}\n")
print(f"ecuacion simplificada: {son_iguales}\n")

if son_iguales == 0:
    print("La curva se encuentra sobre la superficie de un cono.")
else:
    print("La curva no se encuentra sobre la superficie de un cono.")
    