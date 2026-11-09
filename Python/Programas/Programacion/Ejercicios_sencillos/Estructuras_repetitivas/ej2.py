# Ejercicio 2: adivinar un número aleatorio del 1 al 100 en 10 intentos

# Importamos el módulo random para generar números aleatorios
import random

# Generamos el número secreto entre 1 y 100 (ambos incluidos)
secreto = random.randint(1, 100)
# Número máximo de intentos que tiene el jugador
max_intentos = 10
# Contador de intentos que lleva el jugador
intentos = 0
# Variable que indica si ya se ha acertado el número
acertado = False

# Repetimos mientras queden intentos y no se haya acertado
while intentos < max_intentos and not acertado:
    # Pedimos un número al jugador
    numero = int(input("Introduce un número del 1 al 100: "))
    # Sumamos un intento
    intentos = intentos + 1
    # Comprobamos si ha acertado
    if numero == secreto:
        # Marcamos que se ha acertado para salir del bucle
        acertado = True
        # Felicitamos e indicamos en cuántos intentos lo ha conseguido
        print(f"¡Has acertado! Lo has conseguido en {intentos} intentos")
    # Si el número secreto es mayor que el introducido
    elif secreto > numero:
        # Avisamos de que el número a adivinar es mayor
        print("El número a adivinar es MAYOR")
        # Mostramos los intentos que quedan
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
