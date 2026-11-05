##Simulacion Mont carlo estimacion de pi
#1 fija la semilla aleatorioa con np.random.seed(42)
#2 genera 10.000 coordenadas x e y aleatorias ente 0 y 1 usando np.random.random()
#3 calcula el cuadrado de la distancia al origen(x al cuadrado + y al cuadrado) para cada punto
#4 cuenta cuantos puntos caen dentro del circulo unitario (condicion x al cuadrado + y al cuadrado <_ 1 )
# 5 estima pi con la formula  pi = 4 x puntos dentro/puntos totales
##

import numpy as np 

#fijar la semilla

np.random.seed(42)


#Genera 10.000 filas y 2 columnas con valores
n = 10000
x = np.random.random(n)
y = np.random.random(n)

#calcula el cuadrad de la distancia al origen (x al cuadrado y y al cuadrado)