# Ejemplo 09: matrices = listas de listas (lista2.pdf)
# Es la base del tablero del 3 en raya.

# ------------------------------------------------------------
# Crear una matriz a partir de sus filas
# ------------------------------------------------------------

# Primera fila
fila1 = [1, 3, 5]
# Segunda fila
fila2 = [9, 3, 5]
# Tercera fila
fila3 = [7, 3, 8]
# La matriz es una lista que contiene las filas
matriz = [fila1, fila2, fila3]
# Imprime la matriz completa
print(matriz)
# Un solo elemento: matriz[fila][columna] -> 3.º de la 2.ª fila
print(matriz[1][2])

# ------------------------------------------------------------
# Crear una matriz 3x3 llena de ceros con bucles
# ------------------------------------------------------------

# Constante con el valor de casilla vacía
VACIO = 0
# Constante con el tamaño
TAMANIO = 3
# Empezamos con una lista vacía
tablero = []
# Una vuelta por cada fila
for i in range(TAMANIO):
    # Fila nueva vacía
    fila = []
    # Una vuelta por cada columna
    for j in range(TAMANIO):
        # Añadimos una casilla vacía
        fila.append(VACIO)
    # Añadimos la fila al tablero
    tablero.append(fila)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(tablero)

# Lo mismo con comprensión de listas
tablero = [[VACIO for j in range(TAMANIO)] for i in range(TAMANIO)]
# Mostramos
print(tablero)

# ¡CUIDADO! [[0] * 3] * 3 repite LA MISMA fila 3 veces:
mal = [[0] * 3] * 3
# Cambiamos una casilla de la fila 0...
mal[0][0] = 9
# ...y cambia en las tres filas, porque son la misma lista
print("Matriz mal creada:", mal)

# ------------------------------------------------------------
# Modificar y recorrer una matriz
# ------------------------------------------------------------

# Colocamos un 1 en el centro
tablero[1][1] = 1
# Y un 2 en la esquina de abajo a la derecha
tablero[2][2] = 2

# Recorrido por índices: fila y columna
for fila in range(len(tablero)):
    # Columna de esa fila
    for columna in range(len(tablero[fila])):
        # Mostramos posición y valor
        print(f"({fila},{columna}) = {tablero[fila][columna]}")

# Recorrido directo por elementos
for fila in tablero:
    # Texto de la fila
    linea = ""
    # Cada valor de la fila
    for valor in fila:
        # Lo añadimos al texto con un espacio
        linea += str(valor) + " "
    # Mostramos la fila como una línea
    print(linea)

# ------------------------------------------------------------
# Algoritmia típica con matrices
# ------------------------------------------------------------

# Contar cuántas casillas valen VACIO
vacias = 0
# Recorremos filas
for fila in tablero:
    # Recorremos valores
    for valor in fila:
        # Si está vacía, contamos
        if valor == VACIO:
            # Una más
            vacias += 1
# Mostramos el total
print("Casillas vacías:", vacias)

# Sumar cada fila de la matriz de números
for fila in matriz:
    # Acumulador
    suma_fila = 0
    # Recorremos los números de la fila
    for numero in fila:
        # Sumamos
        suma_fila += numero
    # Mostramos la suma
    print("Suma de", fila, "=", suma_fila)

# Sumar una columna: fijamos la columna y movemos la fila
columna = 1
# Acumulador
suma_columna = 0
# Recorremos las filas
for fila in range(len(matriz)):
    # Sumamos el elemento de esa columna
    suma_columna += matriz[fila][columna]
# Mostramos el resultado
print("Suma de la columna", columna, "=", suma_columna)

# Diagonal principal: fila y columna iguales -> (0,0) (1,1) (2,2)
for i in range(len(matriz)):
    # Elemento de la diagonal
    print("Diagonal principal:", matriz[i][i])

# Diagonal secundaria: (0,2) (1,1) (2,0) -> columna = tamaño - 1 - fila
for i in range(len(matriz)):
    # Elemento de la diagonal secundaria
    print("Diagonal secundaria:", matriz[i][len(matriz) - 1 - i])
