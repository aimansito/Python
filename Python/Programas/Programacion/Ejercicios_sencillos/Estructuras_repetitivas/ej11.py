# Ejercicio 11: decir si un número es primo

# Pedimos el número
numero = int(input("Introduce un número: "))
# Suponemos al principio que es primo
es_primo = True
# Los números menores que 2 no son primos
if numero < 2:
    # Marcamos que no es primo
    es_primo = False
# Empezamos a probar divisores desde el 2
divisor = 2
# Basta con probar hasta la raíz cuadrada (divisor * divisor <= numero)
while divisor * divisor <= numero and es_primo:
    # Si la división es exacta, tiene un divisor y no es primo
    if numero % divisor == 0:
        # Marcamos que no es primo
        es_primo = False
    # Pasamos al siguiente divisor
    divisor = divisor + 1
# Si es primo
if es_primo:
    # Lo indicamos
    print(numero, "es primo")
# Si no
else:
    # Indicamos que no lo es
    print(numero, "no es primo")
