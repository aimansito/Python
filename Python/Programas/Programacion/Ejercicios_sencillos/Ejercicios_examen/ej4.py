# Ejercicio 4: descomponer un número en sus factores primos

# Pedimos el número
numero = int(input("Introduce un número mayor que 1: "))
# Mientras no sea mayor que 1, lo volvemos a pedir
while numero < 2:
    # Pedimos de nuevo
    numero = int(input("Debe ser mayor que 1. Introduce otro: "))

# Guardamos el número original para mostrarlo al final
original = numero
# Lista donde guardamos los factores encontrados
factores = []
# Empezamos probando con el primer primo, el 2
divisor = 2
# Repetimos mientras quede algo por descomponer
while numero > 1:
    # Si el divisor divide exactamente al número
    if numero % divisor == 0:
        # Es un factor primo: lo guardamos
        factores.append(divisor)
        # Dividimos el número entre ese factor
        numero = numero // divisor
    # Si no lo divide
    else:
        # Probamos con el siguiente divisor
        divisor = divisor + 1

# Unimos los factores con " x " y mostramos el resultado
print(f"{original} = " + " x ".join(str(f) for f in factores))
