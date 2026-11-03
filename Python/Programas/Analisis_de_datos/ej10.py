import numpy as np

arr = np.arange(12)  # Array de 0 a 11
print("Array original:\n", arr)

mat = arr.reshape(3, 4)  # 3 filas, 4 columnas
print("Array con reshape (3x4):\n", mat)