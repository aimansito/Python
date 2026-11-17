# Ejemplo 07: definición de funciones (tema1.pdf apartado 7 y funciones.pdf)

# ------------------------------------------------------------
# Función sin parámetros
# Se define con def, nombre, paréntesis y dos puntos.
# El código de dentro va indentado.
# ------------------------------------------------------------

def saludo():
    '''
    Muestra un saludo en pantalla
    '''
    # Código de la función
    print('Hola Python')


# Llamada: nombre y paréntesis
saludo()
# help() muestra el comentario de documentación (docstring)
help(saludo)

# ------------------------------------------------------------
# Parámetros y argumentos
# parámetro = la variable de la definición (nombre)
# argumento = el valor que le damos al llamarla ('Juan')
# ------------------------------------------------------------

def saludar_a(nombre):
    '''
    Muestra un saludo en pantalla

    param nombre: a quien saludamos
    '''
    # Usamos el parámetro dentro de la función
    print(f'Hola {nombre}')


# Le pasamos el argumento 'Juan'
saludar_a('Juan')

# ------------------------------------------------------------
# Parámetros con valor por defecto (argumentos no obligatorios)
# ------------------------------------------------------------

def saludo_idioma(nombre='Python', idioma='en'):
    '''
    Muestra un saludo en pantalla

    param nombre: a quien saludamos
    param idioma: 'es' o 'en'
    '''
    # Elegimos el saludo según el idioma
    if idioma == 'es':
        # En español
        print(f'Hola {nombre}')
    else:
        # En inglés
        print(f'Hello {nombre}')


# Sin argumentos: usa los valores por defecto
saludo_idioma()
# Por posición
saludo_idioma('Juan', 'es')
# Por nombre (en el orden que queramos)
saludo_idioma(idioma='es', nombre='Felipe')

# ------------------------------------------------------------
# Funciones que devuelven un valor con return
# ------------------------------------------------------------

def suma(sumando1, sumando2):
    '''
    suma: devuelve la suma de 2 valores

    param sumando1: primer sumando
    param sumando2: segundo sumando

    devuelve el resultado de sumar los dos valores
    '''
    # Calculamos
    resultado = sumando1 + sumando2
    # Devolvemos el resultado a quien llamó
    return resultado


# Guardamos lo que devuelve la función en una variable
res = suma(10, 5)
# Mostramos el resultado
print("10 + 5 =", res)

# Una función puede devolver varios valores separados por comas
def cociente_y_resto(dividendo, divisor):
    # Devolvemos los dos valores a la vez
    return dividendo // divisor, dividendo % divisor


# Recogemos los dos valores en dos variables
c, r = cociente_y_resto(17, 5)
# Mostramos
print("17 entre 5: cociente", c, "resto", r)

# ------------------------------------------------------------
# return también sirve para SALIR de la función en cualquier momento.
# Muy útil para validar parámetros al principio.
# ------------------------------------------------------------

def dividir(a, b):
    '''
    Devuelve a / b, o None si b es 0
    '''
    # Validamos el parámetro: no se puede dividir entre 0
    if b == 0:
        # Avisamos
        print('Se ha producido un error: división entre 0')
        # Salimos de la función sin seguir
        return None
    # Si llegamos aquí, b no es 0
    return a / b


# Llamada correcta
print(dividir(10, 4))
# Llamada con error: devuelve None
print(dividir(10, 0))

# Función que devuelve True o False (muy típico: es_..., hay_...)
def es_par(numero):
    # La comparación ya es True o False
    return numero % 2 == 0


# Usamos la función directamente en un if
if es_par(8):
    # Se ejecuta
    print("8 es par")

# ------------------------------------------------------------
# Indicación de tipos en parámetros y valor devuelto (type hint)
# ------------------------------------------------------------

def area_rectangulo(base: float, altura: float) -> float:
    # Recibe dos float y devuelve un float
    return base * altura


# Llamamos a la función
print("Área:", area_rectangulo(3.0, 2.5))

# ------------------------------------------------------------
# Variables locales y globales
# ------------------------------------------------------------

# Variable global
idioma = 'es'


def cambiar_idioma():
    # Con global decimos que es la variable de fuera, no una nueva
    global idioma
    # Modificamos la global
    idioma = 'en'


# Antes de llamar
print("Idioma antes:", idioma)
# Llamamos a la función que la cambia
cambiar_idioma()
# Después de llamar ha cambiado
print("Idioma después:", idioma)

# Mejor práctica: pasar el dato como parámetro y devolver el resultado
def siguiente_turno(turno_actual):
    # Si era el 1 pasa al 2 y si no al 1
    return 2 if turno_actual == 1 else 1


# Turno inicial
turno = 1
# Cambiamos de turno usando el valor devuelto
turno = siguiente_turno(turno)
# Mostramos
print("Ahora juega el jugador", turno)
