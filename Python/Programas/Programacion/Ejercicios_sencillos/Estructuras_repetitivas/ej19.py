# Ejercicio 19: ejemplo de menú que se repite hasta elegir Salir

# Variable donde guardamos la opción elegida
opcion = ""
# Repetimos mientras no se elija la opción 4 (Salir)
while opcion != "4":
    # Mostramos el título del menú
    print("\n--- MENÚ ---")
    # Opción 1
    print("1. Saludar")
    # Opción 2
    print("2. Sumar dos números")
    # Opción 3
    print("3. Mostrar el doble de un número")
    # Opción 4
    print("4. Salir")
    # Pedimos la opción
    opcion = input("Elige una opción: ")
    # Si eligió la opción 1
    if opcion == "1":
        # Saludamos
        print("¡Hola!")
    # Si eligió la opción 2
    elif opcion == "2":
        # Pedimos el primer número
        a = float(input("Primer número: "))
        # Pedimos el segundo número
        b = float(input("Segundo número: "))
        # Mostramos la suma
        print("La suma es:", a + b)
    # Si eligió la opción 3
    elif opcion == "3":
        # Pedimos un número
        n = float(input("Número: "))
        # Mostramos su doble
        print("El doble es:", n * 2)
    # Si eligió la opción 4
    elif opcion == "4":
        # Nos despedimos
        print("¡Adiós!")
    # Cualquier otra cosa es una opción no válida
    else:
        # Avisamos del error
        print("Opción no válida")
