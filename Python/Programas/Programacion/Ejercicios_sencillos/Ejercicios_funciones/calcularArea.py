import math

#Funcion que recibe el radio y devulev el area y el perimetro
def area_perimetro(radio):
    #Area = pi * r al cuadrado
    area = math.pi * radio ** 2
    #Perimetro = 2 * pi * r
    perimetro = 2 * math.pi * radio
    return area, perimetro

radio = float(input("Introduce el radio: "))
area, perimetro = area_perimetro(radio)
# Mostramos el area y el perimetro con 2 decimales
print(f"Area: {area:.2f}")
print(f"Perimetro: {perimetro:.2f}")