# Ejercicio 11: matriz 5x5 con 1 en la diagonal y 0 en el resto

# Tamaño de la matriz
N = 5
# Creamos la matriz vacía
diagonal = []
# Recorremos las filas
for i in range(N):
    # Creamos una fila vacía
    fila = []
    # Recorremos las columnas
    for j in range(N):
        # Si la fila y la columna coinciden, estamos en la diagonal
        if i == j:
            # Ponemos un 1
            fila.append(1)
        # Si no estamos en la diagonal
        else:
            # Ponemos un 0
            fila.append(0)
    # Añadimos la fila a la matriz
    diagonal.append(fila)

# Recorremos cada fila para mostrarla
for fila in diagonal:
    # Unimos los números de la fila separados por un espacio
    print(" ".join(str(x) for x in fila))
