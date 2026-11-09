# Ejercicio 10: comprobar si una cadena es un palíndromo

# Pedimos la cadena
cadena = input("Introduce una palabra o frase: ")
# La pasamos a minúsculas para que "Ana" y "ana" se consideren iguales
limpia = cadena.lower()
# Quitamos los espacios para que funcione también con frases
limpia = limpia.replace(" ", "")
# Construimos la cadena al revés con slicing ([::-1] recorre de atrás hacia delante)
invertida = limpia[::-1]
# Si la cadena es igual a su versión invertida, es palíndromo
if limpia == invertida:
    # Informamos de que es palíndromo
    print(f"'{cadena}' ES un palíndromo")
# Si no son iguales
else:
    # Informamos de que no lo es
    print(f"'{cadena}' NO es un palíndromo")
