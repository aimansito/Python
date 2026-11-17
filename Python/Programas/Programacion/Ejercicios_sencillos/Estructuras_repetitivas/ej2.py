# Ejercicio 2: adivinar un número aleatorio del 1 al 100 en 10 intentos

import random

# Generamos el número secreto entre 1 y 100 (ambos incluidos)
secreto = random.randint(1, 100)
max_intentos = 10
intentos = 0
acertado = False

# Repetimos mientras queden intentos y no se haya acertado
while intentos < max_intentos and not acertado:
    numero = int(input("Introduce un número del 1 al 100: "))
    intentos = intentos + 1
    if numero == secreto:
        # Marcamos que se ha acertado para salir del bucle
        acertado = True
        print(f"¡Has acertado! Lo has conseguido en {intentos} intentos")
    # Si el número secreto es mayor que el introducido
    elif secreto > numero:
        # Avisamos de que el número a adivinar es mayor
        print("El número a adivinar es MAYOR")
        print(f"Te quedan {max_intentos - intentos} intentos")
    # Si no, el número secreto es menor
    else:
        # Avisamos de que el número a adivinar es menor
        print("El número a adivinar es MENOR")
        # Mostramos los intentos que quedan
        print(f"Te quedan {max_intentos - intentos} intentos")

# Si al terminar el bucle no se ha acertado, se han agotado los intentos
if not acertado:
    # Mostramos cuál era el número generado
    print(f"Has agotado los intentos. El número era {secreto}")
