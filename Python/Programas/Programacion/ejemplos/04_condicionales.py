# Ejemplo 04: sentencia condicional y operador ternario (tema1.pdf, apartado 5)

# ¡OJO! La indentación (los espacios a la izquierda) es la que decide
# qué instrucciones van dentro de cada bloque. No hay llaves {}.

# ------------------------------------------------------------
# if / elif / else
# ------------------------------------------------------------

# Número de ejemplo (en un ejercicio vendría de input)
x = -3
# Si es negativo
if x < 0:
    # Lo ponemos a cero
    x = 0
    # Avisamos (esta línea también está dentro del if)
    print('Puesto a cero')
# Si no, si es cero
elif x == 0:
    # Mensaje para el cero
    print('Cero')
# Si no, si es uno
elif x == 1:
    # Mensaje para el uno
    print('Simple')
# En cualquier otro caso
else:
    # Mensaje para el resto
    print('Más')

# ------------------------------------------------------------
# Condiciones compuestas con and / or / not
# ------------------------------------------------------------

# Nota de ejemplo
nota = 7.5
# Comprobamos el rango con and
if nota >= 0 and nota < 5:
    # Suspenso
    print("Suspenso")
# Rango del aprobado/bien
elif nota >= 5 and nota < 7:
    # Aprobado
    print("Aprobado")
# Rango del notable
elif nota >= 7 and nota < 9:
    # Notable
    print("Notable")
# Rango del sobresaliente
elif nota >= 9 and nota <= 10:
    # Sobresaliente
    print("Sobresaliente")
# Fuera de 0-10
else:
    # Nota no válida
    print("Nota no válida")

# ------------------------------------------------------------
# Operador ternario:
# [valor si se cumple] if [condición] else [valor si no se cumple]
# ------------------------------------------------------------

# Número de ejemplo
n = 6
# Con ternario: todo en una línea
paridad_numero = "es par" if n % 2 == 0 else "es impar"
# Mostramos el resultado
print(n, paridad_numero)

# Lo mismo con if/else normal
if n % 2 == 0:
    # Rama del par
    print("Es par")
else:
    # Rama del impar
    print("Es impar")

# Ejemplo útil en el 3 en raya: qué símbolo dibujar según la ficha
ficha = 2
# 1 es "0", cualquier otro valor es "X"
simbolo = "0" if ficha == 1 else "X"
# Mostramos el símbolo
print("Se dibuja:", simbolo)
