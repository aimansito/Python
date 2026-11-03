import random
numero_secreto = random.randint(0,100)
intentos = 10
while intentos > 0:
    num = int(input("Introduce un número del 0 al 100: "))
    if num == numero_secreto:
        print("Enhorabuena has acertado")
        print(f"Lo has conseguido en {11 - intentos} intentos")
        intentos = 0
    else: 
        intentos -= 1
        if intentos > 0:
            if num < numero_secreto:
                print("El número a adivinar es mayor")
            else:
                print("El número a adivinar es menor")
                print(f"Te quedan {intentos} intentos")
        else:
            print("Has agotado todo los intentos")
            print(f"El número era {numero_secreto}")