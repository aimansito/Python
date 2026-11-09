# Ejercicio 6: pedir un número de mes y decir su nombre y cuántos días tiene

# Vector con los nombres de los meses (posición 0 = enero)
nombres = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
           "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
# Vector con los días de cada mes (febrero con 28 días)
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Pedimos el número de mes
mes = int(input("Introduce un número de mes (1-12): "))
# Mientras no esté entre 1 y 12, lo volvemos a pedir
while mes < 1 or mes > 12:
    # Pedimos de nuevo el mes
    mes = int(input("Mes no válido. Introduce un número entre 1 y 12: "))
# Restamos 1 porque los vectores empiezan en la posición 0
print(f"{nombres[mes - 1]} tiene {dias[mes - 1]} días")
