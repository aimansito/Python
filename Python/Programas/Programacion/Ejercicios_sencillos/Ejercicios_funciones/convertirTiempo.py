#Funcion que recibe horas, minutos y segundos y devuelve el total en segundos
def a_segundos(horas,minutos,segundos):
    return horas * 3600 + minutos * 60 + segundos

#Funcion que recibe segundos y devuelve horas, minutos y segundos
def a_horas(total_segundos):

    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60
    return horas, minutos, segundos

opcion = ""
while opcion != "3":
    print("\n1. Convertir a segundos")
    print("2.Convertir a horas, minutos y segundos")
    print("Salir")
    opcion = input("Elige opción: ")
    if opcion == "1":
        h = int(input("Horas: "))
        m = int(input("Minutos: "))
        s = int(input("Segundos: "))
        print(f"Son {a_segundos(h,m,s)} segundos")
    elif opcion == "2":
        total = int(input("Segundos: "))
        h, m, s = a_horas
        print(f"Son Horas: {h}, Minutos: {m}, Segundos: {s}")
    elif opcion == "3":
        print("Adios")
    else:
        print("Opcion inválida")