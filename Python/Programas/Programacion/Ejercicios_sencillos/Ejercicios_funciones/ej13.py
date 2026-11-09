# Ejercicio 13: operaciones con fracciones (numerador/denominador)


# Devuelve el máximo común divisor de a y b (método de Euclides)
def calcular_mcd(a, b):
    # Trabajamos con valores positivos
    a, b = abs(a), abs(b)
    # Mientras b no sea 0
    while b != 0:
        # a pasa a ser b y b pasa a ser el resto de a entre b
        a, b = b, a % b
    # Cuando b es 0, a es el MCD
    return a


# Simplifica la fracción dividiendo entre el MCD
def simplificar_fraccion(num, den):
    # Calculamos el MCD de numerador y denominador
    divisor = calcular_mcd(num, den)
    # Si el MCD es 0 (numerador y denominador 0) no simplificamos
    if divisor == 0:
        # Devolvemos la fracción tal cual
        return num, den
    # Dividimos ambos por el MCD
    num, den = num // divisor, den // divisor
    # Si el denominador es negativo, pasamos el signo al numerador
    if den < 0:
        # Cambiamos el signo de los dos
        num, den = -num, -den
    # Devolvemos la fracción simplificada
    return num, den


# Lee una fracción por teclado y la devuelve simplificada
def leer_fraccion():
    # Pedimos el numerador
    num = int(input("  Numerador: "))
    # Pedimos el denominador
    den = int(input("  Denominador: "))
    # El denominador no puede ser 0
    while den == 0:
        # Lo volvemos a pedir
        den = int(input("  El denominador no puede ser 0. Denominador: "))
    # Devolvemos la fracción simplificada
    return simplificar_fraccion(num, den)


# Escribe la fracción en pantalla (si el denominador es 1, solo el numerador)
def escribir_fraccion(num, den):
    # Si el denominador es 1
    if den == 1:
        # Devolvemos solo el numerador como texto
        return str(num)
    # Si no, devolvemos "num/den"
    return f"{num}/{den}"


# Suma: n1*d2 + d1*n2 / d1*d2
def sumar_fracciones(n1, d1, n2, d2):
    # Calculamos y simplificamos
    return simplificar_fraccion(n1 * d2 + d1 * n2, d1 * d2)


# Resta: n1*d2 - d1*n2 / d1*d2
def restar_fracciones(n1, d1, n2, d2):
    # Calculamos y simplificamos
    return simplificar_fraccion(n1 * d2 - d1 * n2, d1 * d2)


# Multiplicación: n1*n2 / d1*d2
def multiplicar_fracciones(n1, d1, n2, d2):
    # Calculamos y simplificamos
    return simplificar_fraccion(n1 * n2, d1 * d2)


# División: n1*d2 / d1*n2
def dividir_fracciones(n1, d1, n2, d2):
    # Calculamos y simplificamos
    return simplificar_fraccion(n1 * d2, d1 * n2)


# Opción elegida en el menú
opcion = ""
# Repetimos hasta elegir Salir
while opcion != "5":
    # Mostramos el menú
    print("\n1. Sumar dos fracciones")
    # Opción 2
    print("2. Restar dos fracciones")
    # Opción 3
    print("3. Multiplicar dos fracciones")
    # Opción 4
    print("4. Dividir dos fracciones")
    # Opción 5
    print("5. Salir")
    # Pedimos la opción
    opcion = input("Elige una opción: ")

    # Si la opción es una de las operaciones
    if opcion in ("1", "2", "3", "4"):
        # Pedimos la primera fracción
        print("Primera fracción:")
        # La leemos
        n1, d1 = leer_fraccion()
        # Pedimos la segunda fracción
        print("Segunda fracción:")
        # La leemos
        n2, d2 = leer_fraccion()

        # Sumar
        if opcion == "1":
            # Calculamos la suma
            n, d = sumar_fracciones(n1, d1, n2, d2)
            # Guardamos el símbolo para mostrarlo
            simbolo = "+"
        # Restar
        elif opcion == "2":
            # Calculamos la resta
            n, d = restar_fracciones(n1, d1, n2, d2)
            # Guardamos el símbolo
            simbolo = "-"
        # Multiplicar
        elif opcion == "3":
            # Calculamos el producto
            n, d = multiplicar_fracciones(n1, d1, n2, d2)
            # Guardamos el símbolo
            simbolo = "*"
        # Dividir
        else:
            # No se puede dividir entre una fracción que vale 0
            if n2 == 0:
                # Avisamos y volvemos al menú
                print("No se puede dividir entre 0")
                # Saltamos al principio del bucle
                continue
            # Calculamos el cociente
            n, d = dividir_fracciones(n1, d1, n2, d2)
            # Guardamos el símbolo
            simbolo = ":"
        # Mostramos la operación y el resultado
        print(f"{escribir_fraccion(n1, d1)} {simbolo} {escribir_fraccion(n2, d2)}"
              f" = {escribir_fraccion(n, d)}")
    # Salir
    elif opcion == "5":
        # Nos despedimos
        print("¡Adiós!")
    # Opción no válida
    else:
        # Avisamos
        print("Opción no válida")
