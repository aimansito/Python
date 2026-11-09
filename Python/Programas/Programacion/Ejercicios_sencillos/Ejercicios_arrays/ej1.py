# Ejercicio 1: vector de 10 enteros aleatorios con su cuadrado y su cubo

# Importamos random para generar números aleatorios
import random

# Creamos el vector (lista) vacío
vector_numeros = []
# Repetimos 10 veces para rellenar las 10 posiciones
for i in range(10):
    # Añadimos al final un número aleatorio entre 1 y 10
    vector_numeros.append(random.randint(1, 10))

# Recorremos cada elemento del vector
for numero in vector_numeros:
    # Mostramos el número, su cuadrado y su cubo
    print(f"Número: {numero}  Cuadrado: {numero ** 2}  Cubo: {numero ** 3}")
