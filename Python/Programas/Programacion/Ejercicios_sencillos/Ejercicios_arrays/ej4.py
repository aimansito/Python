# Ejercicio 4: rellenar un vector de 10 enteros hasta llenarlo o meter un negativo

# Tamaño máximo del vector
TAMANO = 10
# Vector vacío donde iremos guardando los números
vector = []
# Pedimos el primer número
numero = int(input("Introduce un número (negativo para terminar): "))
# Seguimos mientras el número no sea negativo y el vector no esté lleno
while numero >= 0 and len(vector) < TAMANO:
    # Guardamos el número en el vector
    vector.append(numero)
    # Si todavía queda sitio en el vector
    if len(vector) < TAMANO:
        # Pedimos el siguiente número
        numero = int(input("Introduce un número (negativo para terminar): "))

# Mostramos solo los elementos introducidos
print("Elementos introducidos:", vector)
