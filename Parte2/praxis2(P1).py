import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

class CurvaBezierInteractiva:
    #preparar todo para interactuar correctamente con el mouse
    def __init__(self, controlar_puntos):
        self.controlar_puntos= np.array(controlar_puntos, dtype=float)
        self.puntos_curva= None
        self.seleccion_puntos= None
        self.figura, self.ax= plt.subplots()        
        self.actualizar= self.ax.scatter(self.controlar_puntos[:,0], self.controlar_puntos[:,1], c='r', label='controlar puntos')#crea un grafico de dispercion
        self.click= self.figura.canvas.mpl_connect('button_press_event', self.press_click)#para precionar el click en la figura
        self.mover= self.figura.canvas.mpl_connect('motion_notify_event', self.mover_mouse)#para mover los puntos con el mouse en la figura
        self.soltar= self.figura.canvas.mpl_connect('button_release_event', self.soltar_click)#para soltar la figura
        self.update_curva() 
        
    #verifica el area de la figura y si el click esta dentro determina cual de control esta mas cerca
    def press_click(self, event):
        if event.inaxes== self.ax:
            self.seleccion_puntos= self.punto_mas_cerca(event.xdata, event.ydata)
    
    #verifica, actualiza los puntos de control y redibuja la curva
    def mover_mouse(self, event):
        if event.inaxes== self.ax and self.seleccion_puntos is not None:
            self.controlar_puntos[self.seleccion_puntos]=[event.xdata, event.ydata] 
            self.update_curva()
            
    def soltar_click(self, event):
        self.seleccion_puntos=None
    
    #calcula las distancias euclidianas en x,y , encuentra el indice que tiene la menor distancia en x,t
    def punto_mas_cerca(self, x,y):
        distancia= np.sqrt(np.sum((self.controlar_puntos - np.array([x,y]))**2, axis=1))
        return np.argmin(distancia)
    
    #calcula los puntos que forman la curva de Bezier 
    def curva_Bezier(self, t):
        n=len(self.controlar_puntos)-1 #calcula el grado de la curva 
        curva= np.zeros_like(self.controlar_puntos[0])
        for i in range(n+1):
            curva += self.controlar_puntos[i]* comb(n,i)* ((1-t)**(n-i))*(t**i)#calcula el termino de la curva de Bezier correspontiente a punto de control
        return curva
    
    #mantiene la grafica actualizada y muestra cualquier cambio en los puntos
    def update_curva(self):
        valor_t= np.linspace(0,1,100)
        self.puntos_curva= np.array([self.curva_Bezier(t) for t in valor_t])
        self.actualizar.set_offsets(self.controlar_puntos)
        self.ax.clear()
        self.ax.plot(self.puntos_curva[:,0], self.puntos_curva[:,1], label='Curva de Bezier', color='blue')
        self.ax.scatter(self.controlar_puntos[:,0], self.controlar_puntos[:,1], label='Puntos de Control', color='red')
        self.ax.set_title('~Curva de Bézier~')
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.legend()
        self.ax.axis('equal')    
        self.ax.grid(True)
        plt.draw()
            
Puntos_iniciales= [[0,0],[1,2],[3,4],[5,0]]
curva_interactiva= CurvaBezierInteractiva(Puntos_iniciales)
plt.show()               