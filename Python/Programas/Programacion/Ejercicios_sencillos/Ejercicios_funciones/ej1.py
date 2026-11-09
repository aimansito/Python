# Ejercicio 1: procedimiento EscribirCentrado (texto centrado y subrayado con =)


# Definimos el procedimiento que recibe el texto a escribir
def escribir_centrado(texto):
    # Calculamos los espacios: 40 menos la mitad de la longitud del texto
    espacios = 40 - len(texto) // 2
    # Escribimos los espacios seguidos del texto
    print(" " * espacios + texto)
    # Debajo escribimos tantos "=" como letras tiene el texto, con los mismos espacios
    print(" " * espacios + "=" * len(texto))


# Pedimos el texto al usuario
mensaje = input("Introduce un texto: ")
# Llamamos al procedimiento para escribirlo centrado
escribir_centrado(mensaje)
