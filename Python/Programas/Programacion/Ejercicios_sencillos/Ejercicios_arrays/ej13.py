# Ejercicio 13: conductores y kilómetros de cada día de la semana

# Vector con los nombres de los días de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
# Pedimos cuántos conductores tiene la empresa
num_conductores = int(input("¿Cuántos conductores hay? "))

# Vector con los nombres de los conductores
nombre = []
# Tabla (lista de listas): una fila por conductor y una columna por día
kms = []

# Recorremos cada conductor
for i in range(num_conductores):
    # Pedimos su nombre y lo guardamos
    nombre.append(input(f"\nNombre del conductor {i + 1}: "))
    # Fila vacía para los kilómetros de este conductor
    fila = []
    # Recorremos los días de la semana
    for dia in dias:
        # Pedimos los km de ese día y los añadimos a la fila
        fila.append(float(input(f"  Km del {dia}: ")))
    # Añadimos la fila a la tabla
    kms.append(fila)

# Vector con los kilómetros totales de cada conductor
total_kms = []
# Recorremos cada fila de la tabla
for fila in kms:
    # Sumamos los km de la semana y los guardamos
    total_kms.append(sum(fila))

# Título del listado final
print("\nConductor        Km totales")
# Recorremos cada conductor
for i in range(num_conductores):
    # Mostramos su nombre (alineado a 15 caracteres) y sus km totales
    print(f"{nombre[i]:15}  {total_kms[i]:.1f}")
