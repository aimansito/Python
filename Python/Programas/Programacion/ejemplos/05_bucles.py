# Ejemplo 05: bucles while y for, range, break, continue y pass (tema1.pdf, apartado 5)

# ------------------------------------------------------------
# while: se repite MIENTRAS la condición sea True
# ------------------------------------------------------------

# Contador que empieza en 1
i = 1
# Mientras sea menor que 6
while i < 6:
    # Mostramos el valor
    print(i)
    # Lo incrementamos (si no, el bucle sería infinito)
    i += 1

# while con una variable de control (bandera), muy usado en juegos
partida_acabada = False
# Número de turno
turno = 1
# Repetimos mientras la partida no haya acabado
while not partida_acabada:
    # Mostramos el turno
    print("Turno", turno)
    # Al llegar al turno 3 acabamos
    if turno == 3:
        # Cambiamos la bandera y el bucle termina
        partida_acabada = True
    # Siguiente turno
    turno += 1

# ------------------------------------------------------------
# for: recorre los elementos de algo iterable (lista, cadena, range...)
# ------------------------------------------------------------

# Lista de palabras
palabras = ['gato', 'ventana', 'defenestrado']
# p toma cada palabra de la lista
for p in palabras:
    # Mostramos la palabra y su longitud
    print(p, len(p))

# Recorremos una cadena carácter a carácter
for letra in "Hola":
    # Mostramos cada letra
    print(letra)

# ------------------------------------------------------------
# range([inicio,] fin [, paso]): el fin NO se incluye
# ------------------------------------------------------------

# Imprime 0 1 2
for i in range(3):
    # Mostramos i
    print(i)
# Imprime del 5 al 9
for i in range(5, 10):
    # Mostramos i
    print(i)
# Imprime los impares del 1 al 9
for i in range(1, 10, 2):
    # Mostramos i
    print(i)
# Cuenta atrás de 3 a 1 (paso negativo)
for i in range(3, 0, -1):
    # Mostramos i
    print(i)

# ------------------------------------------------------------
# Bucles anidados: un bucle dentro de otro
# ------------------------------------------------------------

# Lista de listas
lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]
# Cada i es una sublista
for i in lista:
    # Cada j es un número de esa sublista
    for j in i:
        # Mostramos el número
        print(j)

# ------------------------------------------------------------
# break: sale del bucle  /  continue: salta a la siguiente vuelta
# ------------------------------------------------------------

# Buscamos el primer número divisible entre 7
for numero in range(20, 40):
    # Si es divisible
    if numero % 7 == 0:
        # Lo mostramos
        print("Primer múltiplo de 7:", numero)
        # Salimos del bucle
        break

# Mostramos solo los impares
for numero in range(1, 8):
    # Si es par, nos saltamos el resto de esta vuelta
    if numero % 2 == 0:
        # Pasamos al siguiente número
        continue
    # Solo llegan aquí los impares
    print("Impar:", numero)

# ------------------------------------------------------------
# else en un bucle: solo se ejecuta si el bucle NO acabó con break
# ------------------------------------------------------------

# Comprobamos si 13 es primo buscando divisores
numero = 13
# Probamos desde 2 hasta numero - 1
for divisor in range(2, numero):
    # Si divide exacto, no es primo
    if numero % divisor == 0:
        # Avisamos
        print(numero, "no es primo")
        # Salimos (y el else no se ejecuta)
        break
else:
    # No ha habido break: no tiene divisores
    print(numero, "es primo")

# ------------------------------------------------------------
# pass: bloque vacío (para rellenar más tarde sin que dé error)
# ------------------------------------------------------------

# Bucle que aún no hace nada
for i in range(3):
    # No hace nada
    pass
