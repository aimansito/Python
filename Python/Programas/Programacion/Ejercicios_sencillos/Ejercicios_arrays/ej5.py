# Ejercicio 5: vector aleatorio ordenado de menor a mayor (método de la burbuja)

# Importamos random para generar números aleatorios
import random

# Creamos un vector con 10 números aleatorios entre 1 y 100
vector = [random.randint(1, 100) for i in range(10)]
# Mostramos el vector antes de ordenar
print("Vector original:", vector)

# Guardamos la longitud del vector
n = len(vector)
# Hacemos n-1 pasadas sobre el vector
for i in range(n - 1):
    # En cada pasada comparamos parejas de elementos contiguos
    for j in range(n - 1 - i):
        # Si el de la izquierda es mayor que el de la derecha
        if vector[j] > vector[j + 1]:
            # Los intercambiamos para que el mayor vaya hacia el final
            vector[j], vector[j + 1] = vector[j + 1], vector[j]

# Mostramos el vector ya ordenado (también se podría hacer con vector.sort())
print("Vector ordenado:", vector)
