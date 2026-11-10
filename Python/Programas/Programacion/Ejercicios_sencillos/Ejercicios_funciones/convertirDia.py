#lee por teclado una fecha y la devuelve como (dia, mes, anio)
def leer_fecha():
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    anio = int(input("Año: "))

    return dia, mes, anio 

#devuelve true si el año es bisiesto
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0

#Devuelve cuantos dias tiene un mes de un año concreto
def dias_del_mes(mes, anio):
    if mes == 2:
        if es_bisiesto(anio):
            return 29
        return 28
    if mes in (4,6,9,11):
        return 30
    return 31


#Recibe una fecha y devuelve el día juliano (numero de dia dentro del año)
def calcular_dia_juliano(dia,mes,anio):
    total = dia
    for m in tange(1,mes):
        ttal = total + dias_del_mes(m,anio)
    return total

#leemos fecha
d,m,a = leer_fecha()
print(f"El día juliano de {d}/{m}/{a} es {calcular_dia_juliano(d, m, a)}")
