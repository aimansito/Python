# Ejercicio 3: pedir números hasta un cero y mostrar la suma y la media

# Acumulador para la suma de los números
suma = 0
# Contador de cuántos números se han introducido
contador = 0
# Pedimos el primer número
numero = float(input("Introduce un número (0 para terminar): "))
# Repetimos mientras el número no sea cero
while numero != 0:
    # Sumamos el número al acumulado
    suma = suma + numero
    # Contamos un número más
    contador = contador + 1
    # Pedimos el siguiente número
    numero = float(input("Introduce un número (0 para terminar): "))

# Mostramos la suma total
print("La suma es:", suma)
# Comprobamos que se haya introducido al menos un número para no dividir entre 0
if contador > 0:
    # Calculamos y mostramos la media
    print("La media es:", suma / contador)
# Si no se introdujo ningún número
else:
    # Avisamos de que no se puede calcular la media
    print("No se ha introducido ningún número, no hay media")
