# Ejemplo 06: funciones built-in y módulos (tema1.pdf, apartado 6)

# ------------------------------------------------------------
# Funciones que ya vienen con Python (no hace falta importar nada)
# ------------------------------------------------------------

# Valor absoluto
print("abs(-7) =", abs(-7))
# Número en binario (como texto)
print("bin(10) =", bin(10))
# Número en hexadecimal
print("hex(255) =", hex(255))
# Número en octal
print("oct(8) =", oct(8))
# Carácter a partir de su código Unicode
print("chr(65) =", chr(65))
# Código Unicode de un carácter
print("ord('A') =", ord('A'))
# Cociente y resto a la vez
cociente, resto = divmod(17, 5)
# Mostramos los dos
print("divmod(17, 5) ->", cociente, resto)
# Potencia (igual que 2 ** 10)
print("pow(2, 10) =", pow(2, 10))
# Conversiones de tipo
print(int("42"), float("3.5"), str(100), bool(0), bool(1))
# Longitud de una cadena o lista
print("len('Python') =", len("Python"))
# Máximo y mínimo
print("max =", max([4, 9, 2]), "min =", min([4, 9, 2]))
# Tipo de un dato
print("type(3.5) =", type(3.5))

# Truco con ord/chr: pasar una minúscula a mayúscula a mano
letra = 'g'
# En Unicode las mayúsculas están 32 posiciones antes que las minúsculas
print(letra, "->", chr(ord(letra) - 32))

# ------------------------------------------------------------
# Módulos: se importan para tener más funciones
# ------------------------------------------------------------

# Importamos el módulo math completo
import math
# Hay que escribir modulo.funcion
print("Raíz de 16:", math.sqrt(16))
# Constante pi del módulo
print("pi =", math.pi)

# Importamos solo lo que necesitamos de un módulo
from math import sqrt
# Ahora se llama directamente, sin "math."
print("Raíz de 25:", sqrt(25))

# Módulo random: números pseudoaleatorios
import random
# Entero aleatorio entre 1 y 6 (ambos incluidos), como un dado
print("Dado:", random.randint(1, 6))
# Elemento aleatorio de una lista
print("Elegido:", random.choice(["piedra", "papel", "tijera"]))
