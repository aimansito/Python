import numpy as np

#1. fija np.random.seed(42) y crea una matriz 20x5 con calificaciones aleatorias: np.random.uniform(0,10,(20,5)) 
np.random.seed(42)
numRandom = np.random.uniform(0,10,(0,20))

print(numRandom[:5])
#2.Normaliza las notas por asignatura (z-score): resta la media y divide por la desviacion estandar de cada asignatura
media_asign = np.mean(numRandom, axis = 0)
std_asign = np.std(numRandom, axis = 0)
notas_zscore = (numRandom - media_asign) / std_asign

print(notas_zscore[:5])
#3. Calcula la desviacion de cada estudiante respecto a la media de su clase
media_estudiante = np.mean(numRandom, axis = 1)
media_global = np.mean(numRandom)
desviacion_estudiantes = media_estudiante - media_global
print(desviacion_estudiantes)
#4.Aplica una curva de ajusta (bonus de +0.5) solo a las asignaturas cuya media sea inferior a ti
notas_ajuste = numRandom.copy()

asignaturas_bajas = media_asign < 5.0

