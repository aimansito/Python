import math
radio = float(input("Introduce el radio del cono: "))
altura = float(input("Introduce la altura del cono:  "))

volumen = (math.pi * radio ** 2 * altura ) / 3

print("El volumen del cono es : ",volumen)