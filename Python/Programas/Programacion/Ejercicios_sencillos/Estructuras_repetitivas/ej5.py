# Ejercicio 5: decir si un carácter es VOCAL o NO VOCAL hasta introducir un espacio

# Cadena con todas las vocales (minúsculas, mayúsculas y con tilde)
vocales = "aeiouAEIOUáéíóúÁÉÍÓÚüÜ"
# Pedimos el primer carácter
caracter = input("Introduce un carácter (espacio para terminar): ")
# Repetimos mientras el carácter no sea un espacio
while caracter != " ":
    # Validamos que sea un solo carácter
    if len(caracter) != 1:
        # Si no lo es, mostramos un error
        print("Error: introduce un solo carácter")
    # Si el carácter está dentro de la cadena de vocales
    elif caracter in vocales:
        # Indicamos que es vocal
        print("VOCAL")
    # En cualquier otro caso
    else:
        # Indicamos que no es vocal
        print("NO VOCAL")
    # Pedimos el siguiente carácter
    caracter = input("Introduce un carácter (espacio para terminar): ")
