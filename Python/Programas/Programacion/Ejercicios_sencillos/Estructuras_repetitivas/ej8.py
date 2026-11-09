# Ejercicio 8: trabajar con un intervalo y números hasta introducir 0

# Pedimos el límite inferior
inferior = int(input("Límite inferior: "))
# Pedimos el límite superior
superior = int(input("Límite superior: "))
# Mientras el inferior sea mayor que el superior, los volvemos a pedir
while inferior > superior:
    # Avisamos del error
    print("Error: el límite inferior debe ser menor o igual que el superior")
    # Volvemos a pedir el límite inferior
    inferior = int(input("Límite inferior: "))
    # Volvemos a pedir el límite superior
    superior = int(input("Límite superior: "))

# Suma de los números que están dentro del intervalo abierto
suma_dentro = 0
# Contador de números fuera del intervalo
fuera = 0
# Indica si se ha introducido algún número igual a uno de los límites
igual_limite = False

# Pedimos el primer número
numero = int(input("Introduce un número (0 para terminar): "))
# Repetimos hasta que se introduzca un 0
while numero != 0:
    # Si está estrictamente dentro (intervalo abierto, sin incluir los límites)
    if inferior < numero < superior:
        # Lo sumamos
        suma_dentro = suma_dentro + numero
    # Si es igual a uno de los límites
    elif numero == inferior or numero == superior:
        # Lo apuntamos
        igual_limite = True
    # Si no, está fuera del intervalo
    else:
        # Contamos uno más fuera
        fuera = fuera + 1
    # Pedimos el siguiente número
    numero = int(input("Introduce un número (0 para terminar): "))

# Mostramos la suma de los números de dentro
print("Suma de los números dentro del intervalo:", suma_dentro)
# Mostramos cuántos números estaban fuera
print("Números fuera del intervalo:", fuera)
# Si se introdujo algún número igual a los límites
if igual_limite:
    # Lo informamos
    print("Se ha introducido algún número igual a los límites")
# Si no
else:
    # Informamos de que no
    print("No se ha introducido ningún número igual a los límites")
