# Ejemplo 01: variables y tipos de datos (tema1.pdf, apartados 1 y 2)

# ------------------------------------------------------------
# Comentarios
# ------------------------------------------------------------

# Esto es un comentario de una línea: empieza por #

"""
Esto es un comentario de varias líneas.
Se escribe entre tres comillas dobles (o tres simples).
No se ejecuta.
"""

# ------------------------------------------------------------
# Declarar variables: basta con asignarles un valor
# Nombres en minúscula y con _ entre palabras (snake_case)
# No pueden empezar por número ni ser palabras reservadas (if, for, def...)
# ------------------------------------------------------------

# Número entero (int)
numero = 16
# Número decimal (float)
pi = 3.1416
# Cadena de texto (str) con comillas dobles
nombre = "Jose L."
# Cadena de texto con comillas simples
apellidos = 'Berenguel Gómez'
# Nombre de varias palabras: separadas con _
nombre_instituto = 'IES Zaidín-Vergeles'
# Valor lógico (bool): True o False
es_alumno = True

# type() nos dice de qué tipo es cada variable
print(type(numero), type(pi), type(nombre), type(es_alumno))

# ------------------------------------------------------------
# Asignar varias variables en una sola sentencia
# ------------------------------------------------------------

# Las tres valen 7
a = b = c = 7
# x vale 4 e y vale 2
x, y = 4, 2
# a vale 1, b vale 2 y c vale 3
a, b, c = 1, 2, 3
# Varias sentencias en una línea separadas por ; (mejor no abusar)
x = 5; y = 10
# Mostramos los valores
print(a, b, c, x, y)

# ------------------------------------------------------------
# Constantes: Python no tiene constantes "de verdad".
# Por convenio se escriben en MAYÚSCULAS y no se modifican.
# ------------------------------------------------------------

# Valor de una casilla vacía (como en el 3 en raya)
VACIO = 0
# Valor de la ficha del jugador 1
FICHA_O = 1
# Valor de la ficha del jugador 2
FICHA_X = 2
# Mostramos las constantes
print(VACIO, FICHA_O, FICHA_X)

# ------------------------------------------------------------
# Decoración de tipos (type hint): indica el tipo esperado.
# ¡Python NO lo comprueba! Solo sirve para leer mejor el código.
# ------------------------------------------------------------

# Variable de tipo str
ciudad: str = "Granada"
# Variable de tipo int
edad: int = 30
# Mostramos
print(ciudad, edad)

# ------------------------------------------------------------
# Ámbito (scope): una variable dentro de una función es local
# ------------------------------------------------------------

# Variable global (fuera de cualquier función)
valor = 10


# Función con una variable local que se llama igual
def cambiar_valor():
    # Esta "valor" solo existe dentro de la función
    valor = 5
    # Dentro vale 5
    print("Dentro de la función:", valor)


# Llamamos a la función
cambiar_valor()
# Fuera sigue valiendo 10: la de dentro era otra variable
print("Fuera de la función:", valor)
