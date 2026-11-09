# Ejercicio 9: MCD de dos números por el método de Euclides


# Función que calcula el MCD de a y b
def mcd(a, b):
    # Si a es menor que b, los intercambiamos para dividir el mayor entre el menor
    if a < b:
        # Intercambiamos los valores
        a, b = b, a
    # Calculamos el resto de dividir el mayor entre el menor
    resto = a % b
    # Mientras la división no sea exacta
    while resto != 0:
        # El divisor pasa a ser el dividendo
        a = b
        # El resto pasa a ser el divisor
        b = resto
        # Volvemos a calcular el resto
        resto = a % b
    # Cuando la división es exacta, el último divisor es el MCD
    return b


# Pedimos el primer número
num1 = int(input("Introduce el primer número: "))
# Pedimos el segundo número
num2 = int(input("Introduce el segundo número: "))
# Si alguno es 0 o negativo, el método no se aplica
if num1 <= 0 or num2 <= 0:
    # Avisamos del error
    print("Los números deben ser enteros positivos")
# Si son válidos
else:
    # Mostramos el MCD
    print(f"El MCD de {num1} y {num2} es {mcd(num1, num2)}")
