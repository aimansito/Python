# Ejercicio 7: el ordenador adivina un número que piensa el usuario

# Pedimos el límite inferior del rango
inferior = int(input("Límite inferior: "))
# Pedimos el límite superior del rango
superior = int(input("Límite superior: "))
# Si están al revés, los intercambiamos
if inferior > superior:
    # Intercambio
    inferior, superior = superior, inferior

# Pedimos al usuario que piense un número
print(f"Piensa un número entre {inferior} y {superior}")
# Contador de intentos del ordenador
intentos = 0
# Respuesta del usuario
respuesta = ""
# Repetimos hasta que el usuario diga "S" (correcto)
while respuesta != "S":
    # Si los límites se han cruzado, el usuario ha hecho trampa o se ha equivocado
    if inferior > superior:
        # Lo indicamos y terminamos
        print("Las respuestas no son coherentes, no hay ningún número posible")
        # Salimos del bucle
        break
    # El ordenador propone el número del medio (búsqueda binaria)
    propuesta = (inferior + superior) // 2
    # Sumamos un intento
    intentos = intentos + 1
    # Mostramos la propuesta y pedimos la respuesta en mayúsculas
    respuesta = input(f"¿Es el {propuesta}? (S=sí, A=es más alto que tu número, "
                      f"B=es más bajo): ").upper()
    # Si la propuesta es más alta que el número, el número está por debajo
    if respuesta == "A":
        # Bajamos el límite superior
        superior = propuesta - 1
    # Si la propuesta es más baja que el número, el número está por encima
    elif respuesta == "B":
        # Subimos el límite inferior
        inferior = propuesta + 1
    # Si la respuesta no es S, A ni B
    elif respuesta != "S":
        # Avisamos y no contamos ese intento
        print("Respuesta no válida, usa S, A o B")
        # Descontamos el intento
        intentos = intentos - 1

# Si se ha acertado
if respuesta == "S":
    # Mostramos el número de intentos
    print(f"¡He acertado en {intentos} intentos!")
