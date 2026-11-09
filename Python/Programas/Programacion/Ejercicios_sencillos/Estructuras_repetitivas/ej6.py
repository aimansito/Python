# Ejercicio 6: mostrar los números pares entre dos números

# Pedimos el primer número
num1 = int(input("Introduce el primer número: "))
# Pedimos el segundo número
num2 = int(input("Introduce el segundo número: "))
# Si el primero es mayor que el segundo
if num1 > num2:
    # Los intercambiamos para recorrer siempre de menor a mayor
    num1, num2 = num2, num1
# Recorremos todos los números entre ambos (incluidos)
for i in range(num1, num2 + 1):
    # Si el resto de dividir entre 2 es 0, el número es par
    if i % 2 == 0:
        # Mostramos el número par
        print(i)
