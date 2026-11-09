# Ejercicio 2: comprobar si una cadena comienza por una subcadena

# Pedimos la cadena principal
cadena = input("Introduce una cadena: ")
# Pedimos la subcadena que queremos buscar al principio
subcadena = input("Introduce la subcadena: ")

# startswith() devuelve True si la cadena empieza por la subcadena
if cadena.startswith(subcadena):
    # Informamos de que sí comienza por ella
    print ("La cadena comienza por ", subcadena)
# Si no empieza por la subcadena
else:
    # Informamos de que no comienza por ella
    print("La cadena NO comienza por ",subcadena)
