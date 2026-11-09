# Ejercicio 8: convertir mayúsculas en minúsculas y viceversa

# Pedimos la cadena
cadena = input("Introduce una cadena: ")
# Cadena vacía donde construimos el resultado
resultado = ""
# Recorremos cada carácter
for c in cadena:
    # Si el carácter está en mayúscula
    if c.isupper():
        # Lo añadimos en minúscula
        resultado = resultado + c.lower()
    # Si el carácter está en minúscula
    elif c.islower():
        # Lo añadimos en mayúscula
        resultado = resultado + c.upper()
    # Si no es una letra (números, espacios, signos...)
    else:
        # Lo añadimos sin cambios
        resultado = resultado + c
# Mostramos el resultado (también existe cadena.swapcase() que hace lo mismo)
print("Resultado:", resultado)
