# Ejercicio 3: función que calcula la temperatura media de un día


# Función que recibe la máxima y la mínima y devuelve la media
def temperatura_media(maxima, minima):
    # Devolvemos la suma dividida entre 2
    return (maxima + minima) / 2


# Pedimos cuántos días vamos a introducir
dias = int(input("¿Cuántos días vas a introducir? "))
# Recorremos cada día
for i in range(1, dias + 1):
    # Pedimos la temperatura máxima
    maxima = float(input(f"Día {i} - temperatura máxima: "))
    # Pedimos la temperatura mínima
    minima = float(input(f"Día {i} - temperatura mínima: "))
    # Llamamos a la función y mostramos la media
    print(f"Temperatura media del día {i}: {temperatura_media(maxima, minima):.1f}")
