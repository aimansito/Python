# Ejercicio 9: calcular una potencia sin usar el operador **

# Pedimos la base (número real)
base = float(input("Introduce la base: "))
# Pedimos el exponente (entero positivo)
exponente = int(input("Introduce el exponente (entero positivo): "))
# Mientras el exponente sea negativo, lo volvemos a pedir
while exponente < 0:
    # Volvemos a pedir el exponente
    exponente = int(input("El exponente debe ser positivo. Introdúcelo de nuevo: "))
# Empezamos el resultado en 1 (cualquier número elevado a 0 es 1)
resultado = 1
# Multiplicamos la base tantas veces como indique el exponente
for i in range(exponente):
    # Multiplicamos el resultado por la base
    resultado = resultado * base
# Mostramos el resultado
print(f"{base} elevado a {exponente} = {resultado}")
