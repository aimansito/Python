# Ejercicio 1: escribir por pantalla cada carácter de una cadena

# Pedimos una cadena por teclado
cadena = input("Introduce una cadena: ")

# Recorremos la cadena carácter a carácter
for caracter in cadena:
    # Mostramos cada carácter en una línea distinta (en vertical)
    print(caracter)
# Volvemos a recorrer la cadena para mostrarla en horizontal
for caracter in cadena:
    # end=" " hace que no salte de línea y deje un espacio entre caracteres
    print(caracter, end=" ")
