# Ejercicio 4: contar números positivos, negativos y ceros

cantidad = int(input("¿Cuántos números vas a introducir? "))
positivos = 0
negativos = 0
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

print("Mayores que 0:", positivos)
print("Menores que 0:", negativos)
print("Iguales a 0:", ceros)
