import random
vector_numeros = []

#Repetimos 10 veces para rellenar las 10 posiciones
for i in range(10):
    vector_numeros.append(random.randint(1, 10))
#Recorremos cada elemento del vector
for numero in vector_numeros:
    #mostramos el numero, su cuadrado y su cubo
    print(f"Número: {numero} Cuadrado: {numero ** 2} Cubo: {numero ** 3}")

