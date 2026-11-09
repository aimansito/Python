# Ejercicio 7: sustituir un carácter por otro dentro de una cadena

# Pedimos la cadena
cadena = input("Introduce una cadena: ")

# Pedimos el carácter que queremos sustituir
caracter1 = input("Carácter a sustituir: ")
# Validamos que sea un solo carácter
while len(caracter1) != 1:
    # Si no lo es, lo volvemos a pedir
    caracter1 = input("Error. Introduce UN solo carácter a sustituir: ")

# Pedimos el carácter nuevo
caracter2 = input("Carácter nuevo: ")
# Validamos que sea un solo carácter
while len(caracter2) != 1:
    # Si no lo es, lo volvemos a pedir
    caracter2 = input("Error. Introduce UN solo carácter nuevo: ")

# Cadena vacía donde construimos el resultado
resultado = ""
# Recorremos cada carácter de la cadena
for c in cadena:
    # Si es el carácter que hay que sustituir
    if c == caracter1:
        # Añadimos el carácter nuevo en su lugar
        resultado = resultado + caracter2
    # Si es cualquier otro carácter
    else:
        # Lo añadimos tal cual
        resultado = resultado + c
# Mostramos la cadena resultante
print("Resultado:", resultado)
