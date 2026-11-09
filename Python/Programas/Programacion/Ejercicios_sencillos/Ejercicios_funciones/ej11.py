# Ejercicio 11: calcular el día juliano de una fecha


# Lee por teclado una fecha y la devuelve como (dia, mes, anio)
def leer_fecha():
    # Pedimos el día
    dia = int(input("Día: "))
    # Pedimos el mes
    mes = int(input("Mes: "))
    # Pedimos el año
    anio = int(input("Año: "))
    # Devolvemos los tres valores
    return dia, mes, anio


# Devuelve True si el año es bisiesto
def es_bisiesto(anio):
    # Bisiesto: divisible entre 4 y no entre 100, o divisible entre 400
    return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0


# Devuelve cuántos días tiene un mes de un año concreto
def dias_del_mes(mes, anio):
    # Febrero depende de si el año es bisiesto
    if mes == 2:
        # Si es bisiesto tiene 29 días
        if es_bisiesto(anio):
            # Devolvemos 29
            return 29
        # Si no, tiene 28
        return 28
    # Abril, junio, septiembre y noviembre tienen 30 días
    if mes in (4, 6, 9, 11):
        # Devolvemos 30
        return 30
    # El resto de meses tienen 31
    return 31


# Recibe una fecha y devuelve el día juliano (número de día dentro del año)
def calcular_dia_juliano(dia, mes, anio):
    # Empezamos con los días del mes actual
    total = dia
    # Sumamos los días de todos los meses anteriores
    for m in range(1, mes):
        # Añadimos los días del mes m
        total = total + dias_del_mes(m, anio)
    # Devolvemos el total
    return total


# Leemos la fecha
d, m, a = leer_fecha()
# Calculamos y mostramos el día juliano
print(f"El día juliano de {d}/{m}/{a} es {calcular_dia_juliano(d, m, a)}")
