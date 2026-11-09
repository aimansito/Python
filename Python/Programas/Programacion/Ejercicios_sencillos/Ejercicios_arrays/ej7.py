# Ejercicio 7: vector3 = vector1 + vector2 (suma elemento a elemento)

# Creamos vector1 vacío
vector1 = []
# Creamos vector2 vacío
vector2 = []
# Creamos vector3 vacío (será el resultado)
vector3 = []

# Pedimos los 5 valores de vector1
for i in range(5):
    # Leemos el número y lo añadimos a vector1
    vector1.append(int(input(f"vector1[{i}]: ")))
# Pedimos los 5 valores de vector2
for i in range(5):
    # Leemos el número y lo añadimos a vector2
    vector2.append(int(input(f"vector2[{i}]: ")))

# Recorremos las 5 posiciones
for i in range(5):
    # Sumamos los elementos de la misma posición y lo guardamos en vector3
    vector3.append(vector1[i] + vector2[i])

# Mostramos vector1
print("vector1:", vector1)
# Mostramos vector2
print("vector2:", vector2)
# Mostramos el resultado
print("vector3:", vector3)
