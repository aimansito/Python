# Ejercicio 10: matriz 5x5, suma de cada fila y de cada columna

# Importamos random para cargar la matriz sin tener que teclear 25 números
import random

# Tamaño de la matriz
N = 5
# Creamos la matriz vacía
matriz = []
# Recorremos las filas
for i in range(N):
    # Creamos una fila vacía
    fila = []
    # Recorremos las columnas
    for j in range(N):
        # Añadimos un entero aleatorio (se podría usar int(input(...)) para teclearlo)
        fila.append(random.randint(1, 9))
    # Añadimos la fila a la matriz
    matriz.append(fila)

# Título
print("Matriz:")
# Recorremos cada fila
for fila in matriz:
    # Mostramos la fila con cada número ocupando 3 espacios
    print("".join(f"{x:3}" for x in fila))

# Título de la suma de filas
print("\nSuma de cada fila:")
# Recorremos las filas
for i in range(N):
    # sum() suma todos los elementos de la fila i
    print(f"  Fila {i + 1}: {sum(matriz[i])}")

# Título de la suma de columnas
print("\nSuma de cada columna:")
# Recorremos las columnas
for j in range(N):
    # Acumulador de la columna
    suma_columna = 0
    # Recorremos las filas de esa columna
    for i in range(N):
        # Sumamos el elemento [i][j]
        suma_columna = suma_columna + matriz[i][j]
    # Mostramos la suma de la columna
    print(f"  Columna {j + 1}: {suma_columna}")
