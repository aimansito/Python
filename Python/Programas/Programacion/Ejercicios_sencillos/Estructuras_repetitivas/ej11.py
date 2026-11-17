# Ejercicio 11: decir si un número es primo

numero = int(input("Introduce un número: "))
# Suponemos al principio que es primo
es_primo = True
# Los números menores que 2 no son primos
if numero < 2:
    es_primo = False
divisor = 2
# Basta con probar hasta la raíz cuadrada (divisor * divisor <= numero)
while divisor * divisor <= numero and es_primo:
    if numero % divisor == 0:
        es_primo = False
    divisor = divisor + 1
if es_primo:
    print(numero, "es primo")
else:
    print(numero, "no es primo")
