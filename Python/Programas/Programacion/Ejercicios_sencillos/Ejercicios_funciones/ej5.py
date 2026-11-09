# Ejercicio 5: función calcularMaxMin que devuelve el máximo y el mínimo de un arreglo


# Función que recibe una lista de números y devuelve (máximo, mínimo)
def calcular_max_min(numeros):
    # Suponemos que el primero es a la vez el máximo
    maximo = numeros[0]
    # Y también el mínimo
    minimo = numeros[0]
    # Recorremos todos los números
    for n in numeros:
        # Si encontramos uno mayor que el máximo actual
        if n > maximo:
            # Actualizamos el máximo
            maximo = n
        # Si encontramos uno menor que el mínimo actual
        if n < minimo:
            # Actualizamos el mínimo
            minimo = n
    # Devolvemos los dos valores a la vez (Python lo empaqueta en una tupla)
    return maximo, minimo


# Pedimos cuántos números se van a introducir
cantidad = int(input("¿Cuántos números vas a introducir? "))
# Mientras la cantidad no sea al menos 1, la volvemos a pedir
while cantidad < 1:
    # Pedimos de nuevo
    cantidad = int(input("Debe ser al menos 1. ¿Cuántos números? "))
# Lista donde guardamos los números
lista = []
# Pedimos cada número
for i in range(cantidad):
    # Leemos el número y lo añadimos a la lista
    lista.append(float(input(f"Número {i + 1}: ")))

# Llamamos a la función y recogemos los dos valores devueltos
maximo, minimo = calcular_max_min(lista)
# Mostramos el máximo
print("Máximo:", maximo)
# Mostramos el mínimo
print("Mínimo:", minimo)
