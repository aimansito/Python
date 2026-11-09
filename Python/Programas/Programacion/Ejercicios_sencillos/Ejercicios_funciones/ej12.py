# Ejercicio 12: día juliano validando que la fecha introducida sea correcta


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


# NUEVA: devuelve True si la fecha es válida
def validar_fecha(dia, mes, anio):
    # El año tiene que ser positivo
    if anio < 1:
        # Fecha no válida
        return False
    # El mes tiene que estar entre 1 y 12
    if mes < 1 or mes > 12:
        # Fecha no válida
        return False
    # El día tiene que estar entre 1 y los días que tenga ese mes
    if dia < 1 or dia > dias_del_mes(mes, anio):
        # Fecha no válida
        return False
    # Si pasa todas las comprobaciones, es válida
    return True


# Lee una fecha y no la devuelve hasta que sea válida
def leer_fecha():
    # Repetimos hasta que la fecha sea correcta
    while True:
        # Pedimos el día
        dia = int(input("Día: "))
        # Pedimos el mes
        mes = int(input("Mes: "))
        # Pedimos el año
        anio = int(input("Año: "))
        # Si la fecha es válida
        if validar_fecha(dia, mes, anio):
            # La devolvemos (y salimos del bucle)
            return dia, mes, anio
        # Si no es válida, avisamos y se repite el bucle
        print("Fecha no válida, vuelve a introducirla")


# Recibe una fecha y devuelve el día juliano
def calcular_dia_juliano(dia, mes, anio):
    # Empezamos con los días del mes actual
    total = dia
    # Sumamos los días de todos los meses anteriores
    for m in range(1, mes):
        # Añadimos los días del mes m
        total = total + dias_del_mes(m, anio)
    # Devolvemos el total
    return total


# Leemos una fecha (ya validada)
d, m, a = leer_fecha()
# Calculamos y mostramos el día juliano
print(f"El día juliano de {d}/{m}/{a} es {calcular_dia_juliano(d, m, a)}")
