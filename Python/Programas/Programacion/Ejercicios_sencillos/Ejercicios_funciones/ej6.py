# Ejercicio 6: función que calcula el área y el perímetro de una circunferencia

# Importamos math para usar el número pi
import math


# Función que recibe el radio y devuelve el área y el perímetro
def area_perimetro(radio):
    # Área = pi * r al cuadrado
    area = math.pi * radio ** 2
    # Perímetro = 2 * pi * r
    perimetro = 2 * math.pi * radio
    # Devolvemos los dos valores
    return area, perimetro


# Pedimos el radio
radio = float(input("Introduce el radio: "))
# Llamamos a la función y guardamos los resultados
area, perimetro = area_perimetro(radio)
# Mostramos el área con 2 decimales
print(f"Área: {area:.2f}")
# Mostramos el perímetro con 2 decimales
print(f"Perímetro: {perimetro:.2f}")
