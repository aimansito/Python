# Ejercicio 7: tabla de multiplicar de un número

# Pedimos el número del que queremos la tabla
numero = int(input("Introduce un número: "))
# Recorremos los multiplicadores del 1 al 10
for i in range(1, 11):
    # Mostramos cada línea de la tabla
    print(f"{numero} x {i} = {numero * i}")
