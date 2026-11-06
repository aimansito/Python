import numpy as np
#1. semilla y matriz 10 x 7 (filas = tiendas, columnas = días)
np.random.seed(42)
ventas = np.random.randint(1000,5000, size=(10, 7))
print("Ventas:\n",ventas)
#2. Ventas totales por tienda (suma horizontar -> axis = 1)
total_tienda = ventas.sum(axis=1)
print("\nTotal por tienda:",total_tienda)
#3 media de ventas por dia en toda la cadena(vertical -> axis=0)
media_dia = ventas.mean(axis=0)
dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
for dia, media in zip(dias, media_dia):
    print(f"{dia}: {media:.2f}")
#4 tienda con mejor rendimiento total
mejor = total_tienda.argmax()
print(f"\nMejor tienda: Tienda {mejor + 1} con {total_tienda[mejor]} €")
# 5. Normalizar cada tienda (z-score por fila)
media_tienda = ventas.mean(axis=1, keepdims=True)
std_tienda = ventas.std(axis=1, keepdims=True)
normalizadas = (ventas - media_tienda) / std_tienda
print("\nVentas normalizadas:\n", np.round(normalizadas, 2))