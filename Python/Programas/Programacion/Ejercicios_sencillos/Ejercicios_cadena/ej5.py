# Ejercicio 5: mostrar las iniciales de un nombre y apellidos en mayúsculas

# Pedimos el nombre y los apellidos
nombre = input("Introduce tu nombre y apellidos: ")

# Cadena vacía donde iremos guardando las iniciales
iniciales = ""
# Separamos el nombre en palabras y recorremos cada una
for palabra in nombre.split():
    # Cogemos la primera letra de la palabra, la pasamos a mayúscula y la añadimos
    iniciales = iniciales + palabra[0].upper()

# Mostramos las iniciales
print("Iniciales:",iniciales)
