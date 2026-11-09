# Ejercicio 9: juego Mastermind con MUERTOS y HERIDOS

# Importamos random para elegir el código secreto
import random

# Elegimos 4 cifras distintas entre 0 y 9 (sample no repite elementos)
cifras = random.sample("0123456789", 4)
# Unimos las cifras en una cadena, por ejemplo "2607"
secreto = "".join(cifras)

# Explicamos el juego
print("He elegido un número de 4 cifras sin cifras repetidas. ¡Adivínalo!")
# Contador de intentos
intentos = 0
# Número de muertos de la última jugada
muertos = 0
# Repetimos hasta que haya 4 muertos (todas las cifras en su sitio)
while muertos < 4:
    # Pedimos un intento
    propuesta = input("Tu propuesta: ")
    # Comprobamos: 4 caracteres, todos dígitos y sin cifras repetidas
    if len(propuesta) != 4 or not propuesta.isdigit() or len(set(propuesta)) != 4:
        # Si no es válida, avisamos
        print("Debes escribir 4 cifras distintas")
        # Volvemos a pedir sin contar el intento
        continue
    # Contamos el intento
    intentos = intentos + 1
    # Reiniciamos los muertos
    muertos = 0
    # Reiniciamos los heridos
    heridos = 0
    # Recorremos las 4 posiciones
    for i in range(4):
        # Si la cifra coincide en la misma posición
        if propuesta[i] == secreto[i]:
            # Es un MUERTO
            muertos = muertos + 1
        # Si la cifra está en el secreto pero en otra posición
        elif propuesta[i] in secreto:
            # Es un HERIDO
            heridos = heridos + 1
    # Mostramos la respuesta
    print(f"  {muertos} MUERTOS y {heridos} HERIDOS")

# Al salir del bucle se ha acertado
print(f"¡Enhorabuena! El número era {secreto} y lo has adivinado en {intentos} intentos")
