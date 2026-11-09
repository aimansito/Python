# Ejercicio 6: convertir un número (entre 2 y 1000) a número romano

# Valores de las cifras romanas de mayor a menor (incluyendo las restas: 900, 400...)
VALORES = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
# Símbolos que corresponden a cada valor (misma posición)
SIMBOLOS = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

# Pedimos el número
numero = int(input("Introduce un número (mayor que 1 y menor o igual que 1000): "))
# Mientras no esté en el rango pedido, lo volvemos a pedir
while numero <= 1 or numero > 1000:
    # Pedimos de nuevo
    numero = int(input("Fuera de rango. Introduce un número entre 2 y 1000: "))

# Guardamos el original para mostrarlo al final
original = numero
# Cadena donde construimos el número romano
romano = ""
# Recorremos cada valor con su posición
for i in range(len(VALORES)):
    # Mientras el valor quepa en lo que queda del número
    while numero >= VALORES[i]:
        # Añadimos el símbolo
        romano = romano + SIMBOLOS[i]
        # Restamos el valor
        numero = numero - VALORES[i]

# Mostramos el resultado
print(f"{original} en números romanos es {romano}")
