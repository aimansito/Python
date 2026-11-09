# Ejercicio 2: vector de 5 cadenas copiado en otro vector en orden inverso

# Creamos el vector original vacío
vector = []
# Repetimos 5 veces para leer las 5 cadenas
for i in range(5):
    # Pedimos la cadena y la añadimos al vector
    vector.append(input(f"Introduce la cadena {i + 1}: "))

# Creamos el vector que tendrá los elementos al revés
inverso = []
# Recorremos los índices desde el último (4) hasta el primero (0)
for i in range(len(vector) - 1, -1, -1):
    # Copiamos el elemento de esa posición al nuevo vector
    inverso.append(vector[i])

# Mostramos el vector original
print("Vector original:", vector)
# Mostramos el vector invertido
print("Vector inverso: ", inverso)
