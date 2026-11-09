# Ejercicio 14: punto de encuentro de dos coches en sentido opuesto

# Posición inicial de la primera persona (km 70)
km1 = 70
# Posición inicial de la segunda persona (km 150)
km2 = 150
# Mientras el primer coche no haya alcanzado al segundo
while km1 < km2:
    # El primer coche avanza un kilómetro
    km1 = km1 + 1
    # El segundo coche (sentido opuesto, misma velocidad) retrocede un kilómetro
    km2 = km2 - 1
# Cuando se cruzan, ambos están en el mismo kilómetro
print("Se encontrarán en el kilómetro", km1)
