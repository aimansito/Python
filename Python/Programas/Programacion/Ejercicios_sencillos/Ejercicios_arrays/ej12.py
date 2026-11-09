# Ejercicio 12: matriz 5x15 con un marco de 1 y el interior a 0

# Número de filas
FILAS = 5
# Número de columnas
COLUMNAS = 15
# Creamos la matriz vacía
marco = []
# Recorremos las filas
for i in range(FILAS):
    # Creamos una fila vacía
    fila = []
    # Recorremos las columnas
    for j in range(COLUMNAS):
        # Si es la primera o última fila, o la primera o última columna, es borde
        if i == 0 or i == FILAS - 1 or j == 0 or j == COLUMNAS - 1:
            # El borde vale 1
            fila.append(1)
        # Si no es borde, es interior
        else:
            # El interior vale 0
            fila.append(0)
    # Añadimos la fila a la matriz
    marco.append(fila)

# Recorremos cada fila para mostrarla
for fila in marco:
    # Unimos los números sin separación para que se vea como en el enunciado
    print("".join(str(x) for x in fila))
