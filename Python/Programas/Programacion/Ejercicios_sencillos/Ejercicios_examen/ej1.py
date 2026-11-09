# Ejercicio 1: 10 multiplicaciones aleatorias y contar los aciertos

# Importamos random para generar números aleatorios
import random

# Contador de respuestas correctas
aciertos = 0
# Repetimos 10 veces (10 preguntas)
for i in range(1, 11):
    # Primer factor aleatorio entre 1 y 10
    a = random.randint(1, 10)
    # Segundo factor aleatorio entre 1 y 10
    b = random.randint(1, 10)
    # Preguntamos la multiplicación y leemos la respuesta
    respuesta = int(input(f"Pregunta {i}: ¿Cuánto es {a} x {b}? "))
    # Si la respuesta es correcta
    if respuesta == a * b:
        # Lo indicamos
        print("¡Correcto!")
        # Sumamos un acierto
        aciertos = aciertos + 1
    # Si es incorrecta
    else:
        # Indicamos cuál era la respuesta correcta
        print(f"Incorrecto. La respuesta correcta es {a * b}")

# Mostramos el número total de aciertos
print(f"\nHas acertado {aciertos} de 10")
