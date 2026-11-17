# Ejercicio 5: decir si un carácter es VOCAL o NO VOCAL hasta introducir un espacio

# Cadena con todas las vocales (minúsculas, mayúsculas y con tilde)
vocales = "aeiouAEIOUáéíóúÁÉÍÓÚüÜ"
caracter = input("Introduce un carácter (espacio para terminar): ")
# Repetimos mientras el carácter no sea un espacio
while caracter != " ":
    # Validamos que sea un solo carácter
    if len(caracter) != 1:
        print("Error: introduce un solo carácter")
    # Si el carácter está dentro de la cadena de vocales
    elif caracter in vocales:
        print("VOCAL")
    else:
        print("NO VOCAL")
    caracter = input("Introduce un carácter (espacio para terminar): ")
