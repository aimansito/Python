# Ejercicio 20: mostrar los N primeros números primos

# Pedimos cuántos primos queremos
n = int(input("¿Cuántos números primos quieres mostrar? "))
# Contador de primos encontrados
encontrados = 0
# Número que vamos a comprobar (el primer primo es el 2)
numero = 2
# Repetimos hasta encontrar N primos
while encontrados < n:
    # Suponemos que el número es primo
    es_primo = True
    # Empezamos a probar divisores desde el 2
    divisor = 2
    # Probamos hasta la raíz cuadrada del número
    while divisor * divisor <= numero and es_primo:
        # Si la división es exacta, no es primo
        if numero % divisor == 0:
            # Marcamos que no es primo
            es_primo = False
        # Pasamos al siguiente divisor
        divisor = divisor + 1
    # Si es primo
    if es_primo:
        # Lo mostramos
        print(numero)
        # Contamos un primo más
        encontrados = encontrados + 1
    # Pasamos al siguiente número
    numero = numero + 1
