# Ejemplo 03: operadores (tema1.pdf, apartado 4)

# ------------------------------------------------------------
# Operadores aritméticos
# ------------------------------------------------------------

# Suma
print("3 + 5 =", 3 + 5)
# Resta
print("3 - 2 =", 3 - 2)
# Multiplicación
print("12 * 3 =", 12 * 3)
# División: SIEMPRE devuelve decimal (float)
print("5 / 6 =", 5 / 6)
# Módulo: el resto de la división
print("12 % 3 =", 12 % 3)
# División truncada: se queda con la parte entera
print("9 // 2 =", 9 // 2)
# Exponente (potencia)
print("5 ** 2 =", 5 ** 2)

# ------------------------------------------------------------
# Operadores de asignación compuesta
# ------------------------------------------------------------

# Valor inicial
x = 10
# x = x + 2  -> 12
x += 2
# x = x - 1  -> 11
x -= 1
# x = x * 2  -> 22
x *= 2
# x = x // 4 -> 5
x //= 4
# x = x ** 2 -> 25
x **= 2
# x = x / 5  -> 5.0
x /= 5
# Mostramos el resultado
print("x vale", x)

# ------------------------------------------------------------
# Operadores de comparación: devuelven True o False
# ------------------------------------------------------------

# Dos valores para comparar
a, b = 4, 7
# Menor, menor o igual, mayor, mayor o igual
print(a < b, a <= b, a > b, a >= b)
# Igual y distinto
print(a == b, a != b)

# ------------------------------------------------------------
# Operadores lógicos: and, or, not
# ------------------------------------------------------------

# Indica si la partida ha terminado
terminado = False
# not invierte el valor
if not terminado:
    # Se ejecuta porque not False es True
    print("La partida sigue")
# and: las dos condiciones tienen que cumplirse
print("¿a está entre 1 y 5?", a >= 1 and a <= 5)
# or: basta con que se cumpla una
print("¿a es 4 o 9?", a == 4 or a == 9)

# ------------------------------------------------------------
# Operador in: comprueba si un valor está en una lista o cadena
# ------------------------------------------------------------

# Está en la lista
if 2 in [1, 2, 3]:
    # Se ejecuta
    print("El 2 está en la lista")
# También sirve para cadenas
print("¿'o' está en 'hola'?", "o" in "hola")

# ------------------------------------------------------------
# Ejemplos típicos de algoritmia con % y //
# ------------------------------------------------------------

# Un número es par si el resto entre 2 es 0
numero = 17
# Comprobamos
print(numero, "es par" if numero % 2 == 0 else "es impar")
# Última cifra de un número: resto entre 10
print("Última cifra de 1234:", 1234 % 10)
# Quitar la última cifra: división entera entre 10
print("1234 sin la última cifra:", 1234 // 10)
