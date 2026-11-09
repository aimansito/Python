# Ejercicio 10: convertir entre segundos y horas/minutos/segundos con un menú


# Función que recibe horas, minutos y segundos y devuelve el total en segundos
def a_segundos(horas, minutos, segundos):
    # Cada hora son 3600 s y cada minuto 60 s
    return horas * 3600 + minutos * 60 + segundos


# Función que recibe segundos y devuelve horas, minutos y segundos
def a_horas(total_segundos):
    # División entera entre 3600 nos da las horas
    horas = total_segundos // 3600
    # Lo que sobra de las horas, dividido entre 60, son los minutos
    minutos = (total_segundos % 3600) // 60
    # Lo que sobra de los minutos son los segundos
    segundos = total_segundos % 60
    # Devolvemos los tres valores
    return horas, minutos, segundos


# Variable con la opción elegida
opcion = ""
# Repetimos hasta que se elija salir
while opcion != "3":
    # Mostramos el menú
    print("\n1. Convertir a segundos")
    # Segunda opción
    print("2. Convertir a horas, minutos y segundos")
    # Tercera opción
    print("3. Salir")
    # Pedimos la opción
    opcion = input("Elige una opción: ")
    # Opción 1
    if opcion == "1":
        # Pedimos las horas
        h = int(input("Horas: "))
        # Pedimos los minutos
        m = int(input("Minutos: "))
        # Pedimos los segundos
        s = int(input("Segundos: "))
        # Mostramos el resultado
        print(f"Son {a_segundos(h, m, s)} segundos")
    # Opción 2
    elif opcion == "2":
        # Pedimos los segundos totales
        total = int(input("Segundos: "))
        # Llamamos a la función y recogemos los tres valores
        h, m, s = a_horas(total)
        # Mostramos el resultado
        print(f"Son {h} horas, {m} minutos y {s} segundos")
    # Opción 3
    elif opcion == "3":
        # Nos despedimos
        print("¡Adiós!")
    # Opción no válida
    else:
        # Avisamos del error
        print("Opción no válida")
