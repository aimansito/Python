# Ejercicio 5: convertir de decimal a binario y de binario a decimal


# Recibe un entero y devuelve una cadena con su representación binaria
def convertir_a_binario(numero):
    # El 0 en binario es "0"
    if numero == 0:
        # Lo devolvemos directamente
        return "0"
    # Cadena donde iremos construyendo el binario
    binario = ""
    # Mientras queden cifras por sacar
    while numero > 0:
        # El resto de dividir entre 2 es la siguiente cifra (se pone delante)
        binario = str(numero % 2) + binario
        # Dividimos el número entre 2 (división entera)
        numero = numero // 2
    # Devolvemos la cadena binaria
    return binario


# Recibe una cadena binaria y devuelve el número en decimal
def convertir_a_decimal(binario):
    # Acumulador del resultado
    decimal = 0
    # Recorremos cada cifra de izquierda a derecha
    for cifra in binario:
        # Multiplicamos lo que llevamos por 2 y sumamos la cifra actual
        decimal = decimal * 2 + int(cifra)
    # Devolvemos el número decimal
    return decimal


# Opción del menú
opcion = ""
# Repetimos hasta que se elija salir
while opcion != "3":
    # Mostramos el menú
    print("\n1. Decimal a binario")
    # Opción 2
    print("2. Binario a decimal")
    # Opción 3
    print("3. Salir")
    # Pedimos la opción
    opcion = input("Elige una opción: ")
    # Decimal a binario
    if opcion == "1":
        # Pedimos el número decimal
        n = int(input("Número decimal (positivo): "))
        # Mostramos su binario
        print(f"{n} en binario es {convertir_a_binario(n)}")
    # Binario a decimal
    elif opcion == "2":
        # Pedimos el número binario
        b = input("Número binario: ")
        # Comprobamos que solo tenga ceros y unos y no esté vacío
        if b != "" and all(c in "01" for c in b):
            # Mostramos su valor decimal
            print(f"{b} en decimal es {convertir_a_decimal(b)}")
        # Si tiene otros caracteres
        else:
            # Avisamos del error
            print("Error: un número binario solo puede tener 0 y 1")
    # Salir
    elif opcion == "3":
        # Despedida
        print("¡Adiós!")
    # Opción no válida
    else:
        # Avisamos
        print("Opción no válida")
