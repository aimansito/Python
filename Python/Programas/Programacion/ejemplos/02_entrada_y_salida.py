# Ejemplo 02: lectura y escritura de datos (tema1.pdf, apartado 3)

# ------------------------------------------------------------
# input(mensaje) muestra el mensaje y devuelve SIEMPRE un str
# ------------------------------------------------------------

# Pedimos el nombre
nombre = input("Introduce tu nombre: ")
# Pedimos el apellido
apellidos = input("Introduce tu apellido: ")
# print separa con un espacio cada valor que le pasamos
print("Te llamas", nombre, apellidos)

# ------------------------------------------------------------
# Para operar con números hay que convertir con int() o float()
# ------------------------------------------------------------

# input devuelve "20" (texto) e int() lo convierte en 20 (número)
edad = int(input("Introduce tu edad: "))
# Ya podemos sumar
print("El año que viene tendrás", edad + 1, "años")

# float() convierte a número decimal
altura = float(input("Introduce tu altura en metros (ej. 1.75): "))
# Mostramos el doble de la altura
print("El doble de tu altura es", altura * 2)

# ------------------------------------------------------------
# Formas de construir el texto a mostrar
# ------------------------------------------------------------

# 1) Varios valores separados por comas (print pone espacios)
print("Nombre:", nombre, "- Edad:", edad)
# 2) Concatenando con + (los números hay que pasarlos a texto con str())
print("Nombre: " + nombre + " - Edad: " + str(edad))
# 3) f-string: una f delante y las variables entre llaves {}
print(f"Nombre: {nombre} - Edad: {edad}")

# ------------------------------------------------------------
# Validar un número leído por teclado SIN que el programa falle.
# Si el usuario escribe letras, int() daría error, así que antes
# comprobamos con .isdigit() que todo son dígitos.
# ------------------------------------------------------------

# Leemos el texto
texto = input("Escribe un número entre 1 y 3: ")
# Repetimos mientras no sea un número o esté fuera del rango
while not texto.isdigit() or int(texto) < 1 or int(texto) > 3:
    # Avisamos del error
    print("Valor no válido.")
    # Volvemos a pedirlo
    texto = input("Escribe un número entre 1 y 3: ")
# Ahora ya es seguro convertirlo
numero = int(texto)
# Mostramos el número válido
print(f"Has elegido el {numero}")
