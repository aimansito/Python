import numpy as np

#1. Crea un array 1D con 168 valores aleatorios(np.random.seed(42)) np.random.uniform(15,35,168)
np.random.seed(42)

arrayEj = np.random.uniform(15, 35, 168)


#2. Reshapealo a (24,7) (24x7) horas x dias e inspecciona su shape
arrayShape = arrayEj.reshape(24, 7)


#3. Transponlo a (7,24) dias x horas usando .T.
arrayT = arrayShape.T 

#4. Convierte el array 1D original en vector columna (168, 1) listo para Sciki-learn
arrayColumna = arrayEj.reshape(-1,1)


#5. Verifica con .shape que cada transformacion produce el shape esperado 

print("Shape original:", arrayEj.shape)
print("Shape 24x7:", arrayShape.shape)
print("Shape transpuesto:", arrayT.shape)
print("Shape vector columna:", arrayColumna.shape)