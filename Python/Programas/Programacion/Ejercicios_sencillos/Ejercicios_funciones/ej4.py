# Ejercicio 4: función ConvertirEspaciado (un espacio tras cada letra)


# Función que recibe un texto y devuelve otro con un espacio tras cada carácter
def convertir_espaciado(texto):
    # Cadena vacía donde construimos el resultado
    resultado = ""
    # Recorremos cada carácter del texto
    for caracter in texto:
        # Si el carácter es un espacio, lo saltamos para no duplicar espacios
        if caracter == " ":
            # Pasamos al siguiente carácter
            continue
        # Añadimos el carácter seguido de un espacio
        resultado = resultado + caracter + " "
    # Devolvemos la cadena espaciada
    return resultado


# Pedimos un texto al usuario
texto = input("Introduce un texto: ")
# Mostramos el resultado entre comillas para que se vea el espacio final
print(f'"{convertir_espaciado(texto)}"')
