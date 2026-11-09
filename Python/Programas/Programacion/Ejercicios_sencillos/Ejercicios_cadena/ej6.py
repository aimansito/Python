# Ejercicio 6: invertir una cadena carácter a carácter

# Pedimos la cadena original
cadena = input("Introduce una cadena: ")
# Cadena vacía donde construiremos la invertida
invertida = ""
# Recorremos cada carácter de la cadena original
for caracter in cadena:
    # Ponemos el carácter DELANTE de lo que ya teníamos, así queda al revés
    invertida = caracter + invertida
# Mostramos la cadena invertida
print("Cadena invertida:", invertida)
