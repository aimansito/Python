# Ejercicio 1: calcular el factorial de un número

# Pedimos un número al usuario y lo convertimos a entero
numero = int(input("Introduce un número: "))
# Empezamos el factorial en 1 (elemento neutro de la multiplicación)
factorial = 1
# Recorremos todos los números desde 1 hasta el propio número (incluido)
for i in range(1, numero + 1):
    # Multiplicamos el acumulado por el número actual
    factorial = factorial * i
# Mostramos el resultado con el formato numero! = resultado
print(f"{numero}! = {factorial}")
