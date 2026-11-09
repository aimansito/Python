# Ejercicio 3: contar cuántas veces aparece un carácter en una cadena

# Pedimos la cadena
cadena = input("Introduce una cadena: ")

# Pedimos el carácter que queremos contar
caracter = input("Introduce un carácter: ")
# Validamos que sea un solo carácter: si no, lo repetimos
while len(caracter) != 1:
    # Mostramos el error
    print("Error: Debes introducir un solo carácter.")
    # Volvemos a pedir el carácter
    caracter = input("Introduce un caracter: ")

# Contador de apariciones, empieza en 0
contador = 0
# Recorremos cada letra de la cadena
for letra in cadena:
    # Si la letra coincide con el carácter buscado
    if letra == caracter:
        # Sumamos una aparición
        contador = contador + 1

# Mostramos el resultado
print(f"El caracter '{caracter}' aparece '{contador}' veces en '{cadena}'")
