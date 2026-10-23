import numpy as np

mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(mat[0, 0])   # Esquina superior izquierda -> 1
print(mat[1, 2])   # Fila 1, columna 2 -> 6
print(mat[-1, -1])  # Último elemento -> 9
print(mat[-2, -2])  # -> 5   