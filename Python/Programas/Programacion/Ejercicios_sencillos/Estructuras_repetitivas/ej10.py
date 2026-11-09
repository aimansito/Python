# Ejercicio 10: tablas de multiplicar del 1 al 5

# Recorremos los números del 1 al 5 (bucle exterior)
for numero in range(1, 6):
    # Mostramos un título para cada tabla
    print(f"--- Tabla del {numero} ---")
    # Recorremos los multiplicadores del 1 al 10 (bucle interior)
    for i in range(1, 11):
        # Mostramos la multiplicación
        print(f"{numero} x {i} = {numero * i}")
