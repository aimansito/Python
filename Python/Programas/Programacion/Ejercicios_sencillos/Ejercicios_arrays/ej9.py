# Ejercicio 9: temperaturas mínimas y máximas de 5 días

# Número de días
DIAS = 5
# Vector de temperaturas mínimas
minimas = []
# Vector de temperaturas máximas
maximas = []

# Pedimos las temperaturas de cada día
for i in range(DIAS):
    # Leemos la mínima del día
    minimas.append(float(input(f"Temperatura mínima del día {i + 1}: ")))
    # Leemos la máxima del día
    maximas.append(float(input(f"Temperatura máxima del día {i + 1}: ")))

# Título del apartado de medias
print("\nTemperatura media de cada día:")
# Recorremos los días
for i in range(DIAS):
    # Calculamos la media de ese día
    media = (minimas[i] + maximas[i]) / 2
    # La mostramos
    print(f"  Día {i + 1}: {media:.1f}")

# Buscamos la temperatura más baja de todas las mínimas
temp_mas_baja = min(minimas)
# Título del apartado
print(f"\nDías con menos temperatura ({temp_mas_baja}):")
# Recorremos los días
for i in range(DIAS):
    # Si la mínima del día es la más baja
    if minimas[i] == temp_mas_baja:
        # Mostramos el día
        print(f"  Día {i + 1}")

# Pedimos una temperatura para buscarla entre las máximas
buscada = float(input("\nIntroduce una temperatura a buscar: "))
# Indica si hemos encontrado algún día
encontrado = False
# Recorremos los días
for i in range(DIAS):
    # Si la máxima del día coincide con la buscada
    if maximas[i] == buscada:
        # Mostramos el día
        print(f"  El día {i + 1} tuvo una máxima de {buscada}")
        # Marcamos que se ha encontrado
        encontrado = True
# Si no se encontró ningún día
if not encontrado:
    # Mostramos un mensaje informativo
    print("Ningún día tuvo esa temperatura máxima")
