# Ejercicio 8: factorial con una función recursiva


# Función recursiva: se llama a sí misma con un número más pequeño
def factorial(n):
    # Caso base: el factorial de 0 y de 1 es 1 (aquí se para la recursión)
    if n <= 1:
        # Devolvemos 1
        return 1
    # Caso recursivo: n! = n * (n-1)!
    return n * factorial(n - 1)


# Pedimos un número entero
numero = int(input("Introduce un número entero: "))
# El factorial no existe para números negativos
if numero < 0:
    # Avisamos del error
    print("No existe el factorial de un número negativo")
# Si el número es válido
else:
    # Llamamos a la función y mostramos el resultado
    print(f"{numero}! = {factorial(numero)}")
