# Ejercicio 8: mostrar el calendario de un mes (semana empezando en lunes)


# Devuelve True si el año es bisiesto
def es_bisiesto(anio):
    # Bisiesto: divisible entre 4 y no entre 100, o divisible entre 400
    return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0


# Devuelve los días que tiene un mes de un año
def dias_del_mes(mes, anio):
    # Febrero depende del año
    if mes == 2:
        # 29 si es bisiesto, 28 si no
        return 29 if es_bisiesto(anio) else 28
    # Meses de 30 días
    if mes in (4, 6, 9, 11):
        # Devolvemos 30
        return 30
    # El resto tienen 31
    return 31


# Cuenta los días transcurridos desde el 1/1/1900 hasta el día 1 del mes indicado
def dias_desde_1900(mes, anio):
    # Acumulador de días
    total = 0
    # Sumamos los días de cada año completo desde 1900
    for a in range(1900, anio):
        # 366 si es bisiesto, 365 si no
        total = total + (366 if es_bisiesto(a) else 365)
    # Sumamos los días de los meses completos del año pedido
    for m in range(1, mes):
        # Días del mes m
        total = total + dias_del_mes(m, anio)
    # Devolvemos el total
    return total


# Pedimos el mes
mes = int(input("Mes (1-12): "))
# Validamos el mes
while mes < 1 or mes > 12:
    # Lo volvemos a pedir
    mes = int(input("Mes no válido. Mes (1-12): "))
# Pedimos el año
anio = int(input("Año (superior a 1900): "))
# Validamos el año
while anio <= 1900:
    # Lo volvemos a pedir
    anio = int(input("Año no válido. Año (superior a 1900): "))

# El 1/1/1900 fue lunes. Con los días transcurridos módulo 7 obtenemos
# directamente la columna empezando en lunes: 0=lunes, 1=martes ... 6=domingo
# (si contásemos con domingo=0, como dice el enunciado, sería (dias + 1) % 7)
primer_dia = dias_desde_1900(mes, anio) % 7

# Cabecera con los días de la semana
print(" L   M   X   J   V   S   D")
# Línea de separación
print("==========================")
# Escribimos huecos vacíos hasta llegar a la columna del día 1
print("    " * primer_dia, end="")
# Columna actual dentro de la semana
columna = primer_dia
# Recorremos todos los días del mes
for dia in range(1, dias_del_mes(mes, anio) + 1):
    # Escribimos el día ocupando 2 posiciones y 2 espacios de separación
    print(f"{dia:2}  ", end="")
    # Avanzamos una columna
    columna = columna + 1
    # Si hemos llegado al domingo (7 columnas)
    if columna == 7:
        # Saltamos de línea
        print()
        # Volvemos a la primera columna
        columna = 0
# Salto de línea final si la última semana no estaba completa
if columna != 0:
    # Salto de línea
    print()
