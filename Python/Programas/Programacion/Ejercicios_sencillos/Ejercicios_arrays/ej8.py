# Ejercicio 8: nombres y edades de alumnos hasta introducir "*"

# Vector con los nombres de los alumnos
nombres = []
# Vector con las edades (misma posición que su nombre)
edades = []

# Pedimos el primer nombre
nombre = input("Nombre del alumno (* para terminar): ")
# Repetimos mientras el nombre no sea un asterisco
while nombre != "*":
    # Pedimos la edad de ese alumno
    edad = int(input(f"Edad de {nombre}: "))
    # Guardamos el nombre
    nombres.append(nombre)
    # Guardamos la edad
    edades.append(edad)
    # Pedimos el siguiente nombre
    nombre = input("Nombre del alumno (* para terminar): ")

# Si no se introdujo ningún alumno
if len(nombres) == 0:
    # Lo indicamos
    print("No se ha introducido ningún alumno")
# Si hay alumnos
else:
    # Título del primer listado
    print("\nAlumnos mayores de edad:")
    # Recorremos todas las posiciones
    for i in range(len(nombres)):
        # Si la edad es 18 o más
        if edades[i] >= 18:
            # Mostramos el alumno
            print(f"  {nombres[i]} ({edades[i]} años)")

    # Calculamos la edad máxima
    edad_maxima = max(edades)
    # Título del segundo listado
    print(f"\nAlumnos mayores (con {edad_maxima} años):")
    # Recorremos todas las posiciones
    for i in range(len(nombres)):
        # Si su edad es la máxima (puede haber varios empatados)
        if edades[i] == edad_maxima:
            # Mostramos su nombre
            print(f"  {nombres[i]}")
