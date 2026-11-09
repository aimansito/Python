# Ejercicio 4: contar números positivos, negativos y ceros

# Pedimos cuántos números se van a introducir
cantidad = int(input("¿Cuántos números vas a introducir? "))
# Contador de números mayores que 0
positivos = 0
# Contador de números menores que 0
negativos = 0
# Contador de números iguales a 0
ceros = 0
# Repetimos tantas veces como números haya que pedir
for i in range(cantidad):
    # Pedimos un número
    numero = float(input(f"Número {i + 1}: "))
    # Si es mayor que cero
    if numero > 0:
        # Sumamos uno a los positivos
        positivos = positivos + 1
    # Si es menor que cero
    elif numero < 0:
        # Sumamos uno a los negativos
        negativos = negativos + 1
    # Si no es ni mayor ni menor, es cero
    else:
        # Sumamos uno a los ceros
        ceros = ceros + 1

# Mostramos cuántos son mayores que 0
print("Mayores que 0:", positivos)
# Mostramos cuántos son menores que 0
print("Menores que 0:", negativos)
# Mostramos cuántos son iguales a 0
print("Iguales a 0:", ceros)
