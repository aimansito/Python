# Ejercicio 9: comprobar si una cadena contiene una subcadena

# Pedimos la cadena principal
cadena = input("Introduce una cadena: ")
# Pedimos la subcadena a buscar
subcadena = input("Introduce la subcadena a buscar: ")
# El operador "in" devuelve True si la subcadena está dentro de la cadena
if subcadena in cadena:
    # find() devuelve la posición donde empieza la subcadena
    posicion = cadena.find(subcadena)
    # Informamos de que sí la contiene y en qué posición
    print(f"La cadena contiene '{subcadena}' (empieza en la posición {posicion})")
# Si no la contiene
else:
    # Informamos de que no la contiene
    print(f"La cadena NO contiene '{subcadena}'")
