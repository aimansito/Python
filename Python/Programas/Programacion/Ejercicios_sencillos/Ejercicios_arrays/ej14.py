# Ejercicio 14: precios de 5 artículos y cantidades vendidas en 4 sucursales

# Número de artículos
ARTICULOS = 5
# Número de sucursales
SUCURSALES = 4

# Vector con el precio de cada artículo
precios = []
# Pedimos el precio de cada artículo
for a in range(ARTICULOS):
    # Leemos el precio y lo guardamos
    precios.append(float(input(f"Precio del artículo {a + 1}: ")))

# Tabla de cantidades: cantidades[sucursal][articulo]
cantidades = []
# Recorremos cada sucursal
for s in range(SUCURSALES):
    # Mostramos de qué sucursal pedimos datos
    print(f"\nSucursal {s + 1}")
    # Fila vacía para esta sucursal
    fila = []
    # Recorremos cada artículo
    for a in range(ARTICULOS):
        # Pedimos la cantidad vendida y la guardamos en la fila
        fila.append(int(input(f"  Cantidad vendida del artículo {a + 1}: ")))
    # Añadimos la fila a la tabla
    cantidades.append(fila)

# a) Cantidades totales de cada artículo
print("\nCantidades totales de cada artículo:")
# Recorremos los artículos (columnas)
for a in range(ARTICULOS):
    # Acumulador del artículo
    total = 0
    # Recorremos las sucursales (filas)
    for s in range(SUCURSALES):
        # Sumamos lo vendido en esa sucursal
        total = total + cantidades[s][a]
    # Mostramos el total del artículo
    print(f"  Artículo {a + 1}: {total}")

# b) Cantidad de artículos en la sucursal 2 (índice 1)
print("\nCantidad de artículos en la sucursal 2:", sum(cantidades[1]))

# c) Cantidad del artículo 3 (índice 2) en la sucursal 1 (índice 0)
print("Cantidad del artículo 3 en la sucursal 1:", cantidades[0][2])

# d) Recaudación total de cada sucursal
print("\nRecaudación de cada sucursal:")
# Vector donde guardamos la recaudación de cada sucursal
recaudaciones = []
# Recorremos las sucursales
for s in range(SUCURSALES):
    # Acumulador de dinero de la sucursal
    recaudacion = 0
    # Recorremos los artículos
    for a in range(ARTICULOS):
        # Sumamos cantidad por precio
        recaudacion = recaudacion + cantidades[s][a] * precios[a]
    # Guardamos la recaudación
    recaudaciones.append(recaudacion)
    # La mostramos
    print(f"  Sucursal {s + 1}: {recaudacion:.2f} €")

# e) Recaudación total de la empresa (suma de todas las sucursales)
print(f"\nRecaudación total de la empresa: {sum(recaudaciones):.2f} €")

# f) Sucursal de mayor recaudación: buscamos la posición del valor máximo
mejor = recaudaciones.index(max(recaudaciones))
# Mostramos la sucursal (sumamos 1 porque los índices empiezan en 0)
print(f"Sucursal con mayor recaudación: {mejor + 1}")
