import numpy as np
# 1. Semilla y ventas diarias de un mes (en miles de €)
np.random.seed(42)
ventas = np.random.randint(5, 80, 30)
print("Ventas del mes:", ventas)
# 2. Días con ventas por encima del percentil 90
p90 = np.percentile(ventas, 90)
mascara_top = ventas > p90
print(f"\nPercentil 90: {p90:.2f}k€")
print("Días top:", np.where(mascara_top)[0] + 1)
print("Ventas top:", ventas[mascara_top])
# 3. Fines de semana (suponiendo que el día 1 es lunes)
sabados = ventas[5::7]
domingos = ventas[6::7]
print("\nSábados:", sabados)
print("Domingos:", domingos)
# 4. Ventas entre 10k€ y 20k€ con operadores lógicos
mascara_rango = (ventas >= 10) & (ventas <= 20)
print("\nDías con ventas entre 10k y 20k:", np.where(mascara_rango)[0] + 1)
print("Ventas:", ventas[mascara_rango])
# 5. Fancy indexing: días 1, 5, 10 y 20
dias = np.array([1, 5, 10, 20])
muestra = ventas[dias - 1]  # se resta 1 porque los índices empiezan en 0
print("\nMuestra de días", dias, ":", muestra)