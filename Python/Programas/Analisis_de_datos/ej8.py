import numpy as np

arr3d = np.array([[[1, 2], [3, 4]],
                  [[5, 6], [7, 8]]])

# Acceso a un elemento
print(arr3d[0, 0, 0])  # 1
print(arr3d[1, 1, 1])  # 8
print(arr3d[0, 1, 0])  # 3

# Fila completa
print(arr3d[0, 0, :])  # [1 2]
print(arr3d[1, 1, :])  # [7 8]

# Columna
print(arr3d[0, :, 1])  # [2 4]

# Bloque completo
print(arr3d[0, :, :])  # [[1 2]
                       #  [3 4]]
print(arr3d[1, :, :])  # [[5 6]
                       #  [7 8]]

# Slicing
print(arr3d[0:2, 0, :])  # [[1 2]
                         #  [5 6]]   